import mysql.connector
# Configura la conexión a MySQL
db_config = {
    "user": "root",
    "password": "micaelacorolaire",
    "host": "localhost",
    "database": "petsfastapi",
}

conn = mysql.connector.connect(**db_config)




