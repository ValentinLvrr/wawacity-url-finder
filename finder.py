from extensions import extensions
from threading import Thread
import requests

TIMEOUT = 0.5

urls_avaible = []


def test_with_an_extension(ext_to_test):
    url = 'http://wawacity'+ext_to_test
    try:
        res = requests.get(url, timeout=TIMEOUT)
        if 'sur WawaCity' in res.text:
            urls_avaible.append(url)
    except requests.RequestException:
        pass


if __name__ == '__main__':
    print('- number of extensions: {}'.format(len(extensions)))
    threads = [Thread(target=test_with_an_extension, args=(ext,))
               for ext in extensions]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print('- {} urls found !'.format(len(urls_avaible)))
    for url in urls_avaible:
        print('+ ' + url)
