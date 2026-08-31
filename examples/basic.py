from mydb.database import DataBase

# Create a database
db = DataBase("./data")
print("Database created successfully at ", db.path)