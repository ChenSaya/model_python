#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jc_struct import ModelResult
from jc_struct import CTPMdRecord

#############################################################
# 模型计算类
#     只需实现Model类的ProcOneRecord()函数
class Model:
    def __init__(self):
        self.record_cnt = 0
        self.tick_list = []

    '''
    功能: 对Tick记录r做处理，进行模型计算，并返回模型计算结果
    参数：r为当前接收到的Tick的记录，r中各字段的定义请参考 jc_struct.CTPMdRecord）
    @return
        返回值必须是ModelResult中的枚举值
    '''
    def ProcOneRecord(self, r):
        self.record_cnt += 1

        # 如果需要，可按如下保存最近若干个Tick
        SAVE_TICK_CNT = 60 * 2 * 10  # 保存Tick的数目 
        self.tick_list.append(r)
        if len(self.tick_list) > SAVE_TICK_CNT:
            del self.tick_list[0]

        # r中各字段的定义请参考 jc_struct.CTPMdRecord
        LastPrice = r.LastPrice  # 最新价

        # 如下示例为每隔10个Tick交替发买/卖信号
        modelResult = ModelResult.IGNORE 
        if self.record_cnt % 10 == 0 and self.record_cnt % 20 != 0:
            modelResult = ModelResult.BUY
        elif self.record_cnt % 20 == 0:
            modelResult = ModelResult.SELL

        return modelResult
    


