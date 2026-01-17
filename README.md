# Terminal Photo Exif Viewer 📸

A lightweight Python script that scans a folder of photos (JPEG, HEIC) and prints a beautifully formatted table of their EXIF metadata.

Perfect for photographers, travelers, or anyone who wants a quick overview of camera info, dates, exposure settings, and GPS from a bunch of images at once.

### Features

- Supports JPG/JPEG and HEIC files (common on iPhone & newer cameras)
- Shows:  
  - File name  
  - Camera make & model  
  - Date taken  
  - Exposure time  
  - Aperture (f-stop)  
  - ISO  
  - GPS coordinates (if available)  
- Handles missing data gracefully with "N/A" or "None"
- Auto-scans the current folder — no typing long paths
- Clean, aligned console table output

  ### If you don't want to make it your self
  You can Go to [Exif-Viewer](https://exif-dashboard.streamlit.app)
  

### Requirements

- Python 3.8+
- Pillow library (`pip install pillow`)

### Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/alxgraphy/photo-exif-previewer-.git
   cd photo-exif-previewer-

Create and activate a virtual environment (recommended):Bashpython3 -m venv .venv
source .venv/bin/activate          # macOS / Linux
# OR on Windows: .venv\Scripts\activate
Install the dependency:Bashpip install pillow
Run the script:Bashpython exif_photo_table.pyDrop your photos (JPG/HEIC) directly into the folder and run it again — it scans automatically!

Tips & Customization

Scan a different folder? Edit folder = Path.cwd() in main() to folder = Path("/path/to/your/photos")
Missing exposure/aperture? Some edited/exported photos strip technical EXIF tags — that's normal.
HEIC support works great on recent macOS/Windows with Pillow installed.
Want CSV export? Add pandas and save the table (let me know if you want that upgrade!)


### Additional Stuff
Feel free to fork, modify, use, and share — open an issue/PR if you like it or want improvements!

Made with ❤️ in Toronto, Canada 🇨🇦 by Alexander Wondwossen (@alxgraphy)

### License
Copyright 2026 Alexander Wondwossen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
