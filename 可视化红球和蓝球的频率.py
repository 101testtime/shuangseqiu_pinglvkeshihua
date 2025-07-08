import re

import matplotlib.pyplot as plt
import pickle
import numpy as np
import requests
url = 'https://jc.zhcw.com/port/client_json.php?'


headers = {
'cookie':
'_gid=GA1.2.224374285.1724313188; PHPSESSID=8lqksn9dpto79e1u0kcfc5dhd2; Hm_lvt_692bd5f9c07d3ebd0063062fb0d7622f=1724313189,1724330090; HMACCOUNT=CBFE31DF9FA5D9BA; Hm_lvt_12e4883fd1649d006e3ae22a39f97330=1724313189,1724330090; Hm_lpvt_692bd5f9c07d3ebd0063062fb0d7622f=1724331512; _ga_9FDP3NWFMS=GS1.1.1724330089.5.1.1724331511.0.0.0; Hm_lpvt_12e4883fd1649d006e3ae22a39f97330=1724331512; _ga=GA1.2.1223502022.1714049288; _gat_UA-66069030-3=1',
'host':
'jc.zhcw.com',
'referer':
'https://www.zhcw.com/',
'sec-ch-ua':'"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
'sec-ch-ua-mobile':
'?0',
'sec-ch-ua-platform':
"Windows",
'sec-fetch-dest':
'script',
'sec-fetch-mode':
'no-cors',
'sec-fetch-site':
'same-site',
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

def get_zuixinqihao():
    url = 'https://jc.zhcw.com/port/client_json.php?'

    headers = {
        'cookie':
            '_gid=GA1.2.224374285.1724313188; PHPSESSID=8lqksn9dpto79e1u0kcfc5dhd2; Hm_lvt_692bd5f9c07d3ebd0063062fb0d7622f=1724313189,1724330090; HMACCOUNT=CBFE31DF9FA5D9BA; Hm_lvt_12e4883fd1649d006e3ae22a39f97330=1724313189,1724330090; Hm_lpvt_692bd5f9c07d3ebd0063062fb0d7622f=1724331512; _ga_9FDP3NWFMS=GS1.1.1724330089.5.1.1724331511.0.0.0; Hm_lpvt_12e4883fd1649d006e3ae22a39f97330=1724331512; _ga=GA1.2.1223502022.1714049288; _gat_UA-66069030-3=1',
        'host':
            'jc.zhcw.com',
        'referer':
            'https://www.zhcw.com/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile':
            '?0',
        'sec-ch-ua-platform':
            "Windows",
        'sec-fetch-dest':
            'script',
        'sec-fetch-mode':
            'no-cors',
        'sec-fetch-site':
            'same-site',
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    params = {
            'callback': 'jQuery112207492523503407293_1724331511409',
            'transactionType': '10001001',
            'lotteryId': 1,
            'issueCount': 30,
            'startIssue': '',
            'endIssue': '',
            'startDate':'',
            'endDate':'',
            'type': 0,
            'pageNum': 1,
            'pageSize': 30,
            'tt': 0.2727066704815666,
            '_': '1724331511411'
        }
    resp = requests.get(url=url, headers=headers,params=params)
    result = resp.text
    # print(result)
    pattern_zuixingihao = r'"issue":"(.*?)"'
    qihao = re.findall(pattern_zuixingihao, result)
    return qihao[0]

def get_pages_zong(endIssue):
    params = {
            'callback': 'jQuery112207492523503407293_1724331511409',
            'transactionType': '10001001',
            'lotteryId': 1,
            'issueCount': 0,
            'startIssue': 2003001,
            'endIssue': endIssue,
            'startDate':'',
            'endDate':'',
            'type': 1,
            'pageNum': 1,
            'pageSize': 30,
            'tt': 0.2727066704815666,
            '_': '1724331511411'
    }
    resp = requests.get(url=url, headers=headers,params=params)
    result = resp.text
    pattern_pages = r'"pages":"(.*?)"'
    pages = re.findall(pattern_pages, result)
    print('需要爬取页数为',pages[0])
    return pages[0]

get_pages_zong(get_zuixinqihao())
def get_data():
    import requests, json, re, pickle
    import pandas as pd
    '''
    通过爬虫爬取号码再用字典进行排序，将排序的结果储存在pkl文件中，
    pkl文件中中的数据格式为[{红球频率},{蓝球频率}]
    '''
    url = 'https://jc.zhcw.com/port/client_json.php?'

    headers = {
        'cookie':
            '_gid=GA1.2.224374285.1724313188; PHPSESSID=8lqksn9dpto79e1u0kcfc5dhd2; Hm_lvt_692bd5f9c07d3ebd0063062fb0d7622f=1724313189,1724330090; HMACCOUNT=CBFE31DF9FA5D9BA; Hm_lvt_12e4883fd1649d006e3ae22a39f97330=1724313189,1724330090; Hm_lpvt_692bd5f9c07d3ebd0063062fb0d7622f=1724331512; _ga_9FDP3NWFMS=GS1.1.1724330089.5.1.1724331511.0.0.0; Hm_lpvt_12e4883fd1649d006e3ae22a39f97330=1724331512; _ga=GA1.2.1223502022.1714049288; _gat_UA-66069030-3=1',

        'host':
            'jc.zhcw.com',
        'referer':
            'https://www.zhcw.com/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile':
            '?0',
        'sec-ch-ua-platform':
            "Windows",
        'sec-fetch-dest':
            'script',
        'sec-fetch-mode':
            'no-cors',
        'sec-fetch-site':
            'same-site',
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    hongqiu_pinlu_dic = {}
    endIssue = get_zuixinqihao()
    get_page =get_pages_zong(get_zuixinqihao())
    lanqiu_pinlu_dic = {}
    for n in range(int(get_page)):
        params = {
            'callback': 'jQuery112207492523503407293_1724331511409',
            'transactionType': '10001001',
            'lotteryId': 1,
            'issueCount': 0,
            'startIssue': 2003001,
            'endIssue': endIssue,
            'startDate': '',
            'endDate': '',
            'type': 1,
            'pageNum': n + 1,
            'pageSize': 30,
            'tt': 0.2727066704815666,
            '_': '1724331511411'
        }
        resp = requests.get(url=url, headers=headers, params=params)
        result = resp.text
        # print(result)
        # 找出红球
        pattern_red = r'"frontWinningNum":"(.*?)"'
        matches_red = re.findall(pattern_red, result)

        # 找出蓝球
        pattern_blue = r'"backWinningNum":"(.*?)"'
        matches_blue = re.findall(pattern_blue, result)
        print(f'第{n}页数据爬取完毕！！！')
        print(f'第{n}页数据开始解析！！！')
        # 统计红球和蓝球的频率
        for i in range(len(matches_red)):

            red_list = matches_red[i].split()
            blue = int(matches_blue[i])
            for red in red_list:

                red = int(red)
                if red in hongqiu_pinlu_dic:
                    hongqiu_pinlu_dic[red] += 1

                else:
                    hongqiu_pinlu_dic[red] = 1

            if blue in lanqiu_pinlu_dic:
                lanqiu_pinlu_dic[blue] += 1
            else:
                lanqiu_pinlu_dic[blue] = 1
        print(f'第{n}页数据解析完毕！！！')
        # if n==3:#调试用，只爬取3页数据
        # break
    # 字典的排序
    red_paixu = {}
    blue_paixu = {}

    keys_red = hongqiu_pinlu_dic.keys()  # 红球
    key_list_red = list(keys_red)
    key_list_red.sort()

    keys_blue = lanqiu_pinlu_dic.keys()  # 蓝球
    key_list_blue = list(keys_blue)
    key_list_blue.sort()

    print(key_list_red)
    print(key_list_blue)
    # 红球开始排序
    for key_red in key_list_red:
        value_red = hongqiu_pinlu_dic[key_red]
        red_paixu[key_red] = value_red
    print('红球排序完毕！！！')
    # 蓝球开始排序
    for key_blue in key_list_blue:
        value_blue = lanqiu_pinlu_dic[key_blue]
        blue_paixu[key_blue] = value_blue
    print('蓝球排序完毕！！！')
    print('排序完毕！！！')
    print('红球频率排序前：', hongqiu_pinlu_dic)
    print('红球频率排序后：', red_paixu)
    print('蓝球频率排序前：', lanqiu_pinlu_dic)
    print('蓝球频率排序后：', blue_paixu)

    data = [red_paixu, blue_paixu]
    with open(r'data/data.pkl', 'wb') as file:
        pickle.dump(data, file)

    with open(r'data/data.pkl', 'rb') as file:
        loaded_data = pickle.load(file)

    print(loaded_data)
get_data()

new_qihao = get_zuixinqihao()
with open('data/data.pkl', 'rb') as f:
    data = pickle.load(f)
hongqiu = data[0]
blue = data[1]
hongqiu_qian = list(hongqiu.keys())
hongqiu_zhi = list(hongqiu.values())
print(hongqiu_qian)
print(hongqiu_zhi)
blue_qian = list(blue.keys())
blue_zhi = list(blue.values())
total = 0
for num in blue_zhi:
    total += num
print(blue_qian)
print(blue_zhi)
print(data)
print("双色球总期数：",total)
# 绘制红球频率图
plt.rcParams['font.family'] = 'SimHei'
fig = plt.figure()
bars = plt.bar(hongqiu_qian, hongqiu_zhi, color='red')
plt.gcf().set_size_inches(11, 6)

plt.xticks(hongqiu_qian)
plt.xlabel("红球号码",fontsize=12,color='blue')
plt.ylabel("出现次数",fontsize=12,color='blue')
# plt.text(0, 6, '图片标签', fontsize=12)
plt.text(0.01, 0.95, f"2003001期-{new_qihao}期",color='red', fontsize=20,transform=fig.transFigure)
plt.text(0.92, 0.65,s= "双",color='red', fontsize=25,transform=fig.transFigure)
plt.text(0.92, 0.55,s= "色",color='red', fontsize=25,transform=fig.transFigure)
plt.text(0.92, 0.45,s= "球",color='red', fontsize=25,transform=fig.transFigure)
plt.text(0.85, 0.95, f"总计{total}期",color='red', fontsize=20,transform=fig.transFigure)
plt.title("红球频率图",backgroundcolor='red', color='yellow',fontsize=20,pad=20)
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())), ha='center', va='bottom',color='green')


plt.savefig(r'data/红球频率图{}.png'.format(total))
plt.show()

# 绘制蓝球频率图
fig = plt.figure()
plt.rcParams['font.family'] = 'SimHei'
bars = plt.bar(blue_qian, blue_zhi, color='red')


plt.xticks(blue_qian)
plt.xlabel("蓝球号码",fontsize=12,color='blue')
plt.ylabel("出现次数",fontsize=12,color='blue')
plt.text(0.92, 0.65,s= "双",color='red', fontsize=25,transform=fig.transFigure)
plt.text(0.92, 0.55,s= "色",color='red', fontsize=25,transform=fig.transFigure)
plt.text(0.92, 0.45,s= "球",color='red', fontsize=25,transform=fig.transFigure)
plt.text(0.01, 0.95, f"2003001期-{new_qihao}期",color='red', fontsize=20,transform=fig.transFigure)
plt.text(0.85, 0.95, f"总计{total}期",color='red', fontsize=20,transform=fig.transFigure)
plt.title("蓝球频率图",backgroundcolor='red', color='yellow',fontsize=20,pad=20)
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())), ha='center', va='bottom',color='green')

plt.gcf().set_size_inches(10, 6)
plt.savefig(r'data/蓝球频率图{}.png'.format(total))
plt.show()
