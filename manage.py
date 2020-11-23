# -*- coding: utf-8 -*-

from crawl import Crawl
from settings import *

try:
    from local_settings import *
except ImportError:
    pass


def continue_load():
    reload = raw_input('已经抓取%s 条数据是否继续(Y/N):' % len(crawl.all_data))
    if str(reload) == 'Y':
        try:
            crawl.selenium_page()
        except Exception as e:
            continue_load()
    else:
        pass


if __name__ == '__main__':
    try:
        crawl = Crawl(DEFAULT_URL, DEFAULT_ID, CHROMEDRIVER_URL, XLWT_URL)
        crawl.open()
        crawl.run()
        print('抓取完成, 已经抓取%s 条数据' % len(crawl.all_data))
    except Exception as e:
        continue_load()

    title = raw_input('是否输出为表格并输入名称 ( 关闭 ctrl + c ): ')
    if len(title):
        crawl.write_xlwt(str(title))
