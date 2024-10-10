'''
used = int(input())#已使用的流量
video = int(input())#影片需要使用的流量
basic = int(input())#基本流量
warm = int(input())
if used + video <= basic:#全在基本流量裡
    print(video//20)
elif used + video < warm:#部分在警告流量和基本流量裡
    if used < basic:
        green = basic - used#基本流量
        yellow = video - green#警告流量
        print((green//20)+(yellow//5))
    else:#全在警告流量裡
        print(video//5)
else:#總使用流量會超過警告流量
    if used <= basic:#當前流量是否低於基本配額
        green = basic - used#可在基本配額裡下載的部分
        yellow = warm - basic#可在警告配額裡下載的部分
        red = video-(green+yellow)#只能在紅色等級下載的部分
        print((green//20)+(yellow//5)+(red//1))
    elif used > warm:#是否低於警告配額
        yellow = warm - used#可在警告配額裡下載的部分
        red = video - yellow#只能在紅色等級下載的部分
        print((yellow//5)+(red//1))
    else:
        print(video//1)#總使用流量大於警告流量
綠色等級(基本配額)20MB/s
黃色等級(警告配額)5MB/s
紅色等級1MB/s
'''
# 讀取輸入
used = int(input())  # 已使用的流量
video = int(input())  # 影片需要使用的流量
basic = int(input())  # 基本流量
warm = int(input())  # 警告流量

# 計算下載時間
if used + video <= basic:  # 全部下載在基本流量內 (綠色等級)
    print(video // 20)
elif used + video <= warm:  # 部分在基本流量，部分在警告流量 (黃色等級)
    if used < basic:  # 有部分在綠色等級，剩下在黃色等級
        green = basic - used  # 在基本配額裡的部分
        yellow = video - green  # 在警告配額裡的部分
        print((green // 20) + (yellow // 5))
    else:  # 全部在黃色等級
        print(video // 5)
else:  # 使用量超過警告配額 (紅色等級)
    if used < basic:  # 綠色、黃色和紅色三種等級
        green = basic - used  # 在基本配額裡的部分
        yellow = warm - basic  # 在警告配額裡的部分
        red = video - (green + yellow)  # 超過警告配額的部分
        print((green // 20) + (yellow // 5) + (red // 1))
    elif used < warm:  # 黃色和紅色兩種等級
        yellow = warm - used  # 在警告配額裡的部分
        red = video - yellow  # 超過警告配額的部分
        print((yellow // 5) + (red // 1))
    else:  # 全部在紅色等級
        print(video // 1)
