import yfinance as yf
import numpy as np
import pandas as pd
import ta
import pytz
from datetime import timezone, datetime

"""
    intervalo de tempo com 5m no US-dolar Future, IBOVESPA!
"""

baseOne = yf.download("DX-Y.NYB", start="2022-09-02", interval="5m")
baseOne['%K'] = ta.momentum.stoch(
    baseOne.High, baseOne.Low, baseOne.Close, window=14, smooth_window=3)
baseOne['%D'] = baseOne['%K'].rolling(3).mean()
baseOne['rsi'] = ta.momentum.rsi(baseOne.Close, window=14)
baseOne['macd'] = ta.trend.macd_diff(baseOne.Close)
baseOne.dropna(inplace=True)

"""
    obtendo sinais de disparo e fazendo á explicação!,
    colocando tudo em uma unica função
"""


def estrategy(baseOne, lags, buy=True):
    dfx = pd.DataFrame()
    for i in range(1, lags+1):
        if buy:
            mask = (baseOne['%K'].shift(i) < 20) & (
                baseOne['%D'].shift(i) < 20)
        else:
            mask = (baseOne['%K'].shift(i) > 80) & (
                baseOne['%D'].shift(i) > 80)
        dfx = dfx.append(mask, ignore_index=True)
        return dfx.sum(axis=0)
        # print(dfx.sum(axis=0))


baseOne['BuyTrigger'] = np.where(
    estrategy(baseOne, 4), 1, 0)  # tabela de compra analisada
baseOne['SellTrigger'] = np.where(
    estrategy(baseOne, 4, False), 1, 0)  # tabela de venda analisada
baseOne['Buy'] = np.where((baseOne.BuyTrigger) & (baseOne['%K'].between(20, 80))
                          & (baseOne['%D'].between(20, 80)) &
                          (baseOne.rsi > 50) & (baseOne.macd > 0), 1, 0)
baseOne['Sell'] = np.where((baseOne.SellTrigger) & (baseOne['%K'].between(20, 80))  # venda
                           & (baseOne['%D'].between(20, 80))
                           (baseOne.rsi < 50) & (baseOne.macd < 0), 1, 0)


Buying_dates = []  # datas de compra
Sell_dates = []  # datas de venda


def decision():
    for exc in range(len(baseOne) - 1):
        if baseOne.Buy.iloc[exc]:
            Buying_dates.append(baseOne.iloc[exc + 1].name)
            for num, j in enumerate(baseOne.Sell[exc:]):
                if j:
                    Sell_dates.append(baseOne.iloc[exc + num].name)
                break

"""
    controlando ações repetidas
"""


cutti = len(Buying_dates) - len(Sell_dates)


