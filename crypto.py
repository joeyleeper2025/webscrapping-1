from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.webull.com/quote/crypto'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

coin_data = soup.findAll('div',attrs={'class': 'table-cell'})


i = 1
name_counter = 0

for coins in coin_data[:5]:
    name = soup.findAll('p', attrs={'class': 'tit bold'})
    name_display = name[name_counter].text
    current_price = float(coin_data[i + 1].text.replace(',', ''))  
    percent_change = float(coin_data[i + 2].text.replace(',','').replace('%',''))
    changed_price = round(current_price / (1 + (percent_change)/100),2)
    


    print(f"Name of Currency: {name_display}")
    print(f"The Current Price is: ${current_price:,.2F}")  
    print(f"% change in the last 24 hrs: {percent_change}%")
    print(f"Corresponding price: ${changed_price:,.2F}") 
    print()

    # I tried to scrape the symbol, but I went to Prof. B's office hours and he said that the image was not scrappable because it was a url coded into the background of the tag
    # He said I was fine and didn't need to do it 
    
    i += 10
    name_counter += 1







