
## 1. spider_code
- 主要是一些爬虫代码， 指标分析需要相当的数据量， 所以需要一些测试数据，本系统数据来源是51Job。

## 2. 数据清洗
- 尽量保证数据完整、一致性的条件下，做数据清洗。
- 去掉重复的数据。
- 将一些String字段，转换成的数字的字段，方便后期做数据分析。

### 2.1 数据字段
1. job_title string 职业标题
2. work_city string 工作城市
3. work_experience int 工作经验
4. education string 教育经历
5. company_demand string 招人要求
6. other_asks string 公司其他要求
7. company_name string 公司名称
8. salary float 工资
9. position string 职能
10. company_type string 公司类型
11. company_size string 公司规模
12. address string 公司地址
13. job_message string 工作简介

## 3. 指标分析
统计指标  
1. 涨幅(薪水)  
	a. 例：大数据这个行业，在每一天的各个城市的涨幅。  
	b. 例：在同一个时候， 各大行业的各个城市的涨幅情况。
2. 热门(个数)：  
	a. 例：全国各大城市，最受欢迎的职位。我取的前10。  
	b. 例：大数据这个行业，在全国各个城市，热度(职业个数)。
3. 行业():  
	a. 例：全国各大城市，各个职位，薪水最高的前10个职业  
	b. 例：工作经验在1到3年全国或者同城市top10职业
