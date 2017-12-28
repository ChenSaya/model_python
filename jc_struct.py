# coding:utf-8

class CTPRecordException(Exception):
    pass

# CTP行情数据记录 
class CTPMdRecord:

    def __init__(self, line):

        fields = line.split(",")
        if (len(fields) < 46):
            raise CTPRecordException("fields count: %d" %(len(fields)))

        try:
            self.RecvTime           = fields[0]
            #self.NoUse              = fields[1]
            self.TradingDay         = fields[2]  # 交易日 
            self.InstrumentID       = fields[3]  # 合约代码
            self.ExchangeID         = fields[4]  # 交易所代码
            self.ExchangeInstID     = fields[5]  # 合约在交易所的代码
            self.LastPrice          = float(fields[6])  # 最新价
            self.PreSettlementPrice = float(fields[7])  # 上次结算价
            self.PreClosePrice      = float(fields[8])  # 昨收盘
            self.PreOpenInterest    = float(fields[9])  # 昨持仓量
            self.OpenPrice          = float(fields[10])  # 今开盘
            self.HighestPrice       = float(fields[11])  # 最高价 
            self.LowestPrice        = float(fields[12])  # 最低价
            self.Volume             = float(fields[13])  # 数量
            self.Turnover           = float(fields[14])  # 成交金额
            self.OpenInterest       = float(fields[15])  # 持仓量
            #self.ClosePrice         = float(fields[16])  # 今收盘 (接收到的是空的)
            #self.SettlementPrice    = float(fields[17])  # 本次结算价 (接收到的是空的)
            self.UpperLimitPrice    = float(fields[18])  # 涨停板价
            self.LowerLimitPrice    = float(fields[19])  # 跌停板价
            #self.PreDelta           = float(fields[20])  # 昨虚实度
            #self.CurrDelta          = float(fields[21])  # 今虚实度
            self.UpdateTime         = fields[22]  # 最后修改时间
            self.UpdateMillisec     = fields[23]  # 最后修改毫秒
            self.BidPrice1          = float(fields[24])  # 申买价一
            self.BidVolume1         = float(fields[25])  # 申买量一
            self.AskPrice1          = float(fields[26])  # 申卖价一
            self.AskVolume1         = float(fields[27])  # 申卖量一
            #self.BidPrice2          = fields[28]  # 申买价二
            #self.BidVolume2         = fields[29]  # 申买量二
            #self.AskPrice2          = fields[30]  # 申卖价二 
            #self.AskVolume2         = fields[31]  # 申卖量二
            #self.BidPrice3          = fields[32]  # 申买价三
            #self.BidVolume3         = fields[33]  # 申买量三
            #self.AskPrice3          = fields[34]  # 申卖价三
            #self.AskVolume3         = fields[35]  # 申卖量三
            #self.BidPrice4          = fields[36]  # 申买价四
            #self.BidVolume4         = fields[37]  # 申买量四
            #self.AskPrice4          = fields[38]  # 申卖价四
            #self.AskVolume4         = fields[39]  # 申卖量四
            #self.BidPrice5          = fields[40]  # 申买价五
            #self.BidVolume5         = fields[41]  # 申买量五
            #self.AskPrice5          = fields[42]  # 申卖价五
            #self.AskVolume5         = fields[43]  # 申卖量五
            self.AveragePrice       = fields[44]  # 当日均价
            self.ActionDay          = fields[45]  # 业务日期
        except Exception, e:
            print e.message
            #print "except: 解析数据异常. RecvTime: %s" %(RecvTime)
            raise CTPRecordException("解析数据异常")

#############################################################
class ModelResult:
    IGNORE      = 0  # 忽略，不作处理的模型信号
    BUY         = 1  # 买入（做多）
    SELL        = 2  # 卖出（做空）
    CLOSE_ALL   = 3  # 全部清仓
    CANCEL_OPEN = 4  # 取消开仓单（等待中、未成交的开仓单）

def ModelResult2String(modelResult):
    if 0 == modelResult:
        return "IGNORE"
    elif 1 == modelResult:
        return "BUY"
    elif 2 == modelResult:
        return "SELL"
    elif 3 == modelResult:
        return "CLOSE_ALL"
    elif 4 == modelResult:
        return "CANCEL_OPEN"
    else:
        return "" 


