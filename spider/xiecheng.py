import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def trans_date(date_str):
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    match = date_pattern.search(date_str)
    return match.group() if match else None


def scrape_comments(start_page, end_page, output_file='comments.xlsx'):
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    all_comments = []

    url = 'https://you.ctrip.com/sight/yangzhou12/5716914.html#ctm_ref=www_hp_his_lst'
    driver.get(url)
    sleep(5)
    ele_time = driver.find_element(By.CSS_SELECTOR, '#commentModule > div.sortList > span:nth-child(2)')
    ele_time.click()
    sleep(1)

    for i in range(start_page, end_page + 1):
        print(f"正在爬取第{i}页")
        sleep(3)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        items = soup.find_all('div', class_='commentItem')

        for item in items:
            id_ = item.find('div', class_='userName').text
            rating_star = item.find('span', class_='averageScore').text.strip().split(' ')[0]
            rating = item.find('div', class_='commentDetail').text
            date = item.find('div', class_='commentTime').text
            date_1 = trans_date(date)
            ip = item.find('span', class_='ipContent').text.split('：')[1] if '：' in item.find('span',
                                                                                              class_='ipContent').text else None

            all_comments.append((id_, rating_star, rating, date_1, ip, i))

        sleep(3)
        if i < end_page:
            # 翻页操作
            wait = WebDriverWait(driver, 15)
            next_page = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#commentModule > div.myPagination > ul > li.ant-pagination-next > span')))
            next_page.click()
            sleep(3)

    driver.quit()

    # 将评论数据转换为DataFrame并保存到Excel
    df = pd.DataFrame(all_comments, columns=['用户名', '星级', '评论内容', '日期', 'IP', '页码'])
    df.to_excel(output_file, index=False)
    print(f"数据已保存到{output_file}")
    return df


# 设置起始页和结束页
start_page = 1
end_page = 1

# 调用函数并保存数据
