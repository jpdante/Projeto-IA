from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/ia/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return json.dumps({'status': 'Error', 'message': 'No file part in the request'}), 400

    file = request.files['file']
    
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return json.dumps({'status': 'Error', 'message': 'No file selected'}), 400
    
    # read the file and do something with it
    data = file.read()
    # for example, you could parse the CSV data here using a library like pandas

    # return success
    return json.dumps({'status': 'OK'}), 200

if __name__ == '__main__':
    app.run()
