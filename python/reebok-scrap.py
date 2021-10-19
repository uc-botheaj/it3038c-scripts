import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.microcenter.com/product/626571/acer-nitro-xv272u-vbmiiprx-27-wqhd-(2560-x-1440)-170hz-hdmi-dp-freesync-hdr400-ips-led-gaming-monitor").content
soup = BeautifulSoup(data, 'html.parser') 
details = soup.find("h1")
thisspan = ""
for d in details:
    title = d.find("span")
    if title is not None and title != -1:
      thisspan = title

print("Product %s has a price of %s" % (thisspan.get('data-name'), thisspan.get('data-price')))



  