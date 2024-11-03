# import requests
# from bs4 import BeautifulSoup
#
# # endpoint = 'http://127.0.0.1:8000/api/v1/main/services/steps/'
# # print(requests.get(endpoint, headers={'accept-language': 'uz'}).json())
#
#
# url = 'https://skrivanek.lv/ru/kodi-jazikov/'
# response = requests.get(url).text
# soup = BeautifulSoup(response, 'html.parser')
#
# wrap = soup.find('div', class_='gem-table gem-table-style-1').find_all('tr')
# res = []
# for idx, el in enumerate(wrap):
#     if idx == 0:
#         continue
#     code = el.find_all('td')[0].get_text(strip=True)
#     lang = el.find_all('td')[1].get_text(strip=True)
#     res.append({
#         'code': code.lower(),
#         'lang': lang
#     })
#
# import json
#
# with open('langs.json', 'w', encoding='utf-8') as f:
#     json.dump(res, f, ensure_ascii=False, indent=4)


