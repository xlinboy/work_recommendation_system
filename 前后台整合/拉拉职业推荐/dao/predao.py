import pymysql

class PreDao():
    def __init__(self):
        self.conn = pymysql.connect(host='hadoop1', port=3306,
                                    user='root', passwd='123456',
                                    db='test', charset='utf8mb4')
        self.curser = self.conn.cursor()

    def queryCitysById(self, city):
        sql = 'select id from city where 1=1 and city like "%"+{0}+"%"'
        print(sql.format(city))
        self.curser.execute(sql.format(city))
        results = self.curser.fetchall()
        return results

    def queryPostitionsId(self, position):
        sql = 'select id from position where 1=1 and position like "%"+{0}+"%"'
        print(sql.format(position))
        self.curser.execute(sql.format(position))
        results = self.curser.fetchall()
        return results