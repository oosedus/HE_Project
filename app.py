from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def process_csv(file_path):
    # 여기에 CSV 처리 로직을 구현하세요.
    # 현재는 더미 데이터로 응답합니다.
    return [
        {"timestamp": ["2025-05-12T12:00:00", "2025-05-12T12:01:00"], "anomalyResult": True},
        {"timestamp": "2025-05-12T12:02:00", "anomalyResult": False},
        {"timestamp": ["2025-05-12T12:03:00", "2025-05-12T12:04:00"], "anomalyResult": True}
    ]

@app.route("/upload", methods=["POST"])
def upload_csv():
    if 'csvFile' not in request.files:
        return jsonify({"error": "No file uploaded."}), 400

    file = request.files['csvFile']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        results = process_csv(file_path)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
