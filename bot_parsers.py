import requests
from bs4 import BeautifulSoup


def finder_youtube(content):
    """
    Функция поиска по контексту информации в Youtube
    :param content: строковое значение
    :return: кортеж словарей(название, полная ссылка)
    """
    BASE_URL = "https://youtube.com"

    spam_search = content.replace(' ', '+')
    url = f'{BASE_URL}/results?search_query={spam_search}&pbj=1'
    response = BeautifulSoup(requests.get(url).text, "html.parser")

    results = []
    if response.select(".yt-uix-tile-link"):
        for video in response.select(".yt-uix-tile-link"):
            if video["href"].startswith("/watch?v="):
                video_info = {
                    "title": video["title"],
                    "link": f'{BASE_URL}{video["href"]}'
                }
                results.append(video_info)

    return results


if __name__ == '__main__':
    # тестовые запросы
    print(finder_youtube('abba the winner takes it all'))
    # print(finder_youtube('fhjj sdfkjkj'))
