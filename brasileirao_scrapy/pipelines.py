import json
from itemadapter import ItemAdapter


class BrasileiraoScrapyPipeline:

    def open_spider(self, spider):
      print('Iniciando Crawler')
      self.table2021 = open('Tabelas/tabela-2021.txt', 'w', encoding='utf-8')
      self.table2020 = open('Tabelas/tabela-2020.txt', 'w', encoding='utf-8')
      self.table2019 = open('Tabelas/tabela-2019.txt', 'w', encoding='utf-8')
      self.table2018 = open('Tabelas/tabela-2018.txt', 'w', encoding='utf-8')
      self.table2017 = open('Tabelas/tabela-2017.txt', 'w', encoding='utf-8')
      self.table2016 = open('Tabelas/tabela-2016.txt', 'w', encoding='utf-8')
      self.table2015 = open('Tabelas/tabela-2015.txt', 'w', encoding='utf-8')
      self.table2014 = open('Tabelas/tabela-2014.txt', 'w', encoding='utf-8')
      self.table2013 = open('Tabelas/tabela-2013.txt', 'w', encoding='utf-8')
      self.table2012 = open('Tabelas/tabela-2012.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
      print('Concluido com sucesso, os arquivos tabela-ano.txt foram gerados na pasta Tabelas')
      self.table2021.close()
      self.table2020.close()
      self.table2019.close()
      self.table2018.close()
      self.table2017.close()
      self.table2016.close()
      self.table2015.close()
      self.table2014.close()
      self.table2013.close()
      self.table2012.close()

    def process_item(self, item, spider):
        item['colocacao'] = int((item['colocacao']).replace('º',''))
        line = json.dumps(dict(item), ensure_ascii=False)+ '\n'
        if(item['ano'] == "2021"):
          self.table2021.write(line)
        elif(item['ano'] == "2020"):
          self.table2020.write(line)
        elif(item['ano'] == "2019"):
          self.table2019.write(line)
        elif(item['ano'] == "2018"):
          self.table2018.write(line)
        elif(item['ano'] == "2017"):
          self.table2017.write(line)
        elif(item['ano'] == "2016"):
          self.table2016.write(line)
        elif(item['ano'] == "2015"):
          self.table2015.write(line)
        elif(item['ano'] == "2014"):
          self.table2014.write(line)
        elif(item['ano'] == "2013"):
          self.table2013.write(line)
        elif(item['ano'] == "2012"):
          self.table2012.write(line)
        return item
