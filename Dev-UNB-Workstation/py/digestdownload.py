import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def download_digest(start_url, output_folder='digest'):
    os.makedirs(output_folder, exist_ok=True)
    next_url = start_url
    page = 1
    headers = {'User-Agent': 'Mozilla/5.0'}

    while next_url:
        print(f"صفحہ {page} پر عملدرآمد: {next_url}")
        try:
            response = requests.get(next_url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print("صفحہ حاصل کرنے میں ناکامی:", e)
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        for idx, img in enumerate(images):
            img_url = img.get('src')
            if not img_url:
                continue
            img_url = urljoin(next_url, img_url)
            img_name = f"page{page}_{idx}_{os.path.basename(img_url)}"
            print("ڈاؤن لوڈ ہو رہی ہے:", img_url)
            try:
                img_response = requests.get(img_url, headers=headers, timeout=10)
                img_response.raise_for_status()
                with open(os.path.join(output_folder, img_name), 'wb') as f:
                    f.write(img_response.content)
            except requests.RequestException as e:
                print("تصویر ڈاؤن لوڈ کرنے میں ناکامی:", e)

        # Updated to use 'string' instead of 'text'
        next_link = soup.find('a', string='Next')  # Fix for DeprecationWarning
        if next_link and next_link.get('href'):
            next_url = urljoin(next_url, next_link.get('href'))
            page += 1
        else:
            print("اگلا صفحہ نہیں ملا۔ ختم ہو گیا۔")
            next_url = None

if __name__ == '__main__':
    start_url = input("Digest کا URL درج کریں: ")
    download_digest(start_url)