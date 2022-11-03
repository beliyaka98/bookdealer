from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import time

def search_book_flip(name):
    domain = 'https://flip.kz'
    url = 'https://flip.kz/search?search=' + name + '&subsection=1'
    driver = Chrome('/Users/theak/.wdm/drivers/chromedriver/win32/106.0.5249/chromedriver')
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    books_soup = soup.findAll('div', class_='p-10')
    if soup.find('title').text == 'Мы заметили подозрительную активность!':
        time.sleep(2)
        driver.close()
        search_book_flip(name)
        driver.close()
        return
    if not books_soup:
        driver.close()
        return []

    book_name = books_soup[0].find('a', class_='title').text
    books_list = []

    for book_soup in books_soup:
        item = book_soup.find('a', class_='title')
        if item.text == book_name and not book_soup.find('div', class_='noavailable'):
            info = ({'book_name': book_name, 'book_env': book_soup.find('span').text,
                     'book_genre': book_soup.findAll('span')[1].text,
                     'book_price': int(book_soup.find('div', class_='price').text.split('₸')[0].replace(' ', '')),
                     'book_link': domain + item['href'], 'img_src': book_soup.find('img')['src']})
            books_list.append(info)
        else:
            break
    driver.close()
    return books_list
