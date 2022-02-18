import cx_Oracle

userpwd = "ellplnsc"

cx_Oracle.init_oracle_client(lib_dir=r"D:\DataBackup\Documents\GitHub\instantclient-basic-windows.x64-21.3.0.0.0\instantclient_21_3")
test = []
pool = cx_Oracle.SessionPool(user="ellipse", password=userpwd, dsn="172.16.10.6:1521/ellplnsc", encoding="UTF-8")
connection = pool.acquire()
cursor = connection.cursor()
for result in cursor.execute("select * from MSF810"):
    test.append(result)
print(test)

pool.release(connection)
pool.close()