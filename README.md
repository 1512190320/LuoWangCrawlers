# LuoWangCrawlers

一个爬取落网最近10页中的期刊标题和封面的爬虫

# 第三方库
- BeautifulSoup4
- Requests

# tips
落网的网页挺清晰的，直接用beahtifulsoup的find_all方法，找到class为name和cover rounded的a标签即可。

通过requests伪装成浏览器请求

requests 真牛逼
