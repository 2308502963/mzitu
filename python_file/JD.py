#爬取京東商品頁面
import requests
url="https://item.jd.com/8535863.html"
r=requests.get(url)
r.status_for_status()
#r.encoding=r.apparent_encoding
#print(r.text[:1000])

