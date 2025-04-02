from flask import Flask, request, send_file, jsonify, render_template
import os
import shutil

app = Flask(__name__)

# Set the pen drive storage path
STORAGE_PATH = "D:/"  # Change this to your pen drive path

# Ensure the storage directory exists
if not os.path.exists(STORAGE_PATH):
    try:
        os.makedirs(STORAGE_PATH)
    except OSError as e:
        print(f"Error: Could not create directory on F:/ - {e}")
        exit(1)

# Helper function to get file size
def get_file_size(file_path):
    return round(os.path.getsize(file_path) / 1024, 2)

@app.route('/')
def index():
    return render_template('appindex.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    file_path = os.path.join(STORAGE_PATH, file.filename)
    
    if os.path.exists(file_path):
        return jsonify({"error": "File already exists"}), 400
    
    file.save(file_path)
    return jsonify({
        "message": f"File '{file.filename}' uploaded",
        "size_kb": get_file_size(file_path),
        "filename": file.filename
    }), 201

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(STORAGE_PATH, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return jsonify({"error": "File not found"}), 404

@app.route('/files', methods=['GET'])
def list_files():
    files = []
    total_size = 0
    try:
        for filename in os.listdir(STORAGE_PATH):
            file_path = os.path.join(STORAGE_PATH, filename)
            if os.path.isfile(file_path):
                size_kb = get_file_size(file_path)
                files.append({
                    "name": filename, 
                    "size_kb": size_kb,
                    "url": f"/download/{filename}"
                })
                total_size += size_kb
        return jsonify({
            "files": files, 
            "total_size_kb": round(total_size, 2),
            "storage_path": STORAGE_PATH
        })
    except OSError as e:
        return jsonify({"error": f"Could not access storage - {e}"}), 500

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = os.path.join(STORAGE_PATH, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": f"File '{filename}' deleted"})
    return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    if not os.path.exists(STORAGE_PATH):
        print(f"Error: {STORAGE_PATH} not found. Please check your storage device.")
        exit(1)
    app.run(debug=True, host='0.0.0.0', port=5000)