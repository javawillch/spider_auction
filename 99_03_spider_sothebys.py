"""
Name: Will
----------------
purpose: ingest the activity_name, activity_period and detail into a list from miacare website
pre-condition:
post-condition:
modules need to download: BeautifulSoup
"""
import requests
from bs4 import BeautifulSoup
#import bs4
import time


"""config 類別設定"""
result_list = []
detail_avtivities_url_list = []

# root_url = 'http://www.miacare.com.tw/webc/html/activity/'
activity_page_url = 'https://www.sothebys.com/en/buy/auction/2020/magnificent-jewels-5?locale=zh-Hant'

page = requests.get(activity_page_url)
soup = BeautifulSoup(page.text, "html.parser")
#step1. 找活動的相對url  class = col-md-3 col-sm-6底下的 a
         #   <div class="col-md-3 col-sm-6">
         #    <a href="show.aspx?num=105&root=1&kind=5"> #################
         #       <div class="pic">
         #           <img class="img-responsive" src="../../../app_script/DisplayCut2.ashx?file=activity/activity/640x360_(1).jpg&w=640&h=450" />
         #       </div>
         #       <p class="text-center">【線上預訂】首訂獨享 沐氧月拋1...<small> 2020.01.17 ~ 2020.03.31</small></p>
         #   </a>
print(page)
print('-------分隔線---------')

print(soup)

# parent_tags = soup.find_all("h5", class_="headline-module_headline20Regular__20lfu css-17r6vaq")

# for parent_tag in parent_tags:
#     print(parent_tag)


    # piece_url = parent_tag.find("a")['href']
    # detail_activity_url = root_url+piece_url
    # if detail_activity_url != 'http://www.miacare.com.tw/webc/html/activity/show.aspx?num=84&root=1&kind=5': 
    # #TODO_hard_code to avoid useless page    
    #     detail_avtivities_url_list.append(detail_activity_url)

#step2. ingest information from each activity detail page 
# for url in detail_avtivities_url_list:
#     time.sleep(5)
#     sub_result_list = []    #store sequence: name --> period --> detail
#     detail_page = requests.get(url)
#     soup = BeautifulSoup(detail_page.text, "html.parser")
#     parent_tag = soup.find("div", class_="content col-md-9")
#     title = parent_tag.find("h3")   #<h3>【線上預訂】首訂獨享 沐氧月拋1送1<small><span class="glyphicon glyphicon-time"></span> 2020.01.17 ~ 2020.03.31</small></h3>
#     activity_name = title.text
#     activity_period = title.small.text

#     if activity_period in activity_name:
#         activity_name = activity_name.replace(activity_period, '').strip()

    ###TODO_title is too vague, how to improve this part###
    ###沐氧月拋1送1 -->  氧高透氧矽水膠月拋1盒送1瓶睛透多效保養液360ml(每一首訂會員帳號\xa0 限預訂2組)###
    # detail = soup.find("div", class_="detail-box")
    # activity_detail = detail.text
    # sub_result_list.append(activity_name)
    # sub_result_list.append(activity_period)
    # sub_result_list.append(activity_detail)
    # result_list.append(sub_result_list)


#verify result
# for list in result_list:
#     print(list[0])
#     print(list[1])
#     print('-------分隔線---------')
"""
#   <p class="text-center">【線上預訂】首訂獨享 沐氧月拋1...<small> 2020.01.17 ~ 2020.03.31</small></p>
target_tag = soup.find("p", class_="text-center") # 尋找class = "text-center" 的P標籤
print(target_tag.text)           #--> 線上預訂】首訂獨享 沐氧月拋1... 2020.01.17 ~ 2020.03.31
print(target_tag.small.string)   #--> 2020.01.17 ~ 2020.03.31
len_of_cut = len(target_tag.small.string)
total_len = len(target_tag.text)
activity_name = target_tag.text[0:total_len-len_of_cut] 
activity_period = target_tag.small.string
print(activity_name)
print(activity_period)
"""


"""
target_tags = soup.find_all("p", class_="text-center") # 尋找所有class = "text-center" 的P標籤

for target_tag in target_tags:

    if target_tag.small != None or target_tag.small != '':
        #找要擷取的index range
        len_of_cut = len(target_tag.small.string)
        total_len = len(target_tag.text)

        activity_name = target_tag.text[0:total_len-len_of_cut] 
        activity_period = target_tag.small.string

        if activity_name == '歡迎使用美若康線上預訂服務':
            print(type(target_tag.small))
            print(target_tag.small == '')
            print('a' , target_tag.small)
        print(activity_name)
        print(activity_period)      
"""


#parsing HTML7

#insert db



# url = 'https://www.eyesmart.com.tw/search/a/?keyword=%E3%80%90%E7%9D%9B%E9%9D%9A%E3%80%91%E6%96%B0%E8%89%B2&utm_source=inweb&utm_medium=Appier&utm_campaign=2020_Q1_Bellevision_preorder'