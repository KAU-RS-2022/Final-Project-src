from gettext import find
import json

from requests import delete


# data file 합치기 / 이후에 users_data file도 합치자(얘는 중복제거해야함 )
with open('data_1.json','r', encoding="UTF-8") as f:
    data_1 = json.load(f)
print(len(data_1))


with open('data_2.json','r', encoding="UTF-8") as f:
    data_2 = json.load(f)
print(len(data_2))

with open('data_3.json','r', encoding="UTF-8") as f:
    data_3 = json.load(f)
print(len(data_3))

with open('data_4.json','r', encoding="UTF-8") as f:
    data_4 = json.load(f)
print(len(data_4))

with open('data_5.json','r', encoding="UTF-8") as f:
    data_5 = json.load(f)
print(len(data_5))

all_data = data_1 + data_2 + data_3 + data_4 + data_5

print(len(all_data))

with open('./all_data.json','w',encoding='UTF-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)

# with open('test_data.json','r', encoding="UTF-8") as f:
#     test_data = json.load(f)
# all_data = test_data

all_review_list = [] # 중복 제거 전 모든 리뷰 데이터를 담은 리스트 
for book in all_data:
    reviews = book["user_and_review_info"] # 한 책에 대한 모든 리뷰 를 담은 리스트
    if reviews == "연령제한 책":
        continue
    for review in reviews:
        user_id = review["user_blog_url"].split("/")[-1]
        all_review_list.append({"user_id" : user_id, "user_name" : review["user_name"], "user_blog_url" : review["user_blog_url"]})
print(len(all_review_list)) # 중복 제거 전

with open('./all_review_data.json','w',encoding='UTF-8') as f:
        json.dump(all_review_list, f, ensure_ascii=False, indent=4)

import collections

all_review_list = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.items())) for d in all_review_list)))
print(len(all_review_list)) # 중복 제거 후


with open('./all_review_data_no_duplication.json','w',encoding='UTF-8') as f:
        json.dump(all_review_list, f, ensure_ascii=False, indent=4)



#일단 data_1 에 있는 모든 5000개의 책에대한 각각의 리뷰들을 이렇게 합치고... 
# a_list = [
#             {
#                 "user_id" : "712139133",
#                 "user_name" : "후애",
#                 "user_blog_url" : "https://blog.aladin.co.kr/712139133"
#             },
#             {
#                 "user_id" : "naiad326",
#                 "user_name" : "꼬마요정",
#                 "user_blog_url" : "https://blog.aladin.co.kr/naiad326"
#             },
#             {
#                 "user_id" : "712139133",
#                 "user_name" : "후애",
#                 "user_blog_url" : "https://blog.aladin.co.kr/712139133"
#             },
#             {
#                 "user_id" : "731938109",
#                 "user_name" : "파이버",
#                 "user_blog_url" : "https://blog.aladin.co.kr/731938109"
#             },
#             {
#                 "user_id" : "731938109",
#                 "user_name" : "파이버",
#                 "user_blog_url" : "https://blog.aladin.co.kr/731938109"
#             }
#         ]
# print(a_list)
# a_list 에서 user_id 가 중복되는 애들을 한개만 남기고 제거 


# import collections
# deleted_list = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.items())) for d in a_list)))
# print(deleted_list)
# 출처: https://sanghaklee.tistory.com/60 [이상학의 개발블로그]






##################################################################

# https://velog.io/@panache/python-find-or-remove-duplicated-value
# 중복 되는 원소 찾기 + 해당 중복되는 원소의 count 세기 

# with open('users_data_test.json','r', encoding="UTF-8") as f:
#     data = json.load(f)
# print(len(data))

# find_list = []

# for user in data:
#     find_list.append(user["user_id"])

# # print(find_list)

# from collections import Counter

# tmp_list = ['744743170', 'love4u', '788794163', '775285294', 'love4u', '739955181', '748122196', '782655164', '708483233', '706591196', '729729196', '707795116', '749986274', '795562129', '779029169', '745178171', '770666189', '705270138']

# result = Counter(tmp_list)
# for key, value in result.items():
#     if value >= 2:
#         print(key)