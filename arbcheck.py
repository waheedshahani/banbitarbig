from bancor import bancor
from bittrex import bittrex
import time
from datetime import datetime
bittrex_pub_key='f18a6bdb57'
ban=bancor()

bit = bittrex(bittrex_pub_key,'') #bittrex api
def changePercent(a,b):
        change=float(b)-float(a)
        change=change/float(a)
        change=change*100
        return change
while(True):
	banTick=ban.getTicker()['data']['rate']
	bitTick=bit.getticker('ETH-BNT')
	bitBid=bitTick['Bid']
	bitAsk=bitTick['Ask']
	buyBanSellBit=changePercent(banTick,bitBid)
	buyBitSellBan=changePercent(bitAsk,banTick)
	print datetime.now(),"\tBuy BAN-Sell Bit:",buyBanSellBit,"\t","Buy Bit-Sell BAN",buyBitSellBan
	time.sleep(2)
