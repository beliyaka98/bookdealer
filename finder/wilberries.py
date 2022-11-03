from bs4 import BeautifulSoup
import time
from selenium.webdriver import Chrome
import html5lib

def search_book_wildberries(name):
    domain = 'https://kz.wildberries.ru'
    driver = Chrome('/Users/theak/.wdm/drivers/chromedriver/win32/106.0.5249/chromedriver')

    url = 'https://kz.wildberries.ru/catalog?search='+name+"&subject=381"
    driver.get(url)
    time.sleep(4)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    books_soup = soup.findAll('div', class_='card-cell')

    if not books_soup:
        driver.close()
        return []

    book_name = books_soup[0].find('span', class_='category-name').text
    books_list = []
    for i in range(min(len(books_soup), 3)):
        book_soup = books_soup[i]
        item = book_soup.find('span', class_='category-name').text
        if item==book_name:
            info = ({'book_name': book_name,'book_env': 'пакет', 'book_genre': 'Белгісіз жан',
                    'book_price': int(book_soup.find('span', class_='price__lower').text[:-3].replace(' ', '')),
                    'book_link': domain + book_soup.find('a', class_='card__link')['href'], 'img_src': book_soup.find('img', class_='card-img')['src']})
            books_list.append(info)
    driver.close()
    return books_list
