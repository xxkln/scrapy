# scrapy
scrapy爬虫新手练习
### book项目，是从豆瓣爬取评价最高分top250的书单信息
### MeiZitu项目，是从meizitu.com爬取“可爱”标签的妹子图片
### ArticleSpider 是从伯乐网站上爬取文章信息，并存入数据库

### 基本步骤
- 选择一个网站
- 定义您想抓取的数据
- 编写提取数据的Spider
- 执行spider，获取数据
- 查看提取到的数据
----
### 环境准备
1. windows 10
2. Python3.4
### 1.Twisted安装
鉴于win10下安装Scrapy总出问题，所以先把Twisted的 whl格式文件下载下来，进行安装
地址：https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
选择对于的python版本，点击链接下载whl文件,如“ Twisted-18.7.0-cp34-cp34m-win_amd64.whl”

**安装Scrapy执行过程中经常出现的问题** 
*building'twisted.test.raiser' extension error: Microsoft Visual C++ 10.0 is required.*
![20180801184513.png](https://upload-images.jianshu.io/upload_images/46858-76ad64076459ced9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 执行pip安装

```
pip install Twisted-18.7.0-cp34-cp34m-win_amd64.whl
```
### 2. Scrapy安装
```
pip install Scrapy
```
### 3.安装pywin32
执行爬虫时可能遇到的错误
No modle named ‘win32api’
解决方案：到如下地址，选择对于版本，下载安装pywin32
地址：https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/
![917446-20160411111406957-1216645592.png](https://upload-images.jianshu.io/upload_images/46858-803f1255eac98603.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
### 3.安装pywin32
执行爬虫时可能遇到的错误：
No module named 'PIL'
```
pip install Pillow
```
