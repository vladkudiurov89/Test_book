import requests
from bs4 import BeautifulSoup as bs
import csv
from datetime import datetime
from multiprocessing import Pool


def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_links(html):
    soup = bs(html, 'lxml')
    tds = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')
    links = []
    for td in tds:
        a = td.find('a').get('href')
        link = 'https://coinmarketcap.com' + a
        links.append(link)
    return links


def get_page_data(html):
    soup = bs(html, 'lxml')
    try:
        name = soup.find('h1', class_='details-panel-item--name').text.strip()
    except:
        name = ""
    try:
        price = soup.find("span", id='quote_price').text.strip()
    except:
        price = ""

    data = {'name': name, "price": price}
    return data


def write_csv(data):
    with open("coinmarketcap.csv", 'a') as file:
        writer = csv.writer(file)

        writer.writerow((data['name'], data['price']))
        print(data['name'], 'parsed')


def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)


def main():
    start = datetime.now()
    url = "https://coinmarketcap.com/all/views/all/"
    all_links = get_all_links(get_html(url))
    with Pool(40) as p:
        p.map(make_all, all_links)
    finish = datetime.now()
    total = finish - start
    print(str(total))


if __name__ == '__main__':
    main()
