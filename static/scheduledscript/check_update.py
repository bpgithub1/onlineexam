#---------This script is scheduled to run every mid night to check and update necessary values in database-----------
#---Develop this script and test it

from django.db import connection
#---------------
cursor=connection.cursor()
cursor.execute('select * from teacher_exam')
result=cursor.fetchall()  
connection.close()
print("BP CHECK ==> ",result)