import mysql.connector


conn=mysql.connector.connect(host='localhost',username='root',password='rishimahur@5678')
my_cursor=conn.cursor()

conn.commit()
conn.close

print("connection succesfully created!")