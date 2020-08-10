#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import argparse
import time

parser = argparse.ArgumentParser() #描述程序
parser.add_argument('website',help="welcome,Directory scan",type=str) #獲取用戶輸入地址
args = parser.parse_args()

if "http://" not in args.website:
    url = "http://"+args.website
else:
    url = args.website
website = url
webdic = 'C:\Users\Noth\Desktop\MDB.txt'

header = {
    'Accept': '*/*', 
    'Referer': website, #這是經過處理後的網址
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',#設置掃描器的瀏覽器標識UA
    'Connection': 'Keep-Alive',
    'Cache-Control': 'no-cache',
}

webdict = [] #創建一個新的字典用於存放拼接後的網址
with open(webdic) as file: #打開我們的字典文件，它的新名字是file
    while True:
        dirdic = file.readline().strip()
        if (len(dirdic) == 0):
            break
webdict.append(website + dirdic)

for king in webdic:
    try:
        response = requests.get(king,headers=header)
        if response.status_code == 200:
            print('[' + str(response.status_code) + ']' + ":" + king
    except Exception as e:
        print('error')
