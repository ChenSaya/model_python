#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jc_tcp_client import TcpClient
from jc_config     import JcTcpClientCfg
from jc_struct     import CTPMdRecord, CTPRecordException, ModelResult, ModelResult2String
from model_example import Model

#############################################################
'''
定义自己的数据处理函数
完成自己的数据存储，模型计算等逻辑
@return 
    返回一个字符串（一行），作为模型结果返回给TcpTrader
    如果返回的是空串，则不返回给TcpTrader
'''
def my_data_processor(line):
    try:
        r = CTPMdRecord(line)

        global model
        modelResult = model.ProcOneRecord(r)

        if ModelResult.IGNORE == modelResult:
            return ""
        else:
            '''
            # 返回数据的各字段以\t分隔
            # 第一列是固定公共标志字段: ToJeactpTrader_ModelResult
            # 第二列是个人验证码，请保持与Trader配置文件中的验证码一致
            # 第三列是模型结果
            # 第四列是合约ID
            # 第五列是最新行情数据的接收时间
            # 第六列是价格类型 PriceType
            '''
            print "[%s] modelResult: %s" %(r.RecvTime, ModelResult2String(modelResult))
            checkCode1 = "ToJeactpTrader_ModelResult"
            checkCode2 = JcTcpClientCfg.checkCode2
            priceType = 0  # 默认价格类型 JeactpPriceType_CfgDefault
            return "%s\t%s\t%d\t%s\t%s\t%d" %(checkCode1, checkCode2, modelResult, r.InstrumentID, r.RecvTime, priceType)
    except CTPRecordException, e:
        print "except: 解析数据异常. line: " + line
        print e.message
    except Exception, e:
        print "except: 模型计算异常"
        print e.message

    return ""

#############################################################

if __name__ == "__main__":
    model = Model()  # 模型计算对象

    tcpClient = TcpClient(JcTcpClientCfg.ip, JcTcpClientCfg.port);
    tcpClient.SetDataProcessor(my_data_processor)  # 指定数据处理的回调函数
    tcpClient.Run()

    print "end."

