from flask import Flask, request, jsonify
import requests
from axon.integrations.flask import instrument_with_axon

app = Flask(__name__)

instrument_with_axon(app)

@app.route('/s/getresult/')
def get_result():
    return {"result": 11}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
