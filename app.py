import json
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f"Welcome to the API"


@app.route('/list')
def list_available_files():
    with open("/home/jhoskins/mysite/file.download.json", "rb") as json_file:
        meta_data = json.load(json_file)

    key_list = {}
    for i, key in enumerate(meta_data.keys()):
        key_list[i] = key

    return key_list


@app.route('/meta/<file_name>', methods=["GET"])
def get_meta_data(file_name):
    with open("file.download.json", "rb") as json_file:
        meta_data = json.load(json_file)

    if file_name in meta_data.keys():
        return meta_data[file_name]

    else:
        return f"Error, {file_name} not found in file metadata."
