import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape GroupMe messages
def scrape_groupme(groupme_url):
    # Send a GET request to the GroupMe URL
    response = requests.get(groupme_url)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find and extract messages
        messages = soup.find_all('div', class_='message-text')
        if messages:
            # Extract text from messages
            message_texts = [message.get_text(strip=True) for message in messages]
            return message_texts
        else:
            print("No messages found in the chat.")
            return []
    else:
        print("Failed to fetch data from GroupMe")
        return []

# Example GroupMe URL
groupme_url = "https://groupme.com/example_group"

# Scrape GroupMe messages
messages = scrape_groupme(groupme_url)

if messages:
    # Create a DataFrame for analysis
    df = pd.DataFrame({'Message': messages})

    # Perform statistical analysis
    # Example: Calculate the number of messages
    num_messages = len(df)
    print("Number of messages:", num_messages)

    # Example: Calculate the average message length
    avg_message_length = df['Message'].apply(len).mean()
    print("Average message length:", avg_message_length)

    # Example: Find the most frequent words
    words = ' '.join(df['Message']).split()
    word_counts = pd.Series(words).value_counts()
    print("Most frequent words:")
    print(word_counts.head(10))
else:
    print("No messages to analyze.")
