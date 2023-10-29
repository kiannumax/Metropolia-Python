
import mysql.connector as database
from geopy import distance

connection = database.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_simulator',
    user = 'root',
    password = 'mkiannu2005#!',
    autocommit = True
)

def getDegrees(ICAO):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ICAO}';"

    cursor = connection.cursor()
    cursor.execute(sql)

    return cursor.fetchall()[0]


def getDistance(ICAO1, ICAO2):
    degrees1 = getDegrees(ICAO1)
    degrees2 = getDegrees(ICAO2)

    return distance.distance(degrees1, degrees2).km


ICAO1 = input("Enter first airport's ICAO >> ")
ICAO2 = input("Enter second airport's ICAO >> ")

print(f"The distance in km is: {(getDistance(ICAO1, ICAO2)):.0f}")
