# encoding=utf8
import pymysql
pymysql.install_as_MySQLdb()


config= {
    'host' : 'localhost',
    'user' : 'root',
    'password' : '123456',
    'port' : 3306,
    'databases' : 'info'

}

conn = pymysql.connect()

curs = conn.cursor()
curs.execute("drop table if exists info")
sql = """create table info(name char(20) not null, 
                            password varchar(20),
                            age int,
                            sex char 
                        
                          )"""
curs.execute(sql)

sql = "insert into info values ('daniel','daniel22222', 24, 'M')"
curs.execute(sql)

conn.commit()




conn.close()

