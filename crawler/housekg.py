import httpx
from parsel import Selector

MAIN_URL = "https://www.house.kg/snyat"


def get_page():
    response = httpx.get(MAIN_URL)
    return response.text


def get_links(page):
    selector = Selector(text=page)
    links = selector.css("div.listings-wrapper a::attr(href)").getall()
    return list(map(lambda x: "https://www.house.kg" + x, links))


if __name__ == "__main__":
    page = get_page()
    links = get_links(page)
    print(links)
