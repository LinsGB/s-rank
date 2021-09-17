S-RANK
=============

> :warning: python 3

Script em Python para ajudar na metodologia [s-rank](https://clubedovalor.com.br/blog/melhores-fiis-s-rank/).<br>
A base de dados utilizada foram os fundos no [fundsexplorer](https://www.fundsexplorer.com.br/ranking).

O script vai analizar o DY, P/VPA e a liquidez.<br>

O resultado será algo parecido com a imagem a baixo, um dicionário de {'nome do fundo': nota}, quanto menor a nota melhor
![Sellerfaces](./image/resultado.png)


# Tecnologias usadas no projeto.

- json
- [requests](https://pypi.org/project/requests/)
- [pandas](https://pypi.org/project/pandas/)