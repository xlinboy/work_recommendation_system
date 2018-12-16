import os

from flask import Flask,render_template,request,url_for,redirect,session

import Utils
from controller.base import base

from dao.impaladao import ImpalaDao as idao

app = Flask(__name__)
app.register_blueprint(base, url_prefix='/base')
app.config['SECRET_KEY']= os.urandom(24)

@app.route('/')
def hello_world():
    # return redirect('/pageview')
    return render_template('register.html')

@app.route('/pageview', methods=['get','post'])
def pageview():
    job_title = request.form.get('job_title')
    session['job_title'] = job_title
    experience = request.form.get('experience')
    city = request.form.get('city')
    curr = request.form.get('curr')
    salary = request.form.get('salary')
    pagesize = request.form.get('pagesize')
    education = request.form.get('education')
    if curr is None:
        curr = 1
    if pagesize is None:
        pagesize = 10
    if job_title is None:
        job_title = '大数据'
    if experience is None or experience == '不限':
        experience = ''
    if city is None or city == '不限':
        city = ''
    if salary is None or salary == '不限':
        salary = ''
    if education is None or education == '不限':
        education = ''
    education = Utils.profession(education)
    city = Utils.toCity(city)
    totalpage = idao().queryHotJobNum(job_title, experience, city, salary, education)
    items = idao().queryHotJob(job_title, experience, city, salary, education, int(curr), int(pagesize))
    if len(items) < 1:
        job_title = '大数据'
        city = '深圳'
        items = idao().queryHotJob(job_title, experience, city, salary, education, int(curr), int(pagesize))
    return render_template('hotjob.html', items=items, curr=curr, pagesize=pagesize,
                           total=totalpage, job_title=job_title, edu = education,
                           city = city, exp = experience, sal = salary)


if __name__ == '__main__':
    app.run()
