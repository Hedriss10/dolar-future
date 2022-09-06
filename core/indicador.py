from conection import requestOne
from bs4 import BeautifulSoup as bf 


# dataFrame = [linesPrice, priceOpen, priceClose, priceVarietion]



soupText = bf(requestOne.text, 'html.parser')
linesPrice = soupText.find(id='bid-ask-data').find(id='quoteElementPiece5') # volume
priceOpen =  soupText.find(id='quoteElementPiece11') # abertura 
priceClose =  soupText.find(id="quoteElementPiece14") # fechamento   
priceVarietion = soupText.find(id='quoteElementPiece2') # variação  
    


        