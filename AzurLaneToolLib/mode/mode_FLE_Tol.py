#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

from lzstring import LZString
from AzurLaneToolLib.data import data_FLE_Shi as data_FLE_Shi

comp_teur_comp = LZString.compressToEncodedURIComponent

dic_ship_data = data_FLE_Shi.dic_ship_data


def fun_maks_code():
    list_ksdt = []
    stri_lskd = str(list_ksdt)
    kasn_code = comp_teur_comp(stri_lskd)
    return kasn_code
