import Tkinter as tk
import urllib2
from bs4 import BeautifulSoup

def HSI():
    page = 'http://www.etnet.com.hk/www/tc/stocks/indexes_chart.php?subtype=HSI'
    usragent = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(page,headers=usragent)
    openpage = urllib2.urlopen(req)
    soup = BeautifulSoup(openpage,'html.parser')
    target = soup.find('div', class_= 'quotePrice').text

    return target[0:9], target[10:17], target[19:25]


page = 'http://www.etnet.com.hk/www/tc/stocks/realtime/quote.php?code=' + '1'
usragent = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(page,headers=usragent)
openpage = urllib2.urlopen(req)
soup = BeautifulSoup(openpage,'html.parser')
target1 = soup.find('td', class_= 'styleA')

print target1

'''def stock(event):
    page = 'http://www.etnet.com.hk/www/tc/stocks/realtime/quote.php?code=' + input.get()
    usragent = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(page,headers=usragent)
    openpage = urllib2.urlopen(req)
    soup = BeautifulSoup(openpage,'html.parser')
    target1 = soup.find('span', class_= 'Price up2').text
    target2 = soup.find('span', class_='Change').text

    current = target1
    change = target2
    changepct = target2
    label2.configure(text = current + change + changepct)'''

basic  = tk.Tk()
basic.title('Stock GUI')
currentHSI,changeHSI,changepct = HSI()
label = tk.Label(basic,text = 'HSI : ' +currentHSI +'       ' + changeHSI + '       ' + changepct)
label.pack()
basic.mainloop()