from flask import Flask, request
import json
import pandas as pd
from io import StringIO
import ia
import matplotlib

app = Flask(__name__)
processor = ia.IAProcessor()
matplotlib.use('agg')

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
    data = str(file.read(),'utf-8').split("---\r\n")

    print(data)

    trainDF = pd.read_csv(StringIO(data[0]))
    testDF = pd.read_csv(StringIO(data[1]))
    field = data[2].rstrip()
    k = int(data[3].rstrip())
    responseData = processor.process(trainDF, testDF, field, k)

    # return success
    return json.dumps({'status': True, 'data': responseData}), 200

if __name__ == '__main__':
    app.run()
