def profession(edu):
    if edu == '0':
        edu = ''
    elif edu == '1':
        edu = '大专'
    elif edu == '2':
        edu = '本科'
    elif edu == '3':
        edu = '硕士'
    elif edu == '4':
        edu = '博士'
    else:
        edu = ''
    return edu

def toCity(city):
    if city == '0':
        city = ''
    elif city == '1':
        city = '北京'
    elif city == '2':
        city = '上海'
    elif city == '3':
        city = '广州'
    elif city == '5':
        city = '杭州'
    else:
        city = '深圳'
    return city

def toJob(job):
    if job == '1':
        job = '大数据开发'
    elif job == '2':
        job = 'Python开发工程师'
    elif job == '3':
        job = '全栈工程师'
    elif job == '4':
        job = '软件开发'
    else:
        job = ''
    return job