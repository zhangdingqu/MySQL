from pymysql import *

def main():
    #创建connection连接  连接对象
    conn = connect(host = "localhost", port = 3306, user = 'root', password = 'qwe123123', database = 'jingdong', charset = 'utf8')

    #获取Cursor对象  游标对象
    cs1 = conn.cursor()
    count = cs1.execute('select id, name from goods where id > 4')
    print("打印受影响的行数：", count)

    for i in range(count):
        #获取查询的结果
        result = cs1.fetchone() #返回一个元组  fetchmany()和fetchall()返回的结果是元组套元组
        print(result)

    cs1.close()
    conn.close()

if __name__ == '__main__':
    main()

#插入时间

# 格式符 说明
# %a  星期的英文单词的缩写：如星期一， 则返回 Mon
# %A  星期的英文单词的全拼：如星期一，返回 Monday
# %b  月份的英文单词的缩写：如一月， 则返回 Jan
# %B  月份的引文单词的缩写：如一月， 则返回 January
# %c  返回datetime的字符串表示，如03/08/15 23:01:26
# %d  返回的是当前时间是当前月的第几天
# %f  微秒的表示： 范围: [0,999999]
# %H  以24小时制表示当前小时
# %I  以12小时制表示当前小时
# %j  返回 当天是当年的第几天 范围[001,366]
# %m  返回月份 范围[0,12]
# %M  返回分钟数 范围 [0,59]
# %P  返回是上午还是下午–AM or PM
# %S  返回秒数 范围 [0,61]。。。手册说明的
# %U  返回当周是当年的第几周 以周日为第一天
# %W  返回当周是当年的第几周 以周一为第一天
# %w  当天在当周的天数，范围为[0, 6]，6表示星期天
# %x  日期的字符串表示 ：03/08/15
# %X  时间的字符串表示 ：23:22:08
# %y  两个数字表示的年份 15
# %Y  四个数字表示的年份 2015
# %z  与utc时间的间隔 （如果是本地时间，返回空字符串）
# %Z  时区名称（如果是本地时间，返回空字符串）

from datetime import datetime
dt = datetime.now()
today_time=dt.strftime('%Y-%m-%d %H:%M:%S')

self.mysql.cur.execute('update item set `时间`="%s"'%today_time)