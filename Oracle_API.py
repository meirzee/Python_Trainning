import cx_Oracle
 
query = 'select product from products'
 

 
#connect to database and execute query.
db = cx_Oracle.connect('CMMON', 'CMMON', 'illin629:1521/PCIPROD')
cursor = db.cursor()
cursor.execute(query)
 
#loop through the rows fetched and store the records as arrays.
for row in cursor:
    print (row[0])