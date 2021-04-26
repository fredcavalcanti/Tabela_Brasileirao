# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BrasileiraoScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    ano = scrapy.Field()
    colocacao = scrapy.Field()
    time = scrapy.Field()
    pontos = scrapy.Field()
    jogos = scrapy.Field()
    vitorias = scrapy.Field()
    empates = scrapy.Field()
    derrotas = scrapy.Field()
    gols_pro = scrapy.Field()
    gols_contra = scrapy.Field()
    saldo_de_gols = scrapy.Field()
    cartoes_amarelo = scrapy.Field()
    cartoes_vermelhor = scrapy.Field()
    aproveitamento = scrapy.Field()
    pass
