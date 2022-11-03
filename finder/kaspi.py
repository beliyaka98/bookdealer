from bs4 import BeautifulSoup
import time
from selenium.webdriver import Chrome
import html5lib
def search_book_kaspi(name):

    driver = Chrome('/Users/theak/.wdm/drivers/chromedriver/win32/106.0.5249/chromedriver')
    url = 'https://kaspi.kz/shop/taraz'
    driver.get(url)

    url = 'https://kaspi.kz/shop/search/?text='+name+"&q=%3Acategory%3ABooks"
    driver.get(url)
    driver.execute_script("window.scrollTo(0, 800);")
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html5lib')

    books_soup = soup.findAll('div', class_='item-card')

    if not books_soup:
        driver.close()
        return []

    book_name = books_soup[0].find('a', class_='item-card__name-link').text
    books_list = []
    for book_soup in books_soup:
        item = book_soup.find('a', class_='item-card__name-link').text
        if item==book_name:
            info = ({'book_name': book_name, 'book_env': 'пакет', 'book_genre': soup.findAll('a', class_="tree__link")[3].text,
                     'book_price': int(book_soup.find('span', class_='item-card__prices-price').text[:-2].replace(' ', '')),
                     'book_link': book_soup.find('a', class_='item-card__image-wrapper')['href'],
                     'img_src': book_soup.find('img', class_='item-card__image')['src']})
            books_list.append(info)
    driver.close()
    return books_list
