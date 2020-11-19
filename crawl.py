# -*- coding: utf-8 -*-


from time import sleep

from selenium import webdriver


class Crawl(object):
    def __init__(self, url, id, chromedriver, xlwt_url):
        self.all_data = []
        self.url = url
        self.id = id
        self.page = 0  # 计算大约页数
        self.driver = None
        self.chromedriver = chromedriver
        self.xlwt_url = xlwt_url
        self.waterfall_time = 0.5  # 瀑布流延迟时间
        self.page_time = 3  # 翻页流延迟时间
        self.option = {
            'empty': 'WB_empty',  # 瀑布流对应样式
            'text': 'WB_text',  # 正文对应样式
            'page': 'page',  # 翻页对应样式
            'info': 'WB_info',  # 翻页对应样式
            # 'face': 'W_face_radius',  # 博主头像 # 不确定dom 暂时不存
            'form': 'WB_from'  # 时间以及状态
        }

    def open(self):
        self.driver = webdriver.Chrome(self.chromedriver)

    def get(self):
        self.driver.get(self.url % self.id)
        login = raw_input('手动登入,登入成功后输入y:')
        if str(login) == 'y':
            return True

    def click_waterfall(self):
        now = self.driver.find_elements_by_class_name(self.option['empty'])
        # 瀑布流加载失败异常
        try:
            now[len(now) - 1].click()
            sleep(self.waterfall_time)
        except Exception as e:
            print(e)
        self.selenium_page()

    def sync_data(self):

        text = self.driver.find_elements_by_class_name(self.option['text'])
        info = self.driver.find_elements_by_class_name(self.option['info'])
        # face = self.driver.find_elements_by_class_name(self.option['face'])
        form = self.driver.find_elements_by_class_name(self.option['form'])
        print(len(text), len(info), len(form))
        for index, i in enumerate(text):
            self.all_data.append({
                'text': i.text,
                'info': info[index].text,
                'form': form[index].text,
                'page': self.page + 1
            })
            # write_xlwt(index, i.text)
        self.next_page()

    def next_page(self):
        print(self.option['page'])
        page = self.driver.find_elements_by_class_name(self.option['page'])
        for i in page:
            if i.text == u'\u4e0b\u4e00\u9875':
                print('---- 当前第%s页 ----' % self.page)
                print('---- 开始下一页 ----')
                self.page += 1
                i.click()
                sleep(self.page_time)
                self.selenium_page()

    def selenium_page(self):
        page = self.driver.find_elements_by_class_name(self.option['page'])
        if not len(page):
            self.click_waterfall()
        else:
            self.sync_data()

    def run(self):
        if self.get():
            self.selenium_page()

    def write_xlwt(self, sheet='测试表格'):
        import xlwt
        workbook = xlwt.Workbook(encoding='utf-8')  # 新建工作簿
        sheet = workbook.add_sheet(sheet)  # 新建sheet
        for index, i in enumerate(self.all_data):
            sheet.write(index, 0, i['text'])  # 正文
            sheet.write(index, 1, i['info'])  # 用户名
            sheet.write(index, 2, i['form'])  # 时间以状态
            sheet.write(index, 3, i['page'])  # 大致页面

        out_url = self.xlwt_url % sheet
        workbook.save(r'%s' % out_url)  # 保存
