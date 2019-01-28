import urllib.request
import json
from bs4 import BeautifulSoup
from lxml import etree

global url_servant
global url
global headers

url_servant = "https://fgo.umowang.com/servant/"
url = "https://fgo.umowang.com/servant/ajax?card=&wd=&ids=&sort=12777&o=desc&pn="

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-language': "zh-CN,zh;q=0.9",
    'cache-control': "max-age=0",
    'referer': "https://fgo.umowang.com/",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
def getServantID():
    url_servant_ID = []
    count = 1

    while (count <= 15):
        url_temp = url + str(count)
        request = urllib.request.Request(url=url_temp, headers=headers)
        res = urllib.request.urlopen(request)
        page_source = res.read().decode()
        servant_dict = json.loads(page_source)
        id_length = len(servant_dict['data'])
        id_count = 0
        while (id_count < id_length):
            #print(servant_dict['data'][id_count]['id'])
            url_servant_ID.append(servant_dict['data'][id_count]['id'])
            id_count = id_count + 1
        #print(type(json.loads(page_source)))
        count = count + 1
        del servant_dict
        del id_count
        del id_length

        return url_servant_ID

def getSpecialAttack(url_servant_ID):
    for u in url_servant_ID:
        request1 = urllib.request.Request(url=url_servant + u, headers=headers)
        res1 = urllib.request.urlopen(request1)
        page_source1 = res1.read().decode()
    # soup = BeautifulSoup(page_source1, 'html.parser')
    #
    #
    # print(type(soup.find_all("td")))
    #
    # print(soup.find_all("td")[552].text)


        html = etree.HTML(page_source1)
        html_data1 = html.xpath('/html/body//h4/span[2]')
        html_data = html.xpath('/html/body/div/div/div/div/div[@class="uk-width-large-1-12 uk-hidden-small uk-padding-remove"]/table/tr[6]/td[2]')
        for i in html_data1:
            print(i.text,end="         ")
        for i in html_data:
            print(i.text)

getSpecialAttack(getServantID())
#print(res.read().decode())
#print(res.read())
#driver = webdriver.

#soup = BeautifulSoup(page_source, "html.parser")
#print(soup.a)
#t = [1,2,3]
# print(t)
#print(soup.find_all("a",class_="uk-thumbnail"))

# for item in soup.find_all("a",class_="uk-thumbnail"):
#     print(item.get("href"))


