import requests
from extensions import extensions_list
from typing import List
from threading import Thread
import progressbar

valid_urls: List = []

progress_bar = None
bar_progression = 0

def check_for_wawacity(ext):
    global valid_urls, progress_bar, bar_progression
    url: str = str("http://wawacity"+ext)
    try:
        response = requests.request(
            method="GET",
            url=url,
            timeout=0.5
        )

        if response.status_code == 200:
            if "sur WawaCity" in response.text:
                valid_urls.append(url)
    except:
        pass

    bar_progression += 1
    progress_bar.update(bar_progression)

if __name__ == "__main__":
    print("starting")
    print(len(extensions_list))
    progress_bar = progressbar.ProgressBar(max_value=len(extensions_list), )
    threads = []
    for extension in extensions_list:
        thread = Thread(
            target=check_for_wawacity,
            args=(extension,)
        )
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    print("\n")
    for url in valid_urls:
        print("-> " + url)