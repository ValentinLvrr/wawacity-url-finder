from threading import Thread
from extensions import extensions
import requests
import math
import time

url = "http://www.wawacity{}"

validLinks = []
threadList = []
checkedLinks = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def req_wawacity(url):

    global checkedLinks

    try:
        res = requests.get(url=url, timeout=2)
        if res.status_code == 200:
            if 'sur WawaCity' in res.text:
                validLinks.append(url)
    except:
        pass
    
    checkedLinks += 1
    percentage = math.floor((checkedLinks / len(extensions))*100)
    print(f'[+] Tested Urls: {percentage}%', end='\r')

def get_country(dom):
    query = dom.split('http://www.')[1]
    res = requests.get(f"http://ip-api.com/json/{query}")
    json = res.json()
    return json['country']

def main():

    print('[+] Tool by ValentinLvrr')
    

    start_time = time.time()

    for i in extensions:
        test_url = url.format(i)
        thread = Thread(
            target=req_wawacity,
            args=(test_url,)
        )
        threadList.append(thread)
        thread.start()

    for thread in threadList:
        thread.join()
        
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"\n[+] Found in {execution_time:.2f} seconds")

    if len(validLinks) == 1:
      print(f"[+] {validLinks[0]} - {get_country(validLinks[0])}")
      
    elif len(validLinks) > 1:
        print(f"[+] {len(validLinks)} found")
        for i in validLinks:
            print(f"[+] {i}")
    else:
        print("[+] Link not found")
        


if __name__ == '__main__':
    main()
    input()