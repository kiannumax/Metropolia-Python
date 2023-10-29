
import mysql.connector as database

connection = database.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_simulator',
    user = 'root',
    password = 'mkiannu2005#!',
    autocommit = True
)

def getAirports(aCode):
    sql = (f"select name from airport where iso_country in("
           f"select iso_country from country where iso_country = '{aCode}') "
           f"order by type;")

    cursor = connection.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()
    return result

aCode = input("Enter an area code >> ")

for airport in getAirports(aCode):
    print(airport[0])
