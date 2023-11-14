import json

from flask import Flask, Response

app = Flask(__name__)

@app.route('/prime_number/<num>')
def prime_number(num):
    try:
        prime = True
        num   = int(num)

        for i in range(2, num):
            if num % i == 0:
                prime = False

        return {'Number': num, 'isPrime': prime}

    except Exception as err:
        response = {
            "message": str(err),
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

app.run(use_reloader = False, host = '127.0.0.1', port = 7000)
