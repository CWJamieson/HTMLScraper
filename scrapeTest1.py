import requests;
from lxml import html;
import unicodedata


print ("hello world")

page = requests.get("https://guelph.craigslist.ca/search/apa")
tree = html.fromstring(page.content)

#copied from chrome
title = tree.xpath('//span[@id="titletextonly"]/text()')

#what I copied from chrome

#price = tree.xpath('//*[@id="sortable-results"]/div[1]/p[1]/span/span[2]/span[1]/text()')
#rooms = tree.xpath('//*[@id="sortable-results"]/div[1]/p[1]/span/span[2]/span[2]/text()')

#what I changed it too

price = tree.xpath('//span[@class="price"]/text()')
rooms = tree.xpath('//span[@class="housing"]/text()')

start = tree.xpath('//span[@class="rangeFrom"]/text()')
end = tree.xpath('//span[@class="rangeTo"]/text()')

length = int(end[0]) - int(start[0]) +1



for i in range(0,length):

    curTitle=str(title[i])
    curPrice=str(price[i])
    curRooms=str(rooms[i])
    curTitle = curTitle.strip()
    curPrice = curPrice.strip()
    curRooms = curRooms.strip()
    if(curRooms[0] =='/'):
        curRooms = curRooms[2:]
    if(curRooms[len(curRooms)-1] == '-'):
        curRooms = curRooms[:2]
    print("Title:",curTitle,", price:",curPrice,", # of rooms:",curRooms)

input("Press enter to exit")

