import random
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

random_number = random.randrange(1, 22)

if random_number < 10:
    random_chapter = '0' + str(random_number)
else:
    random_chapter = str(random_number)

webpage_url = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage_url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

page_verse = soup.findAll('div', attrs={'class': 'p'})

myverses = []

for section_verses in page_verse:
    verse_list = section_verses.text.split('.')

    for v in verse_list:
        myverses.append(v.strip())

mychoice = random.choice(myverses)
print(f"Chapter: {random_chapter} Verse: {mychoice}")
print()
