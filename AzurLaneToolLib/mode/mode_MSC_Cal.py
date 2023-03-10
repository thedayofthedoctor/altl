#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS Mode OF AZUR LANE TOOL BY MATT BELFAST BROWN
mode_MSC.py - The core mode of the Azur Lane Tool.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2023-03-11
Version: 0.6.4
Mode Create Date: 2023-03-11
Mode Date: 2023-03-11
Mode Version: 0.0.1α1

THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2023 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A ModeICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
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
