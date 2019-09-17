'''
  创建数据库 dict
  创建数据表 words
  id word mean
'''

import pymysql

#连接数据库
db = pymysql.connect(host='localhost',port = 3306,user='root',password='123456',
                     database='stu',charset='utf8')

#获取游标(操作数据库,执行sql语句,得到执行结果)
cur = db.cursor()

#执行语句
sql = "insert into words (word,mean) values (%s,%d,%d)"

for line in f:
    tmp = line.split(' ',1)
    word = tmp[0]
    mean = tmp[1].strip()
    cur.execute(sql,[word,mean])

#提交到数据库
db.commit()

#关闭游标
cur.close()

#关闭数据库
db.close()