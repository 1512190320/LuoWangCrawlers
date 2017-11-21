#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-19 10:51:40
# @Author  : Cyb (${email})
# @Link    : ${link}
# @Version : $Id$

import requests
from bs4 import BeautifulSoup


def SaveData(data):
    SavePath = 'test.txt'
    f_obj = open(SavePath, 'w')
    f_obj.close()


def SavePic(pic, name):
    SavePath = 'pic/' + name + '.jpg'
    p_obj = open(SavePath, 'wb')
    p_obj.write(pic.content)
    p_obj.close()


url = 'http://www.luoo.net/tag/?'
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0)) like Gecko'
}
value = {}
value['p'] = 1
string = ''

try:
    for x in range(1, 10):
        print(value['p'])
        # url_value = parse.urlencode(data)
        # full_url = url + url_value
        # result = request.urlopen(full_url).read()
        # result = result.decode('UTF-8')
        result = requests.get(url, params=value, headers=headers)
        soup = BeautifulSoup(result.content, 'html.parser')
        print(soup.title)
        for link in soup.find_all('a', class_="name"):
            print(link.get_text())
            string = string + link.get_text() + '\n'
            # SaveData(link.get_text())
        for picNode in soup.find_all('img', class_="cover rounded"):
            pic = requests.get(picNode.get('src'), headers=headers)
            SavePic(pic, picNode.get('alt'))
        SaveData(string)
        value['p'] += 1

except Exception as e:
    print('Error: ', e)

finally:
    pass
