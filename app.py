import mysql.connector

try:
    conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ",
    database="hii"
)

    if conn.is_connected():
        print("database connected successfully")
    else:
        print("database is not connected")

except mysql.connector.Error as err:
    print(f"error: (err)")

finally:
    if conn.isconnected():
        conn.close()
        print("connection closed")
    
    