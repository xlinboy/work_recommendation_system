from flask import Blueprint, request, render_template, redirect, url_for, session

import Utils
from dao.impaladao import ImpalaDao as idao
from dao.topndao import TopnDao as tdao

base = Blueprint('base', __name__)


@base.route('/toregister', methods=['get', 'post'])
def toregister():
    return render_template('register.html')


@base.route('/register', methods=['get', 'post'])
def register():
    name = request.args.get('username')
    experience = request.form.get('experience')
    edate = request.args.get('edate')
    city = request.form.get('city')
    job_title = request.form.get('job_title')
    position = request.args.get('position')
    sex = request.args.get('sex')
    message = request.args.get('message')
    old_company = request.args.get('old_company')
    education = request.args.get('education')
    curr = request.args.get('current')
    pagesize = request.args.get('pagesize')
    sal = request.form.get('salary')
    session['job_title'] = job_title
    session['exp'] = experience
    if curr is None:
        curr = 1
    if pagesize is None:
        pagesize = 10
    if job_title is None:
        job_title = ''
    if experience is None or experience == '不限':
        experience = ''
    if city is None or city == '不限':
        city = ''
    if sal is None or sal == '不限':
        sal = ''
    if education is None or education == '不限':
        education = ''
    education = Utils.profession(education)
    position = Utils.toJob(position)
    totalpage = idao().queryAdviserJobNum(job_title, experience, city, sal, old_company, position, education)
    items = idao().queryAdviserJob(job_title, experience, city, sal, old_company, position, education, int(curr),
                                   int(pagesize))
    if items is None or len(items) < 1:
        job_title = '大数据'
        city = '深圳'
        items = idao().queryAdviserJob(job_title, experience, city, sal, old_company, position, education, int(curr),
                                       int(pagesize))
    return render_template('adviser.html', items=items, curr=curr, pagesize=pagesize, position=position,
                           total=totalpage, job_title=job_title, edu=education,
                           city=city, exp=experience, sal=sal)


@base.route('/allSalaryTopn')
def allTopn():
    results = tdao().findAllTopnDao()
    return render_template('all_topn_dao.html', results=results)


@base.route('/maxSalaryTopn')
def maxSalaryTopn():
    results = tdao().findMaxSalaryTop()
    data1, data2 = [], []
    for result in results:
        data1.append(result[1])
        data2.append(result[0])
    return render_template('max_salary_top.html', data1=data1, data2=data2)


@base.route('/hotCityWorkTop')
def hotCityWorkTop():
    results = tdao().findHotCityWorkTop()
    data1, data2 = [], []
    for result in results:
        data1.append(result[1])
        data2.append(result[0])
    return render_template('hot_city_work_top.html', data1=data1, data2=data2)


@base.route('/salaryTop')
def salaryTop():
    job_title = request.args.get('job_title')
    results = idao().salaryTop(job_title)
    data1, data2 = [], []
    for result in results:
        data1.append(result[1])
        data2.append(result[0])
    return render_template('salary_top.html', data1=data1, data2=data2)


@base.route('/workCityHot')
def workCityHot():
    job_title = request.args.get('job_title')
    results = idao().workCityHot(job_title)
    data1, data2 = [], []
    for result in results:
        data1.append(result[1])
        data2.append(result[0])
    return render_template('work_city_top.html', data1=data1, data2=data2)


@base.route('/expSalaryTop')
def expSalaryTop():
    exp = request.args.get('arg')
    results = idao().expSalaryTop(exp)
    return render_template('exp_salary_top.html', results=results)
