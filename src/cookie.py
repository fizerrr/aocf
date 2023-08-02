from selenium import webdriver


def return_cookie(url):
    driver = webdriver.Chrome()

    driver.get(url)

    cookies = driver.get_cookies()

    return cookies[1]['value']
