import scrapy
from .items import DBItem
from urllib.parse import unquote
import re
#from scrapy.utils.response import open_in_browser
NUMBER_OF_RESPONSER_PER_PAGE = 55

class ProxylistSpider(scrapy.Spider):
    name = 'proxylist'
    allowed_domains = ['www.freeproxylist.net']
    start_urls = ['https://www.freeproxylists.net/']
    def parse(self,response):
        #open_in_browser(response)
        for i in range(NUMBER_OF_RESPONSER_PER_PAGE):
            database = DBItem()
            if i < 2 :
                pass
            else:
                ipadress = response.xpath('(//table[@class="DataGrid"]//tr[{}]//td[{}]//text())'.format(i, 1)).get(),
                port = response.xpath('(//table[@class="DataGrid"]//tr[{}]//td[{}]//text())'.format(i, 2)).get(),
                protocol =  response.xpath('(//table[@class="DataGrid"]//tr[{}]//td[{}]//text())'.format(i, 3)).get(),
                anonymity =  response.xpath('(//table[@class="DataGrid"]//tr[{}]//td[{}]//text())'.format(i, 4)).get(),
                country =  response.xpath('(//table[@class="DataGrid"]//tr[{}]//td[{}]//text())'.format(i, 5)).get(),
                region = response.xpath('(//table[@class="DataGrid"]//tr[{}]//td[{}])'.format(i, 6)).get(),
                city = response.xpath('(//table[@class="DataGrid"]//tr[{}]//td[{}])'.format(i, 7)).get(),
                uptime = response.xpath('(//table[@class="DataGrid"]//tr[{}]//td[{}])'.format(i, 8)).get(),
                rresponse= response.xpath('(//table[@class="DataGrid"]//tr[{}]//td[{}])'.format(i, 9)).get(),
                transfer = response.xpath('(//table[@class="DataGrid"]//tr[{}]//td[{}])'.format(i, 10)).get()

                ipadressmanip =str(ipadress).replace('IPDecode(',"").replace(')','')
                ipadressmanip2 = unquote(ipadressmanip).replace("('",'').replace('\"<a href=\"','').replace("\"",'').replace("https://www.freeproxylists.net/",'').replace(">","").replace("</a',",'')

                if ipadressmanip2 in (" ',") or ipadressmanip2 in ('(None,', None, " ", "(adsbygoogle = window.adsbygoogle || [].push({};',", "IP Address',"):
                    continue
                else:
                    database['ipadress'] = re.sub(".*.html",'',ipadressmanip2)
                    database['port'] = str(port).replace('(','').replace(',','').replace(')','').replace("'",'')
                    database['protocol'] = str(protocol).replace('(','').replace(',','').replace(')','').replace("'",'')

                    anonymitymanip = str(anonymity).replace('(','').replace(',','').replace(')','').replace("'",'')
                    database['anonymity'] = anonymitymanip
                    database['country'] = str(country).replace('(','').replace(',','').replace(')','').replace("'",'').strip()

                    if region == ('<td></td>'):
                        database['region'] = 'Null'
                    else:
                        database['region'] = str(region).replace('(','').replace(',','').replace(')','').replace('<td>','').replace('</td>','').replace("'",'').strip()

                    if city == ("<td></td>"):
                        database['city'] = 'Null'
                    else:
                        database['city'] = str(city).replace('<td>','').replace('</td>','').replace('(','').replace(',','').replace(')','').replace("'",'').strip()

                    uptimemanip = str(uptime).replace('<td align="center">','').replace('%</td>','').replace("('",'').replace("',)",'').replace('(','').replace(',','').replace(')','')
                    database['uptime'] = uptimemanip

                    rresponsemanip = str(rresponse).replace('<td><div class="graph"><span class="bar" style="width:','').replace('%;background:#008000;"></span></div></td>','').replace('(','').replace(',','').replace(')','').replace("%;background:#ffd700;\"></span></div></td>'",'').replace("'",'')
                    database['runtime'] = rresponsemanip
                    
                    transfermanip = str(transfer).replace('<td><div class="graph"><span class="bar" style="width:','').replace('%;background:#008000;"></span></div></td>','').replace('%;background:#ffd700;\"></span></div></td>','')
                    database['transfer'] = transfermanip
                yield database