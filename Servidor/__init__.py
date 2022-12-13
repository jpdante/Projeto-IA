from flask import Flask, request
import json
import pandas as pd
from io import StringIO
import ia

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
    df = pd.read_csv(StringIO(str(data,'utf-8')))
    processor = ia.IAProcessor()
    processor.process(df)

    # return success
    return json.dumps({'status': 'OK'}), 200

if __name__ == '__main__':
    app.run()
