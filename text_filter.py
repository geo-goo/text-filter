import re
import pandas as pd

test_data = [ 
        "Congratulations! You've won a free vacation.",
        "Hi John, can you send me the report?",
        "Get cheap watches and handbags in our online store!",
        "Don't miss the investment chance!",
        "Do you know Binance ? Come to join us!",
        "Do you know Binance ? Come to join us for gain the good profit!"
    ]

# target text url : https://www.chinamoney.com.cn/chinese/zxpjbgh/?bondSrno=&tabtabNum=1&tabid=0&bnc=%E4%B8%8A%E6%B5%B7&ro=&sdt=&edt= 

def generate_pattern():
    key_words = pd.read_csv('text_filter_info/key_words_for_rating_reports.txt',header=None)
    pattern = "|".join(key_words[0])
    return re.compile(fr"{pattern}",re.IGNORECASE)

def re_filter(data):
    pattern = generate_pattern()  # 定义要搜索的模式
    items = []
    for item in data:
        if re.search(pattern, item):
            items.append(item)
    return items

df = pd.read_csv('text_filter_info/text_data.txt',header=None)
print(df.head())
print(re_filter(df[0]))
print(generate_pattern())

# 江东控股集团有限责任公司主体与相关债项2022年度跟踪评级报告