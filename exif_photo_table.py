from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from datetime import datetime

def dms_to_decimal(dms, ref):
    degrees = float(dms[0])
    minutes = float(dms[1])
    seconds = float(dms[2])
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def get_exif(file: Path):
    try:
        with Image.open(file) as img:
            exif = img.getexif()
            if exif is None:
                return {}
            data = {TAGS.get(tag, tag): value for tag, value in exif.items()}
            gps_ifd = exif.get_ifd(34853)  # GPSInfo tag
            if gps_ifd:
                gps = {GPSTAGS.get(key, key): val for key, val in gps_ifd.items()}
                data['GPSInfo'] = gps
            return data
    except Exception:
        return {}

def format_row(file: Path):
    exif = get_exif(file)
    
    make = exif.get('Make', '').strip()
    model = exif.get('Model', '').strip()
    camera = f"{make} {model}".strip() or "Not available"
    
    date_str = exif.get('DateTimeOriginal') or exif.get('DateTime') or "Not available"
    if date_str != "Not available":
        try:
            dt = datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")
            date_str = dt.strftime("%Y-%m-%d %H:%M:%S")
        except:
            pass
    
    exposure = exif.get('ExposureTime')
    if isinstance(exposure, tuple):
        n, d = exposure
        exposure = f"1/{d}" if n == 1 else f"{n}/{d}"
    exposure = str(exposure) or "Not available"
    
    fnumber = exif.get('FNumber')
    if isinstance(fnumber, tuple):
        n, d = fnumber
        fnumber = f"f/{n/d:.1f}"
    aperture = str(fnumber) or "Not available"
    
    iso = str(exif.get('ISOSpeedRatings', "Not available"))
    
    gps = "N/A"
    gps_info = exif.get('GPSInfo', {})
    if gps_info:
        try:
            lat = gps_info.get('GPSLatitude')
            lat_ref = gps_info.get('GPSLatitudeRef')
            lon = gps_info.get('GPSLongitude')
            lon_ref = gps_info.get('GPSLongitudeRef')
            if lat and lat_ref and lon and lon_ref:
                gps = f"{dms_to_decimal(lat, lat_ref):.6f}, {dms_to_decimal(lon, lon_ref):.6f}"
        except:
            gps = "Error parsing GPS"
    
    return {
        "File": file.name,
        "Camera": camera,
        "Taken": date_str,
        "Exposure": exposure,
        "Aperture": aperture,
        "ISO": iso,
        "GPS": gps
    }

def main():
    folder = Path.cwd()
    print(f"\nScanning folder: {folder}\n")
    
    exts = {'.jpg', '.jpeg', '.heic', '.HEIC'}
    photos = [p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in exts]
    
    if not photos:
        print("No JPG or HEIC photos found in this folder. Drop some photos here and try again!")
        return
    
    print(f"Found {len(photos)} photos. Extracting EXIF...\n")
    
    rows = [format_row(p) for p in sorted(photos)]
    
    headers = list(rows[0].keys())
    widths = {h: max(len(h), max(len(str(r[h])) for r in rows)) + 2 for h in headers}
    
    print(" ".join(h.ljust(widths[h]) for h in headers))
    print("-" * sum(widths.values()))
    for row in rows:
        print(" ".join(str(row[h]).ljust(widths[h]) for h in headers))

if __name__ == "__main__":
    main()