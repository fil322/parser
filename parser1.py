import csv
import requests
import re
import lxml
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['symbol'], data['url'], data['price']))

def get_data(html):
    soup = BeautifulSoup(html, "lxml")

    trs = soup.find("table", class_="h7vnx2-2 cgeQEz cmc-table").find("tbody").find_all("tr")

    for tr in trs:
        tds = tr.find_all("td")

        try:
            name = tds[2].find_all("span")[1].text
        except:
            name = tds[2].find("div", class_="sc-1prm8qw-0 pbu8wv-1 jDuhZQ name-area").find("p").text
        try:
            symbol = tds[2].find("a").find("span", class_="crypto-symbol").text
        except:
            symbol = tds[2].find("p", class_="sc-14rfo7b-0 emEbFH coin-item-symbol").text
        try:
            url = "https://coinmarketcap.com" + tds[2].find("a", class_="cmc-link").get("href")
        except:
            url = ""
        try:
            pr = tds[3].find("span").text
            price = pr[1:].replace(",", "")
        except:
            price = ""

        data = {"name": name,
                "symbol": symbol,
                "url": url,
                "price": price}

        write_csv(data)


def main():
    url = "https://coinmarketcap.com/"
    get_data(get_html(url))
    soup = BeautifulSoup(get_html(url), 'lxml')
    end = soup.find("ul", class_="pagination").find_all("li")
    lp = end[6].find("a").text
    for i in range(1, int(lp) + 1):
        url = "https://coinmarketcap.com/" + f"?page={i}"
        get_data(get_html(url))
    # while True:
    #     get_data(get_html(url))
    #     soup = BeautifulSoup(get_html(url), 'lxml')
    #     end = soup.find("ul", class_="pagination").find_all("li")
    #     lp = end[6].find("a").text
    #     print(lp)
    #     for i in range(int(lp)+1):
    #         url = "https://coinmarketcap.com/" + f"?page={i}"
        # try:
        #     url = "https://coinmarketcap.com/" + soup.find("ul", class_="pagination").find("li", class_="next").find("a").get("href")
        # except:
        #     break


if __name__ == "__main__":
    main()
