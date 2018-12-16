# coding=utf8
import pymysql


# 此处报一个异常
class TopnDao(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    passwd='root',
                                    db='blog'
                                    )
        self.curser = self.conn.cursor()

    def findAllTopnDao(self):
        sql = 'select * from all_salary_top order by work_city'
        self.curser.execute(sql)
        results = self.curser.fetchall()
        print(results)
        return results

    def findCitys(self):
        sql = 'select * from city'
        self.curser.execute(sql)
        results = self.curser.fetchall()
        print(results)
        return results

    def findPositions(self):
        sql = 'select * from position'
        self.curser.execute(sql)
        results = self.curser.fetchall()
        print(results)
        return results

    def findMaxSalaryTop(self):
        sql = 'select * from max_salary_top'
        self.curser.execute(sql)
        results = self.curser.fetchall()
        print(results)
        return results

    def findHotCityWorkTop(self):
        sql = 'select * from hot_city_work_top ORDER BY (num+0) desc'
        self.curser.execute(sql)
        results = self.curser.fetchall()
        print(results)
        return results

# TopnDao().findAllTopnDao()
# TopnDao().findCitys()
# TopnDao().findPositions()
TopnDao().findHotCityWorkTop()
# TopnDao().findMaxSalaryTop()