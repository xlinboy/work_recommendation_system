from multiprocessing import Queue, Process
from gevent import monkey
monkey.patch_all()
import gevent
from bs4 import BeautifulSoup as bs

import requests

def customer(q):
    try:
        while True:
            urls = q.get(timeout=5)
            if urls is None: break
            requests_list = []
            for url in urls:
                with open('C:\\Users\\13194\\Desktop\\资料\\bigdataexam\\task_02\\links_51.txt', 'a',
                          encoding='utf-8') as file:
                    file.write(url)
                    file.write('\n')
                requests_list.append(gevent.spawn(get_page, url))
            gevent.joinall(requests_list)

    except BaseException as base:
        print(base)

def get_page(url):
    headers = {
        'Referer': 'https://search.51job.com/list/000000,000000,0000,01,9,99,%25E4%25BA%2592%25E8%2581%2594%25E7%25BD%2591,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    html = requests.get(url, headers=headers)
    html.encoding = 'gbk'
    save51job(html)

def isEducation(education:str):
    if ("本科" in education or  "大专" in education
            or "中专" in education or "高中" in education
            or "初中" in education or "研究生" in education
            or "博士" in education or "中技" in education
            or "硕士" in education):
        return True
    return False

def excetion_handler(request, exception):
    print(request, exception)
    with open('C:\\Users\\13194\\Desktop\\资料\\bigdataexam\\task_02\\error1.txt', 'a', encoding='utf-8') as file:
        file.write(request)
        file.write('\n')


def save51job(response):
    result = response.text
    soup = bs(result, 'lxml')
    div_company = soup.find(name='div', attrs={'class': 'tCompany_center clearfix'})
    div_headjob = div_company.find(name='div', attrs={'class': 'tHeader tHjob'})
    job_title = deal_word(div_headjob.find(name='h1').get('title'))
    cname_p = div_headjob.find(name='p', attrs={'class': 'cname'})
    company = deal_word(cname_p.find(name='a').get('title'))
    salary_range = deal_word(div_headjob.find(name='strong').string)
    asks_nodeal = div_headjob.find(name='p', attrs={'class': 'msg ltype'}).get('title')
    asks: list = asks_nodeal.split('|')
    if len(asks) < 2: return;
    if not isEducation(asks[2]):
        asks[2:2] = '-'
    if len(asks) == 5:
        asks.append('-')
    elif len(asks) == 6:
        pass
    elif len(asks) == 7:
        tmp = asks.pop()
        asks[6] = asks[6] + '/' + tmp
    else:
        return
    asks = '____'.join(asks)
    # print(asks)
    div_tBorderTop_box = div_company.find(attrs={'class': 'tBorderTop_box'})
    div_job_msg = div_tBorderTop_box.find(attrs={'class': 'bmsg job_msg inbox'})
    # job_msgs_nodeal = div_job_msg.find_all(name='p', attrs={'class': None})
    job_msgs_nodeal = div_job_msg.stripped_strings
    job_msgs = ''
    for msg in job_msgs_nodeal:
        if msg is None:
            continue
        job_msgs += deal_word(msg)
    print(job_msgs)
    div_job_mt10 = div_job_msg.find(name='div', attrs={'class': 'mt10'})
    job_category = deal_word(div_job_mt10.find(name='a', attrs={'class': 'el tdn'}).text)
    div_bmsg = div_company.find(name='div', attrs={'class': 'bmsg inbox'})
    work_space = deal_word(div_bmsg.find(name='p', attrs={'class': 'fp'}).text)
    div_company_siderba = div_company.find(name='div', attrs={'class': 'tCompany_sidebar'})
    div_com_tag = div_company_siderba.find(name='div', attrs={'class': 'com_tag'})
    p_at = div_com_tag.find_all(name='p', attrs={'class': 'at'})
    company_size = deal_word(p_at[1].text)
    company_type = deal_word(p_at[0].text)
    company_class = deal_word(p_at[2].text)
    print(
        job_title + '\t' + asks + '\t' + company + '\t' + salary_range + '\t' + job_category + '\t' + company_type + '\t' + company_size + '\t' + work_space + '\t' + company_class +'\t'+job_msgs)

    with open('C:\\Users\\13194\\Desktop\\资料\\bigdataexam\\task_02\\data1.txt', 'a', encoding='utf-8') as file:
        file.write(job_title + '____' + asks + '____' + company + '____' + salary_range + '____' + job_category + '____' + company_type + '____' + company_size + '____' + company_class +'_____' + work_space + '____' + job_msgs)
        file.write('\n')

def deal_word(word):
    word = word.replace('\n', '').replace('\t', '').replace(' ', '').replace('\r', '').replace(' ','')
    return word

def product(q):
    # list = ['01', '37', '38', '31', '32', '40', '35', '39', '02']
    lists = [['38', '010000'], ['38', '020000'], ['38', '030200'], ['38', '040000'],
                ['38', '180200'], ['38', '200200'],
                ['38', '080200'], ['38', '070200'], ['38', '090200'], ['38', '060000'], ['38', '030800'],
                ['38', '230300'], ['38', '230200'],
                ['38', '070300'], ['38', '250200'], ['38', '190200'], ['38', '150200'], ['38', '080300'],
                ['38', '170200'], ['38', '050000'],
                ['38', '120300'], ['38', '120200'], ['38', '220200'], ['38', '240200'], ['38', '110200'],
                ['31', '010000'], ['31', '020000'],
                ['31', '030200'], ['31', '040000'], ['31', '180200'], ['31', '200200'], ['31', '080200'],
                ['31', '070200'], ['31', '090200'],
                ['31', '060000'], ['31', '030800'], ['31', '230300'], ['31', '230200'], ['31', '070300'],
                ['31', '250200'], ['31', '190200'],
                ['31', '150200'], ['31', '080300'], ['31', '170200'], ['31', '050000'], ['31', '120300'],
                ['31', '120200'], ['31', '220200'],
                ['31', '240200'], ['31', '110200'], ['39', '010000'], ['39', '020000'], ['39', '030200'],
                ['39', '040000'], ['39', '180200'],
                ['39', '200200'], ['39', '080200'], ['39', '070200'], ['39', '090200'], ['39', '060000'],
                ['39', '030800'], ['39', '230300'],
                ['39', '230200'], ['39', '070300'], ['39', '250200'], ['39', '190200'], ['39', '150200'],
                ['39', '080300'], ['39', '170200'],
                ['39', '050000'], ['39', '120300'], ['39', '120200'], ['39', '220200'], ['39', '240200'],
                ['39', '110200'], ['32', '010000'],
                ['32', '020000'], ['32', '030200'], ['32', '040000'], ['32', '180200'], ['32', '200200'],
                ['32', '080200'], ['32', '070200'],
                ['32', '090200'], ['32', '060000'], ['32', '030800'], ['32', '230300'], ['32', '230200'],
                ['32', '070300'], ['32', '250200'],
                ['32', '190200'], ['32', '150200'], ['32', '080300'], ['32', '170200'], ['32', '050000'],
                ['32', '120300'], ['32', '120200'],
                ['32', '220200'], ['32', '240200'], ['32', '110200'], ['40', '010000'], ['40', '020000'],
                ['40', '030200'], ['40', '040000'],
                ['40', '180200'], ['40', '200200'], ['40', '080200'], ['40', '070200'], ['40', '090200'],
                ['40', '060000'], ['40', '030800'],
                ['40', '230300'], ['40', '230200'], ['40', '070300'], ['40', '250200'], ['40', '190200'],
                ['40', '150200'], ['40', '080300'],
                ['40', '170200'], ['40', '050000'], ['40', '120300'], ['40', '120200'], ['40', '220200'],
                ['40', '240200'], ['40', '110200'],
                ['01', '010000'], ['01', '020000'], ['01', '030200'], ['01', '040000'], ['01', '180200'],
                ['01', '200200'], ['01', '080200'],
                ['01', '070200'], ['01', '090200'], ['01', '060000'], ['01', '030800'], ['01', '230300'],
                ['01', '230200'], ['01', '070300'],
                ['01', '250200'], ['01', '190200'], ['01', '150200'], ['01', '080300'], ['01', '170200'],
                ['01', '050000'], ['01', '120300'],
                ['01', '120200'], ['01', '220200'], ['01', '240200'], ['01', '110200'], ['37', '010000'],
                ['37', '020000'], ['37', '030200'],
                ['37', '040000'], ['37', '180200'], ['37', '200200'], ['37', '080200'], ['37', '070200'],
                ['37', '090200'], ['37', '060000'],
                ['37', '030800'], ['37', '230300'], ['37', '230200'], ['37', '070300'], ['37', '250200'],
                ['37', '190200'], ['37', '150200'],
                ['37', '080300'], ['37', '170200'], ['37', '050000'], ['37', '120300'], ['37', '120200'],
                ['37', '220200'], ['37', '240200'],
                ['37', '110200']]

    try:
        for list in lists:
            url = 'https://search.51job.com/list/{1},000000,0000,{0},9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(
                list[0],list[1])
            while True:
                html = getPage(url)
                page_url = get_page_url(html)
                q.put(page_url)
                url = get_next_url(html)
                if url == None:
                    break
    except BaseException as base:
        print(base)

def getPage(url):
    headers = {
        'Referer': 'https://search.51job.com/list/000000,000000,0000,01,9,99,%25E4%25BA%2592%25E8%2581%2594%25E7%25BD%2591,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    html = requests.get(url, headers=headers)
    html.encoding = 'gbk'
    return html.text

def get_page_url(html):
    urls = set()
    soup = bs(html, 'lxml')
    div_list = soup.find(attrs={'id': 'resultList'})
    el_divs = div_list.find_all(attrs={'class' : 'el'})
    for el in el_divs:
        p = el.find(name='p')
        if p == None:
            continue
        a = p.find(name='a')
        urls.add(a.get('href'))
    return urls

def get_next_url(html):
    try:
        soup = bs(html, 'lxml')
        div_list = soup.find(attrs={'id': 'resultList'})
        p_in = div_list.find(attrs={'class': 'p_in'})
        li = p_in.find_all(attrs={'class': 'bk'})
        next_page_url = li[1].find(name='a').get('href')
        return next_page_url
    except:
        return None


if __name__ == '__main__':
    q = Queue(maxsize=1000)
    p1 = Process(target=product, args=(q,))
    p2 = Process(target=product, args=(q,))
    p3 = Process(target=product, args=(q,))
    c1 = Process(target=customer, args=(q,))
    c2 = Process(target=customer, args=(q,))

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    c1.join()
    c2.join()
