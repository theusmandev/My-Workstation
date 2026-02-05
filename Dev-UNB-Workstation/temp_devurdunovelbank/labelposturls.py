import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = 'https://urdunovelbanks.com'  # Website ka URL yahan dalen

# Website se content fetch karen
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Error: Unable to fetch the website. Status code: {response.status_code}")
else:
    soup = BeautifulSoup(response.text, 'html.parser')

    # "Funny Books" label ke posts extract karen
    # NOTE: Adjust the HTML structure according to the website
    funny_books_label = soup.find('div', class_='label', text='Funny Books')  # Adjust class name and text
    if funny_books_label:
        posts = funny_books_label.find_next('div', class_='posts')  # Adjust class name
        funny_books_posts = posts.find_all('div', class_='post')  # Adjust class name

        # Debugging: Check how many posts were found
        print(f"Total posts found under 'Funny Books': {len(funny_books_posts)}")

        # Titles aur links store karen
        data = []
        for post in funny_books_posts:
            try:
                title = post.find('h2').text.strip()  # Title extract karen aur whitespace remove karen
                link = post.find('a')['href']  # Link extract karen
                data.append({'Title': title, 'Link': link})
            except AttributeError as e:
                print(f"Error extracting data from a post: {e}")

        # Debugging: Check if data was collected
        print(f"Data collected: {data}")

        # DataFrame banaye aur Excel file mein save karen
        if data:
            df = pd.DataFrame(data)
            df.to_excel('funny_books_posts.xlsx', index=False)
            print("Data successfully saved to funny_books_posts.xlsx")
        else:
            print("No data found to save.")
    else:
        print("'Funny Books' label not found on the website.")