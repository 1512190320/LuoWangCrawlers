#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-19 10:51:40
# @Author  : Cyb (${email})
# @Link    : ${link}
# @Version : $Id$

import requests
from bs4 import BeautifulSoup


class LuoWangCrawlers(object):

    def __init__(self, url, value, headers):
        self.url = url
        self.value = value
        self.headers = headers

    def SaveData(self, Data, SavePath):
        f_obj = open(SavePath, 'wb')
        f_obj.write(Data)
        f_obj.close

    def GetRequest(self, Beg, End):
        string = ''
        try:
            for x in range(Beg, End):
                print(self.value['p'])
                result = requests.get(
                    self.url, params=self.value, headers=self.headers)
                soup = BeautifulSoup(result.content, 'html.parser')
                if soup.find_all('div', class_='error-msg'):
                    raise Exception('404 Error')
                for link in soup.find_all('a', class_="name"):
                    print(link.get_text())
                    string = string + link.get_text() + '\n'
                    # SaveData(link.get_text())
                for picNode in soup.find_all('img', class_="cover rounded"):
                    pic = requests.get(picNode.get(
                        'src'), headers=self.headers)
                    # SavePic(pic, picNode.get('alt'))
                    self.SaveData(pic.content, 'pic/' +
                                  picNode.get('alt') + '.jpg')
                self.value['p'] += 1

        except Exception as e:
            print('Error: ', e)

        finally:
            pass


URL = 'http://www.luoo.net/tag/?'
HEADERS = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0)) like Gecko'
}
VALUE = {}
VALUE['p'] = 1

spider = LuoWangCrawlers(URL, VALUE, HEADERS)
spider.GetRequest(1, 4)
