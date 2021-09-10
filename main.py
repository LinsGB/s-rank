#código para ujudar na estratégia S-RANK com FIIs https://clubedovalor.com.br/blog/melhores-fiis-s-rank/

import json

import requests
from bs4 import BeautifulSoup

def read_data():
    f = open('ranking.json',)
    data = json.load(f)
    get_best_fiis(data)


def get_best_fiis(data):
    #build_data()
    print(get_bests_dy_pvpa(data))

def get_bests_dy_pvpa(data):
    dys = []
    pvpas = []
    for dic in data:
        liquidity = convert_to_number(data[dic]["Liquidez Di\u00e1ria"])
        dy = convert_to_number(data[dic]["DY Ano"])
        pvpa = convert_to_number((data[dic]["P/VPA"]))
        if liquidity != 'N/A' and valid_liquidity(liquidity) == True:
            if dy != 'N/A':
                dys.append([dic,dy])
            if pvpa != 'N/A':
                pvpas.append([dic,pvpa])
    dys = sorted(dys, key=lambda dy: dy[1])[::-1]
    pvpas = sorted(pvpas, key=lambda pvpa: pvpa[1])
    add_grade_to_list(dys)
    add_grade_to_list(pvpas)
    return build_fii_rank(dys, pvpas)

def build_fii_rank(dys, pvas):
    fii_rank = {}
    for dy in dys:
        fii_rank[dy[0]] = dy[2]
    for pva in pvas:
        if pva[0] in fii_rank:
            fii_rank[pva[0]] = fii_rank[pva[0]] + pva[2]
        else:
            fii_rank[pva[0]] = pva[2]
    fii_rank = dict(sorted(fii_rank.items(), key=lambda item: item[1])[:14])
    return fii_rank

def add_grade_to_list(list):
    x = 1
    for data in list:
        data.append(x)
        x = x+1

def valid_liquidity(liquidity):
    if liquidity > 500:
        return True
    return False

def convert_to_number(percentage):
    if percentage != 'N/A':
        return float(percentage.strip('%').replace(',','.'))
    return percentage

def build_data():
    table_info = {}
    page = requests.get('https://www.fundsexplorer.com.br/ranking')
    soup = BeautifulSoup(page.text, 'html.parser')
    table_ranking = soup.find("table", {"id": "table-ranking"})
    table_headers = table_ranking.find_all('th')
    list_headers = []
    for header in table_headers:
        list_headers.append(header.get_text())
    table_row = table_ranking.find('tbody').find_all('tr')
    list_td_data = []
    for row in table_row:
        list_data = []
        td_data = row.find_all('td')
        for data in td_data:
            list_data.append(data.get_text())
        list_td_data.append(list_data)
    for item in list_td_data:
        _dict = {}
        for index in range(0, len(item)):
            _dict.update({list_headers[index]: item[index]})
        table_info[item[0]] = _dict

    with open('ranking.json', 'w') as json_file:
        json.dump(table_info, json_file)

if __name__ == '__main__':
    read_data()