# https://blog.csdn.net/WinWill2012/article/details/72512301
# http://chart.cp.360.cn/kaijiang/kaijiang?lotId=166406&spanType=2&span=2018-04-04_2018-04-04

from bs4 import BeautifulSoup
import urllib.request
import datetime
import os

class GetElevenSelectFiveNumber(object):
    """获取5个号码"""
    def __init__(self, date):
        self.date = date
        self.getUrl(self.date)   

    def getUrl(self,date):
        url = r'http://chart.cp.360.cn/kaijiang/kaijiang?lotId=166406&spanType=2&span=%s_%s' %(date,date)
        htmlContent = self.getRespenseContent(url)
        try:
            soup = BeautifulSoup(htmlContent,'lxml')   #出错
            table = soup.find('table')
            rows = table.find_all('tr')
            file = open("result/" + date, "w")
            for row in rows[1:-2]:
                if row.find('td',{"class":"gray"}) is not None:
                    order = row.find('td',{"class":"gray"}).get_text()
                    left_number = row.find('em',{"class":"orange"}).get_text()
                    right_number = row.find('em',{"class":"blue"}).get_text()
                    number = "%s %s" %(left_number,right_number)
                    file.write("%s_%s ==> %s\n" % (date,order,number))
            file.close()
        except AttributeError:
            print("Get lottery of %s failed!！！" %date)


    def getRespenseContent(self, url):
        try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
            response = urllib.request.urlopen(req)
        except:
            print("Get content of %s failed!-----" % url) 
        else:
            return response.read()

def get_all_date(begin,end):
    """ 获取日期 """
    all_date = []
    begin_date = datetime.datetime.strptime(begin,"%Y-%m-%d")
    end_date = datetime.datetime.strptime(end,"%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        all_date.append(date_str)
        begin_date = begin_date + datetime.timedelta(days=1)
    return all_date

if __name__ == '__main__':
    all_date = get_all_date("2018-04-03","2018-04-04")
    if not os .path.exists("result"):
        os.mkdir("result")
    for date in all_date:
        GetElevenSelectFiveNumber(date)  #出错





        