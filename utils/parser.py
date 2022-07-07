import requests
from lxml import html

headers = {
    'authority': 'www.sudoku.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}

url = "https://sudoku.com/easy"

session = requests.session()

response = session.get(url, headers=headers)

if response.status_code == 200:
    print("Success")
else:
    print("Bad result")

soup = BeautifulSoup(response.text, 'html.parser')

for element in soup.find_all('li', class_='collection-product'):
    name = element.find('h1', class_="product-card__title").text.strip()
    price = element.find('span', class_="product-card__price").text.strip()
    link = "https://kith.com/" + element.find('a').get('href')


#tree = html.fromstring(url)