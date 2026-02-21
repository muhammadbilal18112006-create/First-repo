#QUESTION NO 1

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

icao = input("Enter ICAO code: ")

cursor = connection.cursor()
cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao,))
result = cursor.fetchone()

if result:
    print(f"Airport: {result[0]}")
    print(f"Location: {result[1]}")
else:
    print("Airport not found.")

#QUESTION NO 2

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

country_code = input("Enter country code (e.g. FI): ")

cursor = connection.cursor()
cursor.execute(
    "SELECT type, COUNT(*) AS count FROM airport WHERE iso_country = %s GROUP BY type ORDER BY count DESC",
    (country_code,)
)
results = cursor.fetchall()

if results:
    print(f"\nAirports in {country_code}:")
    for row in results:
        print(f"  {row[0]}: {row[1]}")
else:
    print("No airports found for that country code.")


#QUESTION NO 3

import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

icao1 = input("Enter first ICAO code: ")
icao2 = input("Enter second ICAO code: ")

cursor = connection.cursor()

cursor.execute("SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao1,))
airport1 = cursor.fetchone()

cursor.execute("SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao2,))
airport2 = cursor.fetchone()

if airport1 and airport2:
    coords1 = (airport1[1], airport1[2])
    coords2 = (airport2[1], airport2[2])
    distance = geodesic(coords1, coords2).km
    print(f"\n{airport1[0]} ({icao1}) -> {airport2[0]} ({icao2})")
    print(f"Distance: {distance:.2f} km")
else:
    if not airport1:
        print(f"Airport {icao1} not found.")
    if not airport2:
        print(f"Airport {icao2} not found.")

