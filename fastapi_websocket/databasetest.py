import pymysql

param = {
    "host": "cdb-g76irqy0.cd.tencentcdb.com",
    "port": 10186,
    "db": "mysql",
    "user": "root",
    "password": "red-fox-yj2020",
    "charset": "utf8",
}
conn = pymysql.connect(**param)  # 连接对象
cur = conn.cursor()  # 游标对象，采用默认的数据格式

cur.execute("SELECT * FROM user")  # 执行sql语句，返回受影响的行数
print(cur.fetchall())  # 获取查询结果

# # %s:占位符
# # params：增加内容的列表或元组,多条语句可以使用嵌套
# sql = "insert into test values(%s,%s)"
# params = (1221, "小强")
# cur.execute(sql, params)  # sql语句参数化，防止攻击！

# # pymysql连接数据库默认开启事物，提交之前的操作，使生效！
# conn.commit()

# 要及时关闭连接！
cur.close()  # 关闭游标
conn.close()  # 关闭连接
