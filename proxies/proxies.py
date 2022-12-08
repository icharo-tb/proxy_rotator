import threading
import queue
import requests

q_list = queue.Queue()
valid_proxy_list = []
error_list = []

with open('proxy_list.txt', 'r') as f:
    proxies = f.read().split('\n')
    for proxy in proxies:
        q_list.put(proxy)

def clean_list():
    valid_proxy_list.clear()

def check_proxies():
    global q_list
    
    while not q_list.empty():
        proxy = q_list.get()
        try:
            res = requests.get('https://ipinfo.io/8.8.4.4/json',
                                proxies= {'http': proxy, 'https': proxy})
        except Exception as e:
            error_list.append(e)
            continue

        if res.status_code == 200:
            print(f'Status Code: {res.status_code}\nProxy IP: {proxy}')

            with open('valid_proxies.txt', 'a') as f:
                f.write(f'{proxy}\n')

if __name__=='__main__':
    clean_list()

    for _ in range(10):
        threading.Thread(target=check_proxies).start()