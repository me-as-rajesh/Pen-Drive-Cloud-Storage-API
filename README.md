# Pen-Drive Cloud Storage API

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)

## Overview
A lightweight Flask-based API that turns a USB pen drive into a personal cloud storage device, allowing file uploads, downloads, and management through a simple web interface.

## Features
✅ **File Upload/Download** - Store and retrieve files from your pen drive  
🔍 **File Listing** - View all files with sizes and download links  
🗑️ **File Deletion** - Remove unwanted files  
📊 **Storage Monitoring** - Track total storage usage  
🌐 **Web Interface** - Simple HTML dashboard for easy management  
🔒 **Local Network Access** - No internet required after setup  

---
## Requirements
- Python 3.8+
- Flask
- A USB pen drive (formatted with a compatible file system)

---
## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/pen-drive-cloud-storage.git
   cd pen-drive-cloud-storage
   ```

2. Install dependencies:
   ```sh
   pip install flask
   ```

3. Configure the storage path:
   - Edit `app.py` and modify the `STORAGE_PATH` variable to match your pen drive's mount point:
   ```python
   STORAGE_PATH = "F:/"  # Change this to your pen drive path (e.g., "/media/usb" on Linux)
   ```

---
## Usage
1. Plug in your USB pen drive.
2. Run the application:
   ```sh
   python app.py
   ```
3. Open your browser and navigate to `http://localhost:5000/`

---
## API Endpoints

| Endpoint           | Method  | Description       |
|--------------------|---------|-------------------|
| `/`               | GET     | Web dashboard     |
| `/upload`         | POST    | Upload files      |
| `/download/<file>`| GET     | Download files    |
| `/files`          | GET     | List all files    |
| `/delete/<file>`  | DELETE  | Delete files      |

---
## License
This project is open-source and available under the [MIT License](LICENSE).

---
## Contributions
Feel free to fork this repository and submit pull requests! Any improvements and suggestions are welcome.

---
## Author
[rajesh](https://github.com/me-as-rajesh)

