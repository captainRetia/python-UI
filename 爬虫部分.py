import re
import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
def introduction(item):
    try:
        #quote可将中文转换成URL编码格式
        url='https://baike.baidu.com/item/'+quote(item)
        #对目标url进行请求，读取页面
        content=urllib.request.urlopen(url)
        con=content.read()
        #返回值为bytes类型，需要用decode()解码
        c=con.decode('utf-8')
        #创建BeautifulSoup对象，为一个树形结构，包含HTML页面中的每一个标签元素，使用lxml解析库的原因是因为速度快
        soup=BeautifulSoup(c, "lxml")
        #按F12查看网页源代码，找到自己需要的标签位置
        text=soup.find('div', class_="lemma-summary")
        #利用正则表达式re函数库进行处理
        t=''
        for x in text:
            w1=re.compile(r"<(.+?)>")
            word=re.sub(w1,'',str(x))
            w2=re.compile(r"\[(.+?)\]")
            words=re.sub(w2,'',word)
            t+=words
        return t
    #进行异常处理
    except (AttributeError,TypeError):
        return "输入有歧义或不够详细，请再次输入"
if __name__=="__main__":
    searchitem=input("请输入查询内容")
    var=introduction(searchitem)
    print(var)