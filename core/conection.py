from bs4 import BeautifulSoup as bf 
import requests as r
from time import sleep

url = 'https://br.advfn.com/bolsa-de-valores/bmf/DOLU22/cotacao'.format('str')


navigator = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}


requestOne = r.get(url, headers=navigator)
