# encoding=utf8
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup
import re

URLS = ['https://www.ivsky.com/tupian/mote_t1494/index_{}.html'.format(index) for index in range(1, 100)]
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59"
}


def get_html(url):
    r = requests.get(url, headers=header)
    return r.text


def parse_html(html):
    srcs = []
    names = []
    soup = BeautifulSoup(markup=html, features='html.parser')
    result = soup.find_all('div', class_='il_img')
    for row in result:
        src = row.find('img').get('src')
        name = row.find('a').get('href').split('/')[-1].split('.')[0]
        srcs.append(src)
        names.append(name)
    return zip(srcs, names)


def save_image(image):
    image_url, image_name = 'https:' + image[0], image[1]
    r = requests.get(image_url, headers=header)
    with open('images/' + image_name+'.jpg', 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    start = time.time()
    image_urls = []
    image_names = []
    with ThreadPoolExecutor() as pool:
        html_resutls = pool.map(get_html, URLS)
        parser_results = pool.map(parse_html, html_resutls)
        for row in parser_results:
            for result in row:
                image_urls.append(result[0])
                image_names.append(result[1])

        image_infos = zip(image_urls, image_names)
        pool.map(save_image, image_infos)
    print('end cost', time.time() - start)
