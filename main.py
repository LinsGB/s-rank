import json

import crawler

minimum_liquidity = 1000


def read_data():
    f = open('ranking.json',)
    data = json.load(f)
    get_best_fiis(data)


def get_best_fiis(data):
    crawler.get_data()
    print(get_srank_fiis(data))


def get_srank_fiis(data):
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
    fii_rank_dy = {}
    fii_rank_pvas = {}
    for dy in dys:
        fii_rank_dy[dy[0]] = dy[2]
    for pva in pvas:
        fii_rank_pvas[pva[0]] = pva[2]
    for fii in fii_rank_dy.keys():
        if fii in fii_rank_pvas.keys():
            fii_rank[fii] = fii_rank_dy[fii]+fii_rank_pvas[fii]
    fii_rank = dict(sorted(fii_rank.items(), key=lambda item: item[1])[:14])
    return fii_rank


def add_grade_to_list(list):
    x = 1
    for data in list:
        data.append(x)
        x = x+1


def valid_liquidity(liquidity):
    if liquidity > minimum_liquidity:
        return True
    return False


def convert_to_number(percentage):
    if percentage != 'N/A':
        return float(percentage.strip('%').replace(',','.'))
    return percentage


if __name__ == '__main__':
    read_data()
