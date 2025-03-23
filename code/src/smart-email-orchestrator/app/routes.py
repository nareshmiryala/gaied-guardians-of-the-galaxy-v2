import json
from flask import request, render_template, jsonify, send_file, Blueprint
import os
import shutil
from werkzeug.utils import secure_filename
from app.utils.email_extraction import process_emails
from app import app

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/upload", methods=["POST"])
def upload():
    """Handles file uploads."""
    if "files" not in request.files:
        return jsonify({"error": "No files uploaded"}), 400

    shutil.rmtree(app.config["UPLOAD_FOLDER"])  # Clean previous files
    os.makedirs(app.config["UPLOAD_FOLDER"])

    for file in request.files.getlist("files"):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    process_emails(app.config["UPLOAD_FOLDER"], app.config)
    return jsonify({"message": "Processing complete!"})

@bp.route("/download")
def download():
    return send_file(app.config["OUTPUT_FILE"], as_attachment=True)

@bp.route('/view_output')
def view_output():
    data = load_json()
    return render_template('output.html', data=data)

def load_json():
    with open(app.config["OUTPUT_FILE"], "r") as file:
        return json.load(file)

def init_app(app):
    app.register_blueprint(bp)