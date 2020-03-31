import re
from urllib import request
import requests
from bs4 import BeautifulSoup

url='http://wufazhuce.com/one/'#每一期公共部分
Path='d:\\onetest\\one_img\\'#图片保存路径
num=0#记录爬取照片的个数
for i in range(171,1775):
    s=str(i)
    currenturl=url+s#当前期的url
    try:
        res=requests.get(currenturl)
        res.raise_for_status()
    except requests.RequestException as e:
        print(e)
    else:
        html=res.text
        soup = BeautifulSoup(html,'html.parser')
        a=soup.select('.one-titulo')#期次
        h=soup.find_all('img')#图片标签
        imgUrl=h[1].get('src')#取图片的链接
        index=re.sub("\D","",a[0].string.split()[0])#取得期次
        if(index==''):
            continue
        imgName=Path+'VOL.'+index+'.jpg'#图片的完整路径含图片名
        request.urlretrieve(imgUrl,imgName)#保存图片
        num+=1
        print('已爬取%s张图片...'%num)   
print('-----爬取结束-----')
