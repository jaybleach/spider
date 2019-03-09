import requests
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None


def main():
    url = 'https://s.taobao.com/search?q=%E7%A7%91%E6%8A%80&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
    html = get_one_page(url)
    print(html)

if __name__ == '__main__':
    main()