import json
import mysql.connector as database
from flask import Flask, Response

app = Flask(__name__)

connection = database.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_simulator',
    user = 'root',
    password = 'mkiannu2005#!',
    autocommit = True
)


@app.route('/airport/<icao>')
def prime_number(icao):
    try:
        sql  = f"SELECT airport.name, country.name FROM airport, country WHERE airport.ident = '{icao}' and country.iso_country = airport.iso_country;"

        cursor = connection.cursor()
        cursor.execute(sql)
        airport = cursor.fetchall()[0]

        return {'ICAO': icao, 'Name': airport[0], 'Location': airport[1]}

    except Exception as err:
        response = {
            "message": str(err),
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

app.run(use_reloader = False, host = '127.0.0.1', port = 7000)
