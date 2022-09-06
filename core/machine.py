import yfinance as yf 
import pandas as pd 
import numpy as np


ativo = yf.Ticker("WDOc1")
#print(ativo.info)

hist =  ativo.history(period="max")
#print(hist)



print(hist)
