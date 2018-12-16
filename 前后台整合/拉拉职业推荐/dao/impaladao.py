from impala.dbapi import connect


class ImpalaDao():
    def __init__(self):
        self.conn = connect(host='192.168.14.155', port=21050)
        self.cursor = self.conn.cursor()

    def query(self):
        sql = 'select job_title, work_experience, education, work_city, salary, company_size, position, release_date from work.job_info order by unix_timestamp(release_date) desc limit 20 offset 10'
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print(results)

    def queryHotJob(self, job_title=None, experience=None, city=None, salary=None, education=None, curr=1, pagesize=10):
        sql = 'select job_title, work_experience, education, work_city, salary, company_size, position, release_date from work.job_info where 1=1'
        sql1, sql2, sql3, sql4, sql5 = '', '', '', '', ''
        if job_title is not None and job_title is not '':
            sql1 = ' and job_title like "%{0}%"'.format(job_title)
        if experience is not None and experience is not '':
            sql2 = ' and work_experience = {0}'.format(experience)
        if city is not None and city is not '':
            sql3 = ' and work_city = "{0}"'.format(city)
        if salary is not None and salary is not '':
            sql4 = ' and salary > {0}'.format(salary)
        if education is not None and education is not '':
            sql5 = ' and education = "{0}"'.format(education)
        if curr is None:
            curr = 1
        if pagesize is None:
            pagesize = 10
        sql6 = ' order by unix_timestamp(release_date) desc limit {0} offset {1}'.format(pagesize, (curr-1)*pagesize)
        sql = sql + sql1 + sql2 + sql3 + sql4 + sql5 + sql6
        self.cursor.execute(sql)
        print(self.cursor.description)
        results = self.cursor.fetchall()
        print(results)
        return results

    def queryHotJobNum(self, job_title=None, experience=None, city=None, salary=None, education=None):
        sql = 'select count(1) from work.job_info where 1=1 '
        sql1, sql2, sql3, sql4, sql5 = '', '', '', '', ''
        if job_title is not None and job_title is not '':
            sql1 = ' and job_title like "%{0}%"'.format(job_title)
        if experience is not None and experience is not '':
            sql2 = ' and work_experience = {0}'.format(experience)
        if city is not None and city is not '':
            sql3 = ' and work_city = "{0}"'.format(city)
        else:
            sql3 = ' and work_city = "{0}"'.format('武汉')
        if salary is not None and salary is not '':
            sql4 = ' and salary > {0}'.format(salary)
        if education is not None and education is not '':
            sql5 = ' and education = "{0}"'.format(education)
        sql = sql + sql1 + sql2 + sql3 + sql4 + sql5
        print(sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        if results is not None:
            results = results[0][0]
        print(results)
        return results

    def queryAdviserJob(self, job_title=None, experience=None, city=None, salary=None, old=None, position=None,
                        education=None, curr=1, pagesize=10):
        sql = 'select job_title, work_experience, education, work_city, salary, company_size, position, release_date from work.job_info where 1=1'
        sql1, sql2, sql3, sql4, sql5, sql6, sql7 = '', '', '', '', '', '', ''

        if job_title is not None and job_title is not '':
            sql1 = ' and job_title like "%{0}%"'.format(job_title)
        if experience is not None and experience is not '':
            if experience == '0':
                sql2 = ' and work_experience = 0 '
            elif experience == '1':
                sql2 = ' and work_experience >= 1 and work_experience < 3 '
            elif experience == '3':
                sql2 = ' and work_experience >= 3 and work_experience < 5 '
            elif experience == '5':
                sql2 = ' and work_experience >= 5 and work_experience < 10 '
            elif experience == '10':
                sql2 = ' and work_experience >= 10 '
            else:
                sql2 = ' and 1=1 '
        if city is not None and city is not '':
            sql3 = ' and work_city = "{0}"'.format(city)
        else:
            sql3 = ' and work_city = "{0}"'.format('武汉')
        if salary is not None and salary is not '':
            sql4 = ' and salary > {0}'.format(salary)
        if education is not None and education is not '':
            sql5 = ' and education = "{0}"'.format(education)
        if curr is None:
            curr = 1
        if pagesize is None:
            pagesize = 10
        # if old is not None and old is not '':
        #     sql6 = ' and company_name != "{0}"'.format(old)
        if position is not None and position is not '':
            sql7 = ' and position like "%{0}%"'.format(position)

        sql8 = ' order by unix_timestamp(release_date) desc limit {0} offset {1}'.format(pagesize, ((curr - 1) * pagesize))
        sql = sql + sql1 + sql2 + sql3 + sql4 + sql5 + sql6 + sql7 + sql8
        print(sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print(results)
        return results

    def queryAdviserJobNum(self, job_title=None, experience=None, city=None, salary=None, old=None, position=None,
                        education=None):

        sql = 'select count(1) from work.job_info where 1=1'
        sql1, sql2, sql3, sql4, sql5, sql6, sql7 = '', '', '', '', '', '', ''

        if job_title is not None and job_title is not '':
            sql1 = ' and job_title like "%{0}%"'.format(job_title)
        if experience is not None and experience is not '':
            if experience == '0':
                sql2 = ' and work_experience = 0 '
            elif experience == '1':
                sql2 = ' and work_experience >= 1 and work_experience < 3 '
            elif experience == '3':
                sql2 = ' and work_experience >= 3 and work_experience < 5 '
            elif experience == '5':
                sql2 = ' and work_experience >= 5 and work_experience < 10 '
            elif experience == '10':
                sql2 = ' and work_experience >= 10 '
            else:
                sql2 = ' and 1=1 '
        if city is not None and city is not '':
            sql3 = ' and work_city = "{0}"'.format(city)
        else:
            sql3 = ' and work_city = "{0}"'.format('武汉')
        if salary is not None and salary is not '':
            sql4 = ' and salary > {0}'.format(salary)
        if education is not None and education is not '':
            sql5 = ' and education = "{0}"'.format(education)
        # if old is not None and old is not '':
        #     sql6 = ' and company_name != "{0}"'.format(old)
        if position is not None and position is not '':
            sql7 = ' and position like "%{0}%"'.format(position)
        sql = sql + sql1 + sql2 + sql3 + sql4 + sql5 + sql6 + sql7
        print(sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        if results is not None:
            results = results[0][0]
        print(results)
        return results

    # 当前行业的涨幅
    def salaryTop(self, job_title):
        if job_title is None or job_title is '':
            job_title = '大数据'
        sql = 'select sal,  release_date from ( ' \
                'select (max(salary)*0.4 + min(salary)*0.6) as sal, release_date '\
                'from work.job_info ' \
                'where job_title like "%{0}%" '\
                'group by release_date ' \
                'order by sal) t1 ' \
                ' order by unix_timestamp(release_date);'.format(job_title)
        print(sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    # 同等工作经验top10
    def expSalaryTop(self, exp):
        wh = ''
        if exp == '0':
            wh = ' where work_experience = 0 '
        elif exp == '1':
            wh = ' where work_experience >= 1 and work_experience < 3 '
        elif exp == '3':
            wh = ' where work_experience >= 3 and work_experience < 5 '
        elif exp == '5':
            wh = ' where work_experience >= 5 and work_experience < 10 '
        elif exp =='10':
            wh = ' where work_experience >= 10 '
        else:
            wh = ' where 1=1 '

        sql1 ='select t2.* from (select t1.*, row_number() over(partition by work_city order by sal desc) as row_num '\
            ' from (select (max(salary)*0.4 + min(salary)*0.6) sal, position, work_city ' \
            ' from work.job_info '
        sql3 = 'group by work_city, position ) t1 ) t2 where t2.row_num < 11;'
        sql = sql1 + wh + sql3
        print(sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    # 具体工作岗位在每个城市热度
    def workCityHot(self, job_title):
        if job_title is None or job_title is '':
            job_title = '大数据'
        sql = 'select count(1) num, work_city ' \
                'from work.job_info '\
                'where job_title like "%{0}%" ' \
                'group by work_city ' \
                'order by num desc; '.format(job_title)
        print(sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

# ImpalaDao().queryHotJob('大数据', '0', '深圳', '5000')
# ImpalaDao().queryHotJob('大数据')
# ImpalaDao().queryHotJobNum(None)
# ImpalaDao().queryAdviserJob('大数据', '1','深圳','10000','百里半','大数据', '本科')