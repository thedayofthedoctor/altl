#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL BY MATT BELFAST BROWN
mode_FCS_Cal.py - The core mode of the Azur Lane Tool.

Author: Matt Belfast Brown
Create Date: 2021-07-10
Version Date: 2022-02-22
Version: 0.5.1
Mode Create Date: 2020-05-27
Mode Date: 2022-02-22
Mode Version: 0.5.0

THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2021-2022 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
'''
#define variable name
 variable-name chinese
 fun_sfks_fuca 函数-计算水面舰船油耗
 fun_smks_fuca 函数-计算潜艇油耗
 fun_bsdg_fuca 函数-计算基础满级油耗
 fun_smks_mfuc 函数-计算潜艇移动油耗
 vari_ksct     变量-舰船类别
 para_ksct     参数-舰船类别
 
 #
 DD：驱逐；CL：轻巡；CA：重巡；MN：浅水重炮舰；MT：维修舰；
 CVL：轻航；CV：航母；BC：战列巡洋舰；BB：战列舰 
 #
 
'''


# define import list

# define function
def fun_bsdg_fuca(vari_ksct: str, vari_rare: str, vari_ksnm: str) -> int:
    """

    """
    # 计算舰船类型补正 - para_ksct
    if vari_ksct == 'DD':
        para_ksct = 0
    elif vari_ksct in ['CL', 'MN', 'MT']:
        para_ksct = 1
    elif vari_ksct in ['CA', 'CVL']:
        para_ksct = 2
    elif vari_ksct == 'CV':
        para_ksct = 3
    elif vari_ksct == 'BC':
        para_ksct = 4
    elif vari_ksct == 'BB':
        para_ksct = 5
    else:
        para_ksct = 0
    # 计算稀有度补正 - para_raco
    if vari_rare == '普通':
        para_raco = 0
    elif vari_rare == '稀有':
        para_raco = 1
    elif vari_rare == '精锐':
        para_raco = 2
    elif vari_rare in ['超稀有', '最高方案']:
        para_raco = 3
    elif vari_rare in ['海上传奇', '决战方案']:
        para_raco = 4
    else:
        para_raco = 0
    vari_scco = fun_kstp_scco(vari_ksnm)
    vari_bofb = list_bofd[para_ksct]  # 船型基础油耗
    vari_raco = list_raco[para_raco]  # 稀有度油耗
    vari_dgfu = int(vari_bofb + vari_raco + vari_scco)  # 基础最终油耗（100级0破）
    return vari_dgfu


def fun_sfks_fuca(vari_brea: int, vari_ksct: str, vari_rare: str, vari_ksnm: str, vari_kslv: int) -> int:
    """

    """
    # 计算突破补正 - para_brco
    if vari_brea == 0:
        para_brco = 0
    elif vari_brea == 1:
        para_brco = 1
    elif vari_brea == 2:
        para_brco = 2
    elif vari_brea == 3:
        para_brco = 3
    else:
        para_brco = 0
    vari_brco = list_brco[para_brco]  # 突破度油耗
    vari_dgfu = fun_bsdg_fuca(vari_ksct, vari_rare, vari_ksnm)
    vari_sfkf = int(int(1 + (vari_dgfu * (0.5 + min(vari_kslv, 99)) * 0.05)) + vari_brco)
    return vari_sfkf


def fun_kstp_scco(para_ksnm: str) -> int:
    """

    """
    # 计算特殊补正
    if para_ksnm in ['夕张']:
        vari_scco = list_scco[0]
    elif para_ksnm in ['神风', '多塞特郡', '最上', '三隈', '三笠']:
        vari_scco = list_scco[1]
    elif para_ksnm in ['飞鹰', '隼鹰', '半人马', '金刚', '比叡', '天城']:
        vari_scco = list_scco[2]
    else:
        vari_scco = 0
    return vari_scco


# define list
list_bofd = [1, 2, 3, 4, 5, 6]
list_raco = [0, 1, 2, 3, 4]
list_brco = [0, 2, 4, 6]
list_spco = [7, 9]
list_scco = [-2, -1, 1]
list_scks = ['夕张', '神风', '多塞特郡', '最上', '三隈', '三笠', '飞鹰', '隼鹰', '半人马', '金刚', '比叡', '天城']
