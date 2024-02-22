import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd="",
    # database="master_python"
)

cursor = database.cursor(buffered=True)

cursor.execute("CREATE DATABASE IF NO EXISTS master_python")

cursor.exeute("SHOW DATABASES")

for bd in cursor:
    print(bd)

cursor.execute("""
CREATE TABLE IF NO EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,        
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)                                                                 
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

cursor.execute("INSERT INTO vehiculos VALUES(null,'Opel','Astra',18500)")

database.commit()

cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()

for coche in result:
    print(coche)

cursor.execute("DELETE FROM vehiculos WHERE marca='Renault'")    
database.commit()

print(cursor.rowcount, "borrados")

cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marcar = 'Seat'")
database.commit()