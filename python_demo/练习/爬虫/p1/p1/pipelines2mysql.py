import pymysql.cursors
import os.path
class WeatherPipeline(object):
    def process_item(self, item, spider):
        cityDate = item['cityDate'].encode('utf8')
        week = item['week'].encode('utf8')
        img = os.path.basename(item['img'])
        temperature = item['temperature'].encode('utf8')
        weather = item['weather'].encode('utf8')
        wind = item['wind'].encode('utf8')
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='scrapy',
            passwd='scrapy',
            db='test',
            charset='utf8'
        )
        cur = conn.cursor()
        cur.execute("use test;")
        cur.execute("insert into weather(cityDate,week,img,temperature,weather,wind) values(%s,%s,%s,%s,%s,%s)", (cityDate,week,img,temperature,weather,wind))
        cur.close()
        conn.commit()
        conn.close()
        return item

