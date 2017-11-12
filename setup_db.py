import os
from flask_mysqldb import MySQL


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'yourkraft'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


cur = mysql.connection.cursor()

cur.execute("create table users(Username varchar(30) primary key,Email varchar(35),Password varchar(100),Type_Acc varchar(10) default='artist' )")

cur.close()
