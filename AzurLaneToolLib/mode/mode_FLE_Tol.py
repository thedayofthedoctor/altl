#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This code file overwrite from `azurlanefleet` product by x94fujo6rpg, Licensed under the MIT License.
Copyright (C) 2021 x94fujo6rpg
Author: x94fujo6rpg

THIS FILE IS PART OF AZUR LANE TOOL BY MATT BELFAST BROWN
mode_FLE_Tol.py - The core mode of the Azur Lane Tool.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2024-01-06
Version: 0.6.4
Mode Create Date: 2022-10-18
Mode Date: 2023-03-04
Mode Version: 0.0.2

THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2024 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not,
see <http://www.gnu.org/licenses/>.
"""

from lzstring import LZString

from AzurLaneToolLib.data import data_AZR_Lan as data_AZR_Lan

comp_teur_comp = LZString.compressToEncodedURIComponent

dic_ship_data = data_AZR_Lan.dic_ksen_data


def fun_maks_code():
    list_ksdt = []
    stri_lskd = str(list_ksdt)
    kasn_code = comp_teur_comp(stri_lskd)
    return kasn_code
