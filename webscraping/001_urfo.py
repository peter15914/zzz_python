import requests, json, time, ftfy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

good_specs = ['01.00.00', '02.00.00', '10.05.01', '09.03.03', '09.03.02', '09.03.01', '09.03.04']
domain = 'https://urfu.ru'


def good_spec(spec):
    for s in good_specs:
        if s in spec:
            return True
    return False


# def parse_selenium():
#     row_ind = 0
#     # driver.implicitly_wait(0)

#     tbl = driver.find_element(By.TAG_NAME, "table")

#     for row in tbl.find_elements(By.TAG_NAME, "tr"):

#         row_str = ""
#         for cell in row.find_elements(By.TAG_NAME, "td"):
#             row_str += "#" + ftfy.fix_text(cell.text).strip().replace('\n', '')

#         if "Инф" in row_str and good_spec(row_str):
#             print(row_str)
#             g.write(row_str)
#             g.write('\n')
#             row_ind += 1

#         # if row_ind > 10:
#         #     break


def process(driver, res_file):

    for id in range(1, 34):
        url = domain + f'/api/ratings/info/27/{id}/'

        f = requests.get(url)
        try: json_data = json.loads(f.text)
        except: continue

        time.sleep(1)

        url2 = domain + json_data['url']

        driver.get(url2)
        time.sleep(3)

        # soup = BeautifulSoup(driver.page_source, 'html.parser')
        # res_file.write(soup.prettify())

        parse_soup(driver.page_source, res_file)


def parse_soup(html_text, res_file):
    soup = BeautifulSoup(html_text, 'html.parser')

    row_ind = 0
    # tbl = soup.find("table")

    for row in soup.find_all('tr'):
        row_str = ""
        for cell in row.find_all('td'):
            row_str += "#" + ftfy.fix_text(cell.text).replace('\n', '').strip()

        if row_str: #"Инф" in row_str and good_spec(row_str):
            print(row_str)
            res_file.write(row_str)
            res_file.write('\n')
            row_ind += 1

        # if row_ind > 10:
        #     break


def main():
    res_file = open('wrk/res.txt', 'wt')

    driver = webdriver.Firefox()
    process(driver, res_file)
    driver.quit()

    # parse_soup(''.join(open('wrk/_tmp_html.txt').readlines()), res_file)

    res_file.close()


if __name__ == '__main__':
    main()
