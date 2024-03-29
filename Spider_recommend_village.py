from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import quote


def spider_recommend_village(KEYWORD):
    try:
        browser = webdriver.Chrome()  # 构造一个WebDriver对象
        url = 'https://m.5i5j.com/bj/xiaoquceping'
        browser.get(url)
        input_city = browser.find_element_by_class_name('sug-input')
        input_city.send_keys(KEYWORD)  # send_keys方法用于输入文字
        time.sleep(2)
        # button = browser.find_element_by_class_name('btn')
        # button.click()
        input_city.send_keys(Keys.ENTER)  # 按enter
        # 已经跳转到北京地区
        browser.close()

        browser.switch_to_window(browser.window_handles[-1])  # 切换到最后一个窗口
        url_2 = browser.current_url
        url = url_2 + quote('xiaoqu')
        browser.get(url)
        xiaoqu = browser.find_elements_by_class_name('lj-lazy')

        xiaoqu_name = []  # 储存要搜索的小区名称
        Xiaoqu_list = []

        # 获取热度高的小区的信息并以字典形式保存
        for i in xiaoqu:
            xq = {}
            browser.switch_to_window(browser.window_handles[0])

            i.click()
            browser.switch_to_window(browser.window_handles[-1])  # 切换到最后一个窗口

            # 获取各项信息
            name = browser.find_element_by_class_name('detailTitle').text
            xiaoqu_name.append(name)  # 转换为小区名的字符串

            price = browser.find_element_by_class_name('xiaoquUnitPrice')  # 获取价格
            xq[name] = price.text

            one = browser.find_elements_by_class_name('xiaoquInfoLabel')
            two = browser.find_elements_by_class_name('xiaoquInfoContent')

            for i in range(len(one)):
                xq[one[i].text] = two[i].text

            Xiaoqu_list.append(xq)
            browser.close()
        # 已经获得数据Xiaoqu_list

        # print(Xiaoqu_list)  # 测试结果是否正确

        for i in range(len(Xiaoqu_list)):
            K = Xiaoqu_list[i].keys()
            Key = list(K)
            Xiaoqu_list[i][Key[0]] = int(Xiaoqu_list[i][Key[0]])
            Xiaoqu_list[i][Key[1]] = int(Xiaoqu_list[i][Key[1]][:4])
            Xiaoqu_list[i][Key[-3]] = int(Xiaoqu_list[i][Key[-3]][:-1])
            Xiaoqu_list[i][Key[-2]] = int(Xiaoqu_list[i][Key[-2]][:-1])
        # 对Xiaoqu_list中数据处理一下



    finally:
        browser.quit()
        print(Xiaoqu_list)  # 测试结果是否正确
        return Xiaoqu_list


if __name__ == '__main__':
     spider_recommend_village('北京')
