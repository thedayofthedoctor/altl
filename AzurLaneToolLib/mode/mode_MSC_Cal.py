#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS Mode OF AZUR LANE TOOL BY MATT BELFAST BROWN
mode_MSC.py - The core mode of the Azur Lane Tool.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2024-01-06
Version: 0.6.4
Mode Create Date: 2023-03-11
Mode Date: 2024-01-06
Mode Version: 0.0.2

THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2024 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A ModeICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not,
see <http://www.gnu.org/licenses/>.
"""


# define import list

# define function list
def fun_kexp_bcyd(numb_lvcm: int, numb_comf: int, numb_ksen: int, para_fsra: float) -> int:
    """
    This function is used to calculate the obtained value of experience in the backyard.
    :param para_fsra: 变量 食物补正比率 variable food supplement ratio
    :param numb_comf: 变量 后宅舒适值 variable value of backyard comfort
    :param numb_lvcm: 变量 指挥官等级 variable value of level of commander
    :param numb_ksen: 变量 舰船数目 variable number of Kansen
    :return: vari_expg - 变量 后宅综合经验值(每舰船每小时) variable comprehensive experience value per Kansen per hour
    """
    list_kncr = [0, 1, 1.8, 2.4, 2.8, 3.2, 3.6]
    vari_expg = (240 + numb_lvcm * 12)
    vari_expg *= (1 + para_fsra)
    vari_expg *= (1 + (numb_comf / (numb_comf + 100)))
    vari_expg *= (1 + para_fsra)
    vari_expg *= (list_kncr[numb_ksen] / numb_ksen)
    vari_expg = int(vari_expg)
    return vari_expg


# 好感度计算

# 舰队综合实力
# 结算经验值
"""def fun_figt_expg(stri_succ: str, leve_emot: int, ):
    dic_succ_leve = {"S": 1.2, "A": 1.0, "B": 0.8}
"""


# 演习经验值
# 指挥官经验
def fun_cman_expg(numb_ksen: int, stri_succ: str, numb_lvcm: int, stri_btcp: str, vari_hard: int) -> int:
    list_bexp = [20, 27, 35, 42.5, 49.5, 57.5, 65, 72.5]
    dic_succ_leve = {"S": 1.2, "A": 1.0, "B": 0.8}
    dic_beat_chap = {
        "1-1": [1, 2], "1-2": [3, 4], "1-3": [5, 6], "1-4": [8, 10], "2-1": [11, 12], "2-2": [14, 15],
        "2-3": [17, 18], "2-4": [20, 21], "3-1": [23, 24], "3-2": [26, 27], "3-3": [29, 30], "3-4": [32, 33],
        "4-1": [35, 36], "4-2": [38, 39], "4-3": [41, 42], "4-4": [44, 45], "5-1": [47, 48], "5-2": [50, 51],
        "5-3": [53, 54], "5-4": [56, 57], "6-1": [59, 60], "6-2": [62, 63], "6-3": [65, 66], "6-4": [68, 69],
        "7-1": [71, 72], "7-2": [73, 74], "7-3": [75, 76], "7-4": [77, 78], "8-1": [79, 80], "8-2": [81, 82],
        "8-3": [83, 84], "8-4": [85, 86], "9-1": [88, 89], "9-2": [90, 91], "9-3": [92, 93], "9-4": [94, 95],
        "10-1": [95, 96], "10-2": [97, 98], "10-3": [99, 100], "10-4": [101, 102], "11-1": [103, 104],
        "11-2": [104, 105], "11-3": [105, 106], "11-4": [106, 107], "12-1": [107, 108], "12-2": [109, 110],
        "12-3": [111, 112], "12-4": [113, 114], "13-1": [115, 116], "13-2": [117, 118], "13-3": [119, 120],
        "13-4": [121, 122]
        }
    para_leve = dic_beat_chap[stri_btcp][vari_hard]
    if numb_lvcm - para_leve > 40:
        para_vlec = 0.1
    elif 20 < numb_lvcm - para_leve <= 40:
        para_vlec = 0.5
    else:
        para_vlec = 1
    para_bcex = list_bexp[numb_ksen - 2]
    para_succ = dic_succ_leve[stri_succ]
    vari_cexp = para_bcex * para_succ * para_vlec
    return vari_cexp
