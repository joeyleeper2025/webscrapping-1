from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

#scrape the first page 
url = 'https://quotes.toscrape.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

quote_data_list = []

quote_data = soup.find_all('div', attrs={'class': 'quote'})
quote_data_list.extend(quote_data)  

#scrape 2-10 pages 
for i in range(2, 11):  
    url = 'https://quotes.toscrape.com/page/' + str(i) + '/'  

    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    quote_data = soup.find_all('div', attrs={'class': 'quote'})
    quote_data_list.extend(quote_data)  

#find how many quotes have been scraped (should be 100)
total_quotes = len(quote_data_list)
print(f"Total number of quotes scraped: {total_quotes}")

#author analysis 
author_quotes = {}
for quote in quote_data_list:
    author_text = quote.find('small', {'class': 'author'})
    author_name = author_text.text

    if author_name in author_quotes:
        author_quotes[author_name] += 1
    else:
        author_quotes[author_name] = 1

sorted_authors = sorted(author_quotes, key=author_quotes.get, reverse=True)
authors_with_one_quote = []

for author, quote_count in author_quotes.items():
    if quote_count == 1:
        authors_with_one_quote.append(author)

print('Author: Number of Quotes')
for author, number in author_quotes.items():
    print(f"{author}: {number}")

print(f"The author with the most quotes is {sorted_authors[0]}")
print()
print("Authors with only one quote:")
x = 'Y'

for author in authors_with_one_quote:
    print(author)
    x = input("Do you want to continue and see another author with one quote ('Y/N'): ").upper()
    if x not in ['Y', 'N']:
        print("Invalid input")
    if x == 'N':
        break
else:
    print("There are no more quotes")

#quote length analysis 
quotes_lengths = []
quote_list = []

for quote in quote_data_list:
    quote_text = quote.find('span', {'class': 'text'}).text
    quote_list.append(quote_text)  
    quote_length = len(quote_text)  
    quotes_lengths.append(quote_length) 

average_length = sum(quotes_lengths) / len(quotes_lengths)

longest_index = quotes_lengths.index(max(quotes_lengths))
shortest_index = quotes_lengths.index(min(quotes_lengths))
longest_quote = quote_list[longest_index]
shortest_quote = quote_list[shortest_index]

print()
print(f"The average length of a quote is {average_length}")
print()
print(f"The longest quote is {len(longest_quote)} characters long")
print()
print(f"The shortest quote is {len(shortest_quote)} characters long")
print()

#tag analysis 
tag_counts = {}
x = 'Y'

for quote in quote_data_list:
    tag_elements = quote.findAll('a', {'class': 'tag'})
    for tag_element in tag_elements:
        tag_text = tag_element.text
        if tag_text in tag_counts:
            tag_counts[tag_text] += 1
        else:
            tag_counts[tag_text] = 1

sorted_tags = sorted(tag_counts, key=tag_counts.get, reverse=True)

tag_once = []

for tag, tag_count in tag_counts.items():
    if tag_count == 1:
        tag_once.append(tag)

print('Tag: Number of Occurences')
for tag , number in tag_counts.items():
    print(f"{tag}: {number}")

x = 'Y'
print(f"The most popular tag is {sorted_tags[0]}")
print()
print("Tags only used once:")
for single_tagger in tag_once:
    print(single_tagger)
    x = input("Do you want to continue and see another tag used once ('Y/N'): ").upper()
    if x not in ['Y', 'N']:
        print("Invalid input")
    if x == "N":
        break
else:
    print("There are no more tags")

print(f'The total number of tags is {sum(tag_counts.values())}')

# plotly bar chart with pandas 

import plotly.express as plot
import pandas as panda

# top 10 authors 
author_df = panda.DataFrame(author_quotes.items(), columns=['Author', 'Number of quotes'])

author_df_sorted = author_df.sort_values(by='Number of quotes', ascending=False)

top_10_authors = author_df_sorted.head(10)

fig = plot.bar(top_10_authors, x='Author', y='Number of quotes', title='Top 10 Authors')
fig.update_layout(xaxis_title='Author', yaxis_title='Number of Quotes')
fig.show()

# top 10 tags 
tags_df = panda.DataFrame(tag_counts.items(), columns=['Tag', 'Number of tags'])

tags_df_sorted = tags_df.sort_values(by='Number of tags',ascending=False)

top_10_tags = tags_df_sorted.head(10)

fig = plot.bar(top_10_tags, x="Tag", y="Number of tags", title='Top 10 Tags')
fig.update_layout(xaxis_title='Tag',yaxis_title= 'Number of tags')
fig.show()






