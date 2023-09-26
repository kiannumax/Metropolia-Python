
import mysql.connector as database

connection = database.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_simulator',
    user = 'root',
    password = 'mkiannu2005#!',
    autocommit = True
)

def getAirportCountry(ICAO):
    sql = (f"SELECT airport.name, country.name FROM airport, country "
           f"WHERE ident = '{ICAO}' and  airport.iso_country = country.iso_country;")

    cursor = connection.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()[0]
    return f"This airport's country is {result[1]}, and name: {result[0]}"

ICAO = input("Enter airport's ICAO >> ")

print(getAirportCountry(ICAO))
