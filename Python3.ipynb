import shutil

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import random
import os
import numpy as np
import matplotlib.pyplot as plt


PIC_NUM = 505

def mkdir(path):
    floder = os.path.exists(path)
    if not floder:
        os.makedirs(path)
        print("new folder...")
        print("OK")
    else:
        print("there is a folder!")

def get_dir_size(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/56.0.2924.87 Safari/537.36'}

fileList = {'sunflower':'%E5%90%91%E6%97%A5%E8%91%B5','rose':"%E7%8E%AB%E7%91%B0",
            'dandelion':"%E8%92%B2%E5%85%AC%E8%8B%B1",'daisy':'%E9%9B%8F%E8%8F%8A',
            'tulip':"%E9%83%81%E9%87%91%E9%A6%99"}

mkdir("temp")
for item in fileList.keys():
    mkdir(item)
    page = 0
    count = 0
    while (count < PIC_NUM):
        print(str(count))
        url = "https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+fileList[item]+"&pn="+str(count)+\
              "&ct=&ic=0&lm=-1&width=0&height=0"
        print(url)
        html = urlopen(url).read().decode('utf-8')
        with open("temp"+"//"+item+str(page)+'.html', 'w') as fp:
            fp.write(html)
        for addr in re.findall(str('"objURL":"(.*?)"'), html, re.S):
            if(count > PIC_NUM-1):
                continue
            print("正在爬取第"+str(count)+"张图片："+addr)
            try:
                pics = requests.get(addr,timeout = 10)
            except requests.exceptions.ConnectionError:
                print("Url请求错误")
            fq = open(item+"//"+str(count)+".png", 'w+b')
            fq.write(pics.content)
            fq.close()
            count += 1
            print('下载完成。'+str(count))
        page += 1

mkdir("test")
for item in fileList.keys():
    for i in range(0,5):
        shutil.move(item+'//'+str(random.randint(0,505))+'.png', 'test//'+item+str(i)+'.png')


size = {}
for item in fileList.keys():
    size[item] = get_dir_size(item)
    print(item+' size is: %.3f Mb' % (size[item] / 1024 / 1024))
size['test'] = get_dir_size('test')

print('test size is: %.3f Mb' % (size['test'] / 1024 / 1024))
#print(size)


sunflower = [0]
rose = [0]
i = 0
for root, dirs, files in os.walk('sunflower'):
    sunflower = np.array([os.path.getsize(os.path.join(root, name)) for name in files]) / 1024
    i += 1
sunflower.sort()
#print(sunflower)
i = 0
for root, dirs, files in os.walk('rose'):
    rose = np.array([os.path.getsize(os.path.join(root, name)) for name in files]) / 1024
    i += 1
rose.sort()
#print(rose)
X = np.linspace(1,500,500,endpoint=True)

sunflowerMean=np.mean(sunflower)
roseMean = np.mean(rose)

sunflowerVar = np.var(sunflower)
print('方差值为：'+str(sunflowerVar))
roseVar = np.var(rose)
print('方差值为：'+str(roseVar))

#曲线
plt.scatter(X, sunflower, color = "blue", linewidth = 1.0,linestyle="-", label = "sunflower")
plt.scatter(X, rose, color = "green", linewidth = 1.0,linestyle="-", label = "rose")
#均值
plt.axhline(y = sunflowerMean,color="red",linestyle="dotted", label = "sunflowerMean")
plt.axhline(y = roseMean,color="grey",linestyle="dotted", label = "sunflowerMean")
#99%分位线
sunflowerPercentile99 = np.percentile(sunflower, 99)
rosePercentile99 = np.percentile(rose, 99)
plt.axhline(y = sunflowerPercentile99,color="yellow",linestyle="dotted", label = "sunflowerPercentile99")
plt.axhline(y = rosePercentile99,color="black",linestyle="dotted", label = "rosePercentile99")
#80%分位线
sunflowerPercentile80 = np.percentile(sunflower, 80)
rosePercentile80 = np.percentile(rose, 80)
plt.axhline(y = sunflowerPercentile80,color='aliceblue',linestyle="dotted", label = "sunflowerPercentile80")
plt.axhline(y = rosePercentile80,color='mediumseagreen',linestyle="dotted", label = "rosePercentile80")

plt.xlabel("Pics",fontsize=15)
plt.ylabel("KB",fontsize=15)
plt.legend(loc='upper left')

plt.show()
