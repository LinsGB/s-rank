import requests
import pandas as pd


def get_data():
    soup = requests.get('https://www.fundsexplorer.com.br/ranking')
    parse_data_table(soup)


def parse_data_table(page):
    dataframe = pd.read_html(page.text, header=None)[0]
    dataframe.to_json(r'ranking.json', orient='records')


if __name__ == '__main__':
    get_data()
