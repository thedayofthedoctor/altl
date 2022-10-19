#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This data file is the important part for Azur Lane Tool Lib, the python lib in Pypi.
It is from `azurlanekeyan` product by tianqianzhiyang, Licensed under the Mulan PSL V2.
Copyright (C) 2022 tianqianzhiyang
Author: tianqianzhiyang
bilibili: https://space.bilibili.com/337285187/
url: https://gitee.com/iamtianqianzhiyang/azurelanekeyan

THIS FILE IS PART OF AZUR LANE TOOL BY MATT BELFAST BROWN
mode_SRS_Pyl.py - The core code part of the Azur Lane Tool.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2022-10-20
Version: 0.6.0
Mode Create Date: 2020-10-13
Mode Date: 2022-10-20
Mode Version: 0.0.3

THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2022 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import copy
import random


# define class
class KsenGene:
    # define internal implementation of class
    def __init__(self, main_data: list):
        """
        This implementation sets the main parameters of the Kansen plan.
        此实现方案对舰船计划部分主要参数进行设定。
        :param main_data: 列表 元数据 list main data
        """
        self.gene_kfir = [0, 0, 0, 0, 0]  # 省物资0，省魔方1，缺心智2，金：彩3，彩：装备4
        self.gene_ksec = [0, 0, 0, 0, 0]  # 省物资5，省魔方6，缺心智7，金：彩8，彩：装备9
        self.gene_kthi = [0, 0, 0, 0, 0]  # 省物资10，省魔方11，缺心智12，金：彩13，彩：装备14
        self.numb_chge = [1, 2, 4, 8, 16, 32, -1, -2, -4, -8, -16, -32]
        self.data_maxn = [1024, 1024, 64, 256, 256]
        self.mtrl_work = 1  # 物资
        self.mdcb_work = 1  # 心智魔方
        self.mtut_work = 1  # 心智单元
        self.list_cnvt = []
        if main_data[31][1] == 0:
            self.mtrl_work = 0
        if main_data[32][1] == 0:
            self.mdcb_work = 0
        if main_data[36][1] == 0:
            self.mtut_work = 0
        for para_numb in range(15):
            if para_numb == 0 or para_numb == 5 or para_numb == 10:
                if self.mtrl_work == 0:
                    continue
            if para_numb == 1 or para_numb == 6 or para_numb == 11:
                if self.mdcb_work == 0:
                    continue
            if para_numb == 2 or para_numb == 7 or para_numb == 12:
                if self.mtut_work == 0:
                    continue
            if para_numb == 8 or para_numb == 13 or para_numb == 14:
                continue
            self.list_cnvt.append(copy.deepcopy(para_numb))
        self.numb_lcvt = len(self.list_cnvt) - 1

    def iic_gnew_rand(self):
        """
        This implementation sets the random parameters of the Kansen plan.
        此实现方案对舰船计划随机参数进行设定。
        """
        for numb_rang in range(5):
            if numb_rang == self.mtrl_work == 0:
                continue
            if numb_rang == 1 and self.mdcb_work == 0:
                continue
            if numb_rang == 2 and self.mtut_work == 0:
                continue
            self.gene_kfir[numb_rang] = random.randint(0, self.data_maxn[numb_rang])
            if numb_rang == 3:
                continue
            self.gene_ksec[numb_rang] = random.randint(0, self.data_maxn[numb_rang])
            if numb_rang == 4:
                continue
            self.gene_kthi[numb_rang] = random.randint(0, self.data_maxn[numb_rang])

