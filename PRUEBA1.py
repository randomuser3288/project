import sqlite3
# Connexion to database
connection = sqlite3.connect('databasexxxxxx.db')
cursor = connection.cursor()
# Crear tabla de edificios
cursor.execute('''CREATE TABLE buildings (
                   name TEXT,
                   location TEXT,
                   description INTEGER)''')
# Inserts data
cursor.execute('''INSTERT INTO buildings VALUES
('TUM Aerospace and Geodesy','48.05466205512792, 11.653800678322426','This building is for aerospace research'),              
('TUM Campus Garching','48.26585215006792, 11.673009411689836','This campus is of very much interest')
''')
# Saves changes and closes connection 
connection.commit()
connection.close()
rows = cursor.fetchall()
print(rows)