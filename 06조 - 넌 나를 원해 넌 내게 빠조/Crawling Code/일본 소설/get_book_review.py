# 셀레니움 import
# ---------------------------------------
# -*- coding: utf-8 -*-

from select import select
from selenium import webdriver
import time
import requests 
from bs4 import BeautifulSoup
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


import datetime
    
def doScrollDown(whileSeconds):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=whileSeconds)
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)
        if datetime.datetime.now() > end:
            break

# selenium driver 옵션
# ---------------------------------------
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
agent="User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131"
options.add_argument(agent)
options.add_argument("lang=ko_KR")
options.add_experimental_option("excludeSwitches", ["enable-logging"])


# 드라이버 생성
# ---------------------------------------
chromedriver = "C://Users//wxx7829//Documents//(대학)4학년1학기//(수업)//추천시스템//팀프로젝트//chromedriver.exe"

optionss = webdriver.ChromeOptions()
optionss.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(chromedriver, chrome_options=options)
# driver = webdriver.Chrome(chromedriver, options=optionss)




result = []
def get_info(book_title, url):
    

    driver.get(url)
    # time.sleep(1)
    driver.implicitly_wait(10)
    
    try:
        html = driver.page_source
    except:
        return None

    # 페이지 쭈우우우욱 내리기
    scroll_location = driver.execute_script("return document.body.scrollHeight")
    while True:

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        scroll_height = driver.execute_script("return document.body.scrollHeight")

        if scroll_location == scroll_height:
            break
        else:
            scroll_location = scroll_height

    
    # doScrollDown(10)
    print("정상 스크롤 끝")
    # driver.execute_script('window.scrollTo(0,0)')
    # print("스크롤 업")
    # time.sleep(3)
    # print("스크롤 내림")

    # total_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#tabTotal")))
    try:
        # total_button = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tabTotal")))
        total_button = driver.find_element_by_css_selector("#tabTotal")
        driver.execute_script("arguments[0].click();", total_button) 
        time.sleep(0.5)
    # print("전체 탭 클릭")
    except:
        current_px = 0
        while True:
            scrollY = driver.execute_script("return window.scrollY")
            driver.execute_script("window.scrollTo( %s, %s);" % (current_px, current_px+1))
            current_px+=20
            
            if scrollY == driver.execute_script("return window.scrollY"):
                break
        print("tab 오류 난 애 스크롤 끝")
        # total_button = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tabTotal")))
        total_button = driver.find_element_by_css_selector("#tabTotal")
        driver.execute_script("arguments[0].click();", total_button) 
        time.sleep(0.5)
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@" + book_title + "은 전체 탭 오류입니다 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # append_dict = {} # 책 하나 에 해당하는 리뷰 및 유저 정보
        # append_dict["book_title"] = book_title
        # append_dict["user_and_review_info"] = "전체 탭 오류 책"
        # return append_dict
    # 사실 필요 없음... 
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # print(soup)

    append_dict = {} # 책 하나 에 해당하는 리뷰 및 유저 정보
    append_dict["book_title"] = book_title
    append_dict["user_and_review_info"] = []

    # 100 자평 리뷰 더보기 클릭 계속해서 없어질때 까지 클릭
    while(True):
        try:
            add_more_button = driver.find_element_by_css_selector("#divReviewPageMore > div.Ere_btn_more > a")
            driver.execute_script("arguments[0].click();", add_more_button)  #자바 명령어 실행
            time.sleep(0.7)
            # print("더보기 클릭")
            # print(driver.find_element_by_css_selector("#divReviewPageMore").get_attribute("style"))
            if driver.find_element_by_css_selector("#divReviewPageMore").get_attribute("style") == "display: none;":
                # print("display가 none 이므로 더보기 버튼 끝~~~~~")
                break
        except:
            break
        
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')


    # 100자평 더보기 다 클릭 되었으면 ul_list 셀렉터 이용해서 find
    div_tags = soup.select("#CommentReviewList > div.review_list_wrap > ul > div > div.HL_star")
    
    ul_tags = soup.select("#CommentReviewList > div.review_list_wrap > ul > div > div.HL_write > div > ul") # 블로그 url 및 리뷰 텍스트 담긴 태그들의 리스트
    if ul_tags == []:
        print(book_title + "은 100자평 리뷰가 없습니다.")

    for ul_tag, div_tag in zip(ul_tags, div_tags):
        loop_dict = {}

        # print(div_tag.select("img")) # list 출력
        count = 0
        for i in div_tag.select("img"):
            if i['src'] == "//image.aladin.co.kr/img/shop/2018/icon_star_on.png":
                count += 1
            else:
                continue
        user_stars_num = count

        user_blog_url = ul_tag.select_one("ul > li:nth-child(2) > div.left > a.Ere_sub_gray8.Ere_fs13.Ere_PR10")['href']
        user_review = ul_tag.select_one("ul > li:nth-child(1) > div > div > a").text.translate(str.maketrans('', '', '\n\t\r\xa0'))
        user_name = ul_tag.select_one("ul > li:nth-child(2) > div.left > a.Ere_sub_gray8.Ere_fs13.Ere_PR10").text
        loop_dict["user_star"] = count
        loop_dict["user_name"] = user_name
        loop_dict["user_blog_url"] = user_blog_url
        loop_dict["user_review"] = user_review
        append_dict["user_and_review_info"].append(loop_dict)
        # print(user_name + "의 리뷰를 넣었다.")
    return append_dict    




if __name__ == '__main__':

    with open('./japan_fiction_title_url_list.json','r', encoding="UTF-8") as f:
        json_data = json.load(f)
    print(len(json_data))
    # for title, url in json_data[0].items():
    #     print(title, url)
    # title, url = list(json_data[0].items())[0]
    # print(title, url)


    # append_dict = get_info("tabTotal 오류나는 책", "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=105651245")
    # result.append(append_dict)
    
    for idx, url in enumerate(json_data[0:1000]): # 0 : 5639 하면 됨
        title, url = list(url.items())[0]
        print(idx, title, url)
        append_dict = get_info(title, url)
        if(append_dict == None): # 19세 짤 
            result.append({"book_title" : title, "user_and_review_info" : "연령제한 책"})
            continue # 19 세 책은 그냥 안넣겠다.. 

        result.append(append_dict)





    with open('./data_1.json','w',encoding='UTF-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
