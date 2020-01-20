# encoding=utf8
import pymysql
pymysql.install_as_MySQLdb()


class Database():
    __db = None
    __curs = None
    __data = None

    def __init__(self, *args, **kwargs):

        host = 'host' in kwargs and kwargs['host'] or 'localhost'
        port = 'port' in kwargs and kwargs['port'] or '3306'
        user = 'user' in kwargs and kwargs['user'] or 'root'
        password = 'password' in kwargs and kwargs['password'] or '123456'
        db = 'db' in kwargs and kwargs['db'] or 'daniel'
        charset = 'charset' in kwargs and kwargs['charset'] or 'utf8'

        self.__db = pymysql.connect(host=host, port=int(port), user=user, password=password, db=db, charset=charset )

        self.__curs = self.__db.cursor()
        # self.__curs = self.__db.cursor(cursor=pymysql.cursors.DictCursor)

    def insert(self, sql):
        self.__curs.execute(sql)
        self.__db.commit()
        return

    def delete(self, sql):
        self.__curs.execute(sql)
        self.__db.commit()
        return

    def updata(self, sql):
        self.__curs.execute(sql)
        self.__db.commit()
        return

    def select(self, sql):
        self.__curs.execute(sql)
        self.__data = self.__curs.fetchall()
        return self.__data


base = Database()

# 这个语句INSERT的是空的
base.insert('insert into daniel.info values (info.name="NN", info.password="00", info.age=1, info.sex="M")')
# 　这个可以insert
base.insert('insert into daniel.info values ("wori", "wowo00",22, "F")')

base.delete('delete from info where info.age is NULL ')
# base.updata('update info set age=20 where age=12')
data =base.select('select * from info')
print(data)