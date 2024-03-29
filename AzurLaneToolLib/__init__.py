#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL BY MATT BELFAST BROWN
__init__.py - The core part of the Azur Lane Tool.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2024-01-06
Version: 0.6.4

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

# import list
import AzurLaneToolLib.data.data_AZR_Lan as data_AZR_Lan
import AzurLaneToolLib.mode.mode_BlP_Cal as mode_BlP_Cal
import AzurLaneToolLib.mode.mode_CME_Cal as mode_CME_Cal
import AzurLaneToolLib.mode.mode_EXP_Cal as mode_EXP_Cal
import AzurLaneToolLib.mode.mode_FCS_Cal as mode_FCS_Cal
import AzurLaneToolLib.mode.mode_FLE_Tol as mode_FLE_Tol
import AzurLaneToolLib.mode.mode_KSN_Com as mode_KSN_Com
import AzurLaneToolLib.mode.mode_MSC_Cal as mode_MSC_Cal
import AzurLaneToolLib.mode.mode_SRS_Ptl as mode_SRS_Ptl

# information list
__title__ = "AzurLaneToolLib"
__version__ = "0.6.4"
__author__ = "Matt Belfast Brown"
__license__ = "GPL-3.0"
__copyright__ = "Copyright (c) 2020-2024 Matt Belfast Brown"
__all__ = ["mode", "data", "data_AZR_Lan", "mode_BlP_Cal", "mode_CME_Cal", "mode_EXP_Cal", "mode_FCS_Cal",
           "mode_FLE_Tol", "mode_MSC_Cal", "mode_KSN_Com", "mode_SRS_Ptl"]

# class list
FitCal = mode_SRS_Ptl.FitCal
KsenKeyGen = mode_SRS_Ptl.KsenKeyGen

# function list
fun_cnbp_rbpt = mode_BlP_Cal.fun_cnbp_rbpt
fun_cnbp_rqub = mode_BlP_Cal.fun_cnbp_rqub
fun_cnbp_rqup = mode_BlP_Cal.fun_cnbp_rqup
fun_cnbp_rrcl = mode_BlP_Cal.fun_cnbp_rrcl
fun_cnbp_tyfi = mode_BlP_Cal.fun_cnbp_tyfi
fun_berf_cmug = mode_CME_Cal.fun_berf_cmug
fun_evdb_cmul = mode_CME_Cal.fun_evdb_cmul
fun_cexp_vrfu = mode_EXP_Cal.fun_cexp_vrfu
fun_crex_cele = mode_EXP_Cal.fun_crex_cele
fun_bsdg_fuca = mode_FCS_Cal.fun_bsdg_fuca
fun_kstp_scco = mode_FCS_Cal.fun_kstp_scco
fun_sfks_fuca = mode_FCS_Cal.fun_sfks_fuca
fun_subd_fuco = mode_FCS_Cal.fun_subd_fuco
fun_maks_code = mode_FLE_Tol.fun_maks_code
fun_ksen_nmco = mode_KSN_Com.fun_ksen_nmco
fun_gain_valu = mode_SRS_Ptl.fun_gain_valu
fun_anel_algr = mode_SRS_Ptl.fun_anel_algr
fun_mkmt_data = mode_SRS_Ptl.fun_mkmt_data

# data list
dic_ksen_data = data_AZR_Lan.dic_ksen_data
