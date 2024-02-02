import json, time
from selenium import webdriver


def main():
    url = 'https://ratings.utmn.ru/api/rating/?action=ratingdata&pageid=78f7edd5-b6ba-407c-b4cf-a575d1cae087'
    fname = time.strftime("%Y-%m-%d-%H%M%S")

    driver = webdriver.Firefox()

    driver.get(url)
    time.sleep(1)

    s = driver.page_source
    i1 = s.find('{')
    i2 = s.rfind('}')
    s = s[i1:i2+1]

    with open(f'wrk/{fname}.txt', 'wt') as res_file:
        res_file.write(s)
        res_file.close()

    s2 = json.loads(s)

    res_file = open(f'wrk/{fname}_res.txt', 'wt')

    for rec in s2["#value"]["Abiturients"]:
        fio = rec["FIO"]
        place = rec["number"]
        consent = rec["consent"]
        bally = rec["sum"]

        if fio == '154-030-469 24':
            our_place = place

        if consent:
            s = f'{place}. {bally}, <{fio}>'
            print(s)
            res_file.write(s + '\n')

    print(f'\nOur place: {our_place}')
    res_file.write(f'\nOur place: {our_place}\n')

    res_file.close()

    driver.quit()


if __name__ == '__main__':
    main()
