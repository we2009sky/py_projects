# encoding=utf8
import re
from urllib import request
import threading

class Download(object):
    url_page = []
    url_list = []
    def __index__(self):
        pass

    def get_url(self):
        """Define page url"""
        root_url = 'https://www.dota2.com.cn/enjoy/gamewall/'
        for i in range(5):
            self.url_page.append(root_url + 'index{}.htm'.format(i))

    def get_page_url(self):
        """Get every page url"""
        for page in self.url_page:
            res = request.urlopen(page).read()


