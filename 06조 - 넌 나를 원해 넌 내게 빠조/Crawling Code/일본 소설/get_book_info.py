
import requests # 웹 페이지 가져오는 라이브러리
from bs4 import BeautifulSoup # 웹 페이지 분석(크롤링)하는 라이브러리

base_url = "https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=2&page="
plus_url = "&Stockstatus=1&PublishDay=84&CID=50918&SearchOption="

base_img_url = "//image.aladin.co.kr/img/common/star_s"
plus_img_url = ".git"

img_score = 'null'
review_cnt = 'null'
book_info = []
for i in range(1,114): #484하면됨
    print(i, " 번째 페이지")
    url = base_url + str(i) + plus_url
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    uls = soup.select('#Myform > div:nth-child(2) > div  div.ss_book_list:nth-child(1) > ul')
    # print(uls)
    for ul in uls:
        # print(len(ul.find_all('li')), "개 에서 ") # 총 개수 
        for idx, li in enumerate(ul.find_all('li')):
            if li.select_one('a.bo3'):
                title_cnt = idx
                # print(title_cnt + 1, "번 째")
        cnt = 1 # len(ul.find_all('li')) - title_cnt
        book_append_dict = {}
        for idx, li in enumerate(ul.find_all('li')):
            if idx >= title_cnt:
                if cnt == 1:
                    title = li.select_one('a.bo3')
                elif cnt == 2:
                    pub_and_year = li
                elif cnt == 3:
                    price = li.select_one('span.ss_p2 > b > span')
                elif cnt == 4:
                    review = ul.select_one('img > a')
                    if(review == None):
                        # print('null')
                        review_cnt = 'null'
                    else:
                        review_cnt = review.get_text()
                    img = li.select_one('img')
                    if(img == None):
                        img_f = "null"
                    else:
                        img_src = img.find('img')
                        img_f = img.get('src')
                    if(img_f == '//image.aladin.co.kr/img/common/star_s10.gif'):
                        img_score = 5
                    elif(img_f == '//image.aladin.co.kr/img/common/star_s9.gif'):
                        img_score = 4.5
                    elif(img_f == '//image.aladin.co.kr/img/common/star_s8.gif'):
                        img_score = 4
                    elif(img_f == '//image.aladin.co.kr/img/common/star_s7.gif'):
                        img_score = 3.5
                    elif(img_f == '//image.aladin.co.kr/img/common/star_s6.gif'):
                        img_score = 3
                    elif(img_f == '//image.aladin.co.kr/img/common/star_s5.gif'):
                        img_score = 2.5
                    elif(img_f == '//image.aladin.co.kr/img/common/star_s4.gif'):
                        img_score = 2
                    elif(img_f == '//image.aladin.co.kr/img/common/star_s3.gif'):
                        img_score = 1.5
                    elif(img_f == '//image.aladin.co.kr/img/common/star_s2.gif'):
                        img_score = 1
                    elif(img_f == '//image.aladin.co.kr/img/common/star_s1.gif'):
                        img_score = 0.5
                    elif(img_f == '//image.aladin.co.kr/img/common/star_s0.gif'):
                        img_score = 0
                    elif(img_f == 'null'):
                        img_score = 'null'

                cnt += 1
                if cnt == 5:
                    break

            else:
                continue


##################
        # if len(ul.find_all('li')) == 5:
        #     # print("@@@@@ 5개짜리 @@@@@")
        #     title = ul.select_one('a.bo3')
        #     author = ul.select_one('ul > li:nth-child(3) > a')
        #     publisher = ul.select_one('ul > li:nth-child(3)> a:nth-child(2)')
        #     price = ul.select_one('ul > li:nth-child(4) > span.ss_p2 > b > span')
        #     review = ul.select_one('ul > li:nth-child(5) > img > a')
        #     pub_year = ul.select_one('ul > li:nth-child(3)')

        # else:
        #     # print("@@@@@ 4개짜리 @@@@@")
        #     title = ul.select_one('a.bo3')
        #     author = ul.select_one('ul > li:nth-child(2) > a')
        #     publisher = ul.select_one('ul > li:nth-child(2) > a:nth-child(2)')
        #     price = ul.select_one('ul > li:nth-child(3)> span.ss_p2 > b > span')
        #     review = ul.select_one('ul > li:nth-child(4) > img > a')
        #     pub_year = ul.select_one('ul > li:nth-child(2)')
        
        
        # img = ul.select_one('ul > li:nth-child(5) > img')
        # if(img == None):
        #     img = ul.select_one('ul > li:nth-child(4) > img')
        #     if(img == None):
        #         img_f = "null"
        #     else:
        #         img_src = img.find('img')
        #         img_f = img.get('src')
        # else:
        #     img_src = img.find('img')
        #     img_f = img.get('src')

            
        # if(img_f == '//image.aladin.co.kr/img/common/star_s10.gif'):
        #     img_score = 5
        # elif(img_f == '//image.aladin.co.kr/img/common/star_s9.gif'):
        #     img_score = 4.5
        # elif(img_f == '//image.aladin.co.kr/img/common/star_s8.gif'):
        #     img_score = 4
        # elif(img_f == '//image.aladin.co.kr/img/common/star_s7.gif'):
        #     img_score = 3.5
        # elif(img_f == '//image.aladin.co.kr/img/common/star_s6.gif'):
        #     img_score = 3
        # elif(img_f == '//image.aladin.co.kr/img/common/star_s5.gif'):
        #     img_score = 2.5
        # elif(img_f == '//image.aladin.co.kr/img/common/star_s4.gif'):
        #     img_score = 2
        # elif(img_f == '//image.aladin.co.kr/img/common/star_s3.gif'):
        #     img_score = 1.5
        # elif(img_f == '//image.aladin.co.kr/img/common/star_s2.gif'):
        #     img_score = 1
        # elif(img_f == '//image.aladin.co.kr/img/common/star_s1.gif'):
        #     img_score = 0.5
        # elif(img_f == '//image.aladin.co.kr/img/common/star_s0.gif'):
        #     img_score = 0
        # elif(img_f == 'null'):
        #     img_score = 'null'

            
                
            

        # print(title.get_text())
        # print(author.get_text())
        # print(publisher.get_text())
        # print(price.get_text())
        
        # print(img_score)
        # print(pub_year.get_text().split('|'))
        
        # print('\n')
        print(title.get_text(), "책 삽입")
        book_info.append({
            "title" : title.get_text(),
            "book_id" : title['href'].split('=')[-1],
            "author" : pub_and_year.get_text().split('|')[0],
            "publisher" : pub_and_year.get_text().split('|')[1],
            "price" : price.get_text(),
            "review_cnt" : review_cnt if review_cnt else 'null',
            "review_score" : img_score if img_score else 'null',
            "pub_year" : pub_and_year.get_text().split('|')[-1]
        })
        img_score = 'null'
        review_cnt = 'null'

print(len(book_info))

import json
with open('./japan_fiction_data.json','w',encoding='UTF-8') as f:
    json.dump(book_info, f, ensure_ascii=False, indent=4)