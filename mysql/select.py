'''
第一步：安装第三方库：mysqlclient
pip install mysqlclient
第二步：导入MYSQLdb库
第三步：连接数据库服务
conn=MYSQLdb.connect(host='',user='',passwd='',db='',charset='utf8')
第四步：创建一个游标/指针
c=conn.cursor()
第五步：通过游标来执行sql（可以为查询语句也可以为插入语句）
c.execute('sql命令')

第六步：游标常用方法
fetchone()
fetchmany()
fetchall()
第七步：【通过机器对查询的结果进行校验/批量对数据库进行增删改】
conn.close()
'''
import MySQLdb
conn=MySQLdb.connect(host='https://dms.alipay.com/',
                     user='czh01084963',
                     passwd='HZC0615.',
                     db='pcpc_solution_setting',
                     charset='utf8')
c=conn.cursor()
c.execute('SELECT * FROM `pcpc_solution_setting` LIMIT 20')
row=c.fetchone()
print(row)
row=c.fetchone()     #fetchone()方法返回一个元组，游标，执行一次显示一行；再执行一次。依次打印下一行,
print(row)
rows=c.fetchmany()   #fetchmany()方法可以分组（执行返回的记录）返回记录
print(row)
allrows=c.fetchall() #fetchall()方法会返还所有记录：返回一个大元组，每条记录为一个小元组
print(allrows)

'''
使用循环查询所有记录
'''
for i in range(c.rowcount):     #游标rowcount属性：会记录游标执行的总记录
    row=c.fetchone()
    if row[1]=='str':
        print('检查点=》str找到，测试通过')
        break

'''
进行性能测试，插入1万条数据
'''
c.conn.cursor()
for x in range(10000):
    c.execute(f"INSERT INTO course(NAME,display_idx,) VALUES('测试课程{x+1}','6')")
conn.commit()   #进行提交
conn.close()    #关闭连接

