"""import mariadb
print(mariadb.__version__)
connection = mariadb.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="bc5258034",
    database="mysql",
    autocommit=True
    )
print("connection established successfully.")
def get_employees_by_last_name(connection, last_name):
    sql = "select number,last_name,first_name, salary FROM  WHERE Last_Name = ?"
    cursor = connection.cursor()
    cursor.execute(sql, (last_name,))
    result= cursor.fetchall()
    if result:
        for a in result:
        print(f"hello i am {a[2]} {a[1]}.my salary is {a[3]} euros per month")
    else:
         print(f"no employees found with last name {last_name}.")
    cursor.close()
lastname=input("enter last name to get salary information")
get get_employees_by_last_name(connection, lastname)
connection.close()
print ("connection closed.")"""






