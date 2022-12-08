import requests

with open('proxies/valid_proxies.txt', 'r') as f:
    proxies = f.read().split('\n')


urls = ['https://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
'https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html']

cnt = 0
for url in urls:
    try:
        print(f'Using proxy: {proxies[cnt]}')
        res = requests.get(url, proxies={'http': proxies[cnt], 'https': proxies[cnt]})

        print(f'Status: {res.status_code}')
        print(res.text)
    except Exception as e:
        print(f'Process failed.\nError: {e}')
    finally:
        cnt += 1
        cnt % len(proxies)