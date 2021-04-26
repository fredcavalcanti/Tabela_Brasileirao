import scrapy
from brasileirao_scrapy.items import BrasileiraoScrapyItem

class BrasileiraoSpider(scrapy.Spider):
    name = 'brasileirao'
    #allowed_domains = ['https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2021/']
    start_urls = [
        'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2021/',
        'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2020/',
        'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2019/',
        'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2018/',
        'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2017/',
        'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2016/',
        'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2015/',
        'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2014/',
        'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2013/',
        'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2012/'
    ]

    def parse(self, response):
        ano = response._url.split('/')[-1]
        for dataTable in response.css("table.tabela-expandir tbody tr:not([style='display: none'])"):
            pontos = dataTable.css("th ::text").extract_first()
            allTds = dataTable.css("td ::text").getall()
            result = list(filter(lambda x: x.strip() != "" and x != "E" and x != "V" and x != "D", allTds))
            if(len(result) == 13):
                (colocacao, movimentacao, time, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, saldo_de_gols, cartoes_amarelo, cartoes_vermelhor, aproveitamento) = (result)
            elif(len(result) == 12):
                (colocacao, time, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, saldo_de_gols, cartoes_amarelo, cartoes_vermelhor, aproveitamento) = (result)
                
            tabela = BrasileiraoScrapyItem(ano=ano, colocacao=colocacao, time=time, pontos=pontos, jogos=jogos, vitorias=vitorias, empates=empates, derrotas=derrotas, gols_pro=gols_pro, gols_contra=gols_contra, saldo_de_gols=saldo_de_gols, cartoes_amarelo=cartoes_amarelo, cartoes_vermelhor=cartoes_vermelhor, aproveitamento=aproveitamento)

            yield tabela