import pymysql
import datetime

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Wyj19735.',
    db='ToolsBase',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)


def write_in_datebase(title, text, if_share, contact_way):
    curse = connection.cursor()
    sql = "insert into cyber(title,text,ifshare,contact_way,submit_time) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" \
          % (title, text, if_share, contact_way, datetime.datetime.now())
    connection.ping(reconnect=True)
    try:
        curse.execute(sql)
    except:
        print("数据库写入异常")
    connection.commit()
    connection.close()
