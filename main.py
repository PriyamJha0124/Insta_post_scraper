import instaloader
import csv
import re
import datetime
from pprint import pprint
import os
import time
import random
import datetime

proxies = [

    "http://isjrotjv-1:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-2:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-3:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-4:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-5:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-6:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-7:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-8:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-9:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-10:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-11:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-12:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-13:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-14:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-15:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-16:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-17:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-18:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-19:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-20:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-21:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-22:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-23:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-24:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-25:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-26:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-27:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-28:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-29:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-30:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-31:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-32:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-33:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-34:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-35:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-36:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-37:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-38:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-39:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-40:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-41:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-42:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-43:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-44:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-45:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-46:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-47:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-48:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-49:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-50:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-51:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-52:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-53:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-54:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-55:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-56:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-57:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-58:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-59:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-60:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-61:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-62:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-63:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-64:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-65:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-66:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-67:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-68:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-69:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-70:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-71:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-72:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-73:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-74:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-75:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-76:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-77:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-78:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-79:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-80:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-81:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-82:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-83:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-84:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-85:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-86:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-87:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-88:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-89:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-90:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-91:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-92:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-93:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-94:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-95:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-96:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-97:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-98:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-99:n715rfvdsrwf@p.webshare.io:80", 
    "http://isjrotjv-100:n715rfvdsrwf@p.webshare.io:80", 

]


# -*- coding: utf-8 -*-
ph_re = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'


def write_in_csv(data):
    global page_name
    print(data)

    fieldnames = ['Origin', 'Name', 'User Name', 'Followers', 'User_name_url',
                  'Biography', 'link_in_bio', 'phone', 'email', 'post_url', 'date_of_Post', 'Post_likes']
    with open('tempDir/' + page_name + '.csv', 'a', newline='', encoding='utf-8') as f:
        wr = csv.DictWriter(f, fieldnames=fieldnames)
        wr.writerow(data)


# if not os.path.exists('tempDir'):
#     os.mkdir('tempDir')
proxy = random.choice(proxies)
print(proxy)
os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
time.sleep(0.50)
page_name = input('Page_name:-')
# page_name = "Rapeton"


L = instaloader.Instaloader()
sunames = []
currentDT = 0
posts = instaloader.Profile.from_username(L.context, page_name).get_posts()
# SINCE = datetime(2019, 3, 1)
# UNTIL = datetime(2020, 10, 1)
# for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
current_year = 2019
current_month = 12
for post in posts:
    # here ip changing code=======================================
    oldDT = currentDT
    currentDT = (datetime.datetime.now().hour * 60) + datetime.datetime.now().minute
    print(currentDT)
    diff = currentDT - oldDT
    if (diff >= 5):
        proxy = random.choice(proxies)
        print(proxy)
        print(diff)
        os.environ['http_proxy'] = proxy
        os.environ['HTTP_PROXY'] = proxy
        os.environ['https_proxy'] = proxy
        os.environ['HTTPS_PROXY'] = proxy
    # os.rename('guru99.txt','career.guru99.txt') 
    print("ths is post==============>start", post.date)
    mentions = post.caption_mentions
    post_date = post.date
    year = post_date.strftime("%Y")
    month = post_date.strftime("%m")
    difference =int(year)*12 + int(month) - current_year*12 - 3
    print("ths is post========cl======>end", year, month)
    if difference >= 0:
        post_url = post.url
        post_link = post.shortcode
        post_likes = post.likes
        post_comments = post.comments
        L.filename_pattern = str(post_likes) + "__" + str(post_comments)
        L.download_video_thumbnails = "--no-video-thumbnails"
        L.download_geotags = False
        L.download_comments = False
        L.save_metadata = False
        # L.post_metadata_txt_pattern = False
        L.compress_json = False
        L.download_post(post, page_name)
        

    