#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL BY MATT BELFAST BROWN
mode_FCS_Cal.py - The core mode of the Azur Lane Tool.

Author:Matt Belfast Brown
Create Date:2021-07-10
Version Date:2022-01-30
Version:0.4.13
Mode Create Date:2020-05-27
Mode Date:2022-01-22
Mode Version:0.1.6

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
def fun_bsdg_fuca(vari_ksct, vari_rare, vari_brea, vari_ksnm):
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
    if vari_brea == 0:
        para_brco = 0
    elif vari_brea == 1:
        para_brco = 2
    elif vari_brea == 2:
        para_brco = 4
    elif vari_brea == 3:
        para_brco = 6
    vari_bofb = list_bofd[para_ksct]
    vari_raco = list_raco[para_raco]
    vari_brco = list_brco[para_brco]


# define list
list_bofd = [1, 2, 3, 4, 5, 6]
list_raco = [0, 1, 2, 3, 4]
list_brco = [0, 2, 4, 6]
list_spco = [7, 9]
list_scco = [-2, -1, 1]
