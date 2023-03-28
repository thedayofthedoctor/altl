#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL BY MATT BELFAST BROWN
mode_BlP_Cal.py - The core mode of the Azur Lane Tool.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2023-03-28
Version: 0.7.0a1（5M3a1）
Mode Create Date: 2020-05-02
Mode Date: 2022-10-20
Mode Version: 1.1.4

THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2023 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not,
see <http://www.gnu.org/licenses/>.
"""


# define function list
def fun_cnbp_rqub(vari_plle: int) -> int:
    """
    此函数输入科研等级达到对应等级所需的蓝图数量。
    This function inputs the number of blueprints required to reach the corresponding level of scientific research.
    :param vari_plle: 变量 科研等级 variable level of plan
    :return: vari_bprb - 变量 升级所需基础蓝图数量 variable number of Basic Blueprint which Required for Upgrade
    """
    if 1 <= vari_plle <= 4 or 6 <= vari_plle <= 9 or 11 <= vari_plle <= 14:
        vari_bprb = 0.4 * vari_plle - 0.4 * (vari_plle % 5) + 2
    elif 16 <= vari_plle <= 19 or 21 <= vari_plle <= 24 or 26 <= vari_plle <= 29:
        vari_bprb = vari_plle - (vari_plle % 5) - 5
    elif vari_plle == 5:
        vari_bprb = 5
    elif vari_plle % 5 == 0:
        vari_bprb = int(-(vari_plle ** 3) / 375 + (vari_plle ** 2) / 5 - 2.9333 * vari_plle + 20)
    else:
        vari_bprb = 0
    return int(vari_bprb)


def fun_cnbp_rqup(flag_pltp: str, vari_plle: int) -> int:
    """
    此函数输入舰船科研类别与科研等级,输出升级所需蓝图数量.
    This function inputs the research type and research level of the ship, and outputs the number of blueprints required for
    the upgrade.
    :param flag_pltp: 舰船科研类别 包括 "Top Solution"(最高方案)和"Decisive Plan"(决战方案)两个参数.
    The ship research category includes  "Top Solution" and "Decisive Plan" parameters.
    :param vari_plle: 变量 科研等级 <Plan Level>
    :return: vari_bprq - 变量 升级所需蓝图数量 <Number of Blueprint which Required for Upgrade>
    """
    if flag_pltp == "Top Solution":
        vari_bprq = fun_cnbp_rqub(vari_plle)
    elif flag_pltp == "Decisive Plan":
        vari_bprq = int(fun_cnbp_rqub(vari_plle) * 1.5)
    else:
        vari_bprq = 0
    return vari_bprq


def fun_cnbp_rrcl(flag_pltp: str, vari_plde: int, vari_epbp: int, vari_lede: int, vari_levn: int) -> tuple[int, int]:
    """
    此函数输入下列五个参数输出非天运科研图纸需求数量以及已用图纸数量。
    This function inputs the following five parameters and outputs the required quantity of non-Tianyun scientific research
    drawings and the quantity of used blueprints.
    :param flag_pltp: 舰船科研类别 包括:"Top Solution"(最高方案)和"Decisive Plan"(决战方案)两个参数.
    The ship research category includes: "Top Solution" and "Decisive Plan" parameters.
    :param vari_plde: 已拥有未使用的蓝图数量. Already have the number of unused blueprints.
    :param vari_epbp: 本级已使用的蓝图数量. The number of blueprints used by this level.
    :param vari_lede: 需要升到的科研等级. The plan level which need.
    :param vari_levn: 目前的科研等级. The plan leve which had.
    :return:  vari_prbp, vari_tebp - 变量 科研图纸需求计算结果，变量 已用的总蓝图数.
    Calculation results of scientific blueprint requirements and the total number of blueprints used.
    """
    vari_tbpr = 0
    vari_tebp = 0
    for para_plle in range(vari_lede):
        vari_tbpr += fun_cnbp_rqup(flag_pltp, para_plle)
    for para_plee in range(vari_levn):
        vari_tebp += fun_cnbp_rqup(flag_pltp, para_plee)
    vari_tebp += vari_epbp
    vari_prbp = vari_tbpr - vari_plde - vari_tebp
    return vari_prbp, vari_tebp


def fun_cnbp_tyfi(flag_pltp: str, vari_tfdl: int, vari_tyfg: int, vari_crtf: int) -> tuple[int, int]:
    """
    此函数输入下列四个参数输出天运拟合总需蓝图数与天运拟合总用蓝图数.
    This function inputs the following four parameters and outputs the total number of blueprints required for the fitting of
    the sky and the total number of blueprints used for the fitting of the sky.
    :param flag_pltp: 舰船科研类别 包括:"Top Solution"(最高方案)和"Decisive Plan"(决战方案)两个参数.
    The ship research category includes: "Top Solution" and "Decisive Plan" parameters.
    :param vari_tfdl: 天运拟合现有等级. Tianyun fits existing grades.
    :param vari_tyfg: 天运拟合未使用蓝图数量. Number of unused blueprints.
    :param vari_crtf: 天运拟合目前经验值. Tianyun fits the current experience value.
    :return:vari_tbtf, vari_bpty - 天运拟合总需蓝图数，天运拟合总用蓝图数
    The total number of blueprints required for Tianyun fitting. The total number of blueprints required for Tianyun fitting.
    """
    vari_bpty = 0
    if flag_pltp == "Top Solution":
        for i in range(vari_tfdl):
            vari_bpty += list_fitt[i]
        vari_bpty += int((vari_crtf / 100) * list_fitt[vari_tfdl])
        vari_tbtf = 165 - vari_tyfg - vari_bpty
    elif flag_pltp == "Decisive Plan":
        for i in range(vari_tfdl):
            vari_bpty += list_fitd[i]
        vari_bpty += int((vari_crtf / 100) * list_fitt[vari_tfdl])
        vari_tbtf = 215 - vari_tyfg - vari_bpty
    else:
        vari_tbtf = 0
    return vari_tbtf, vari_bpty


def fun_cnbp_rbpt(
        flag_pltp: str, flag_pftf: str, vari_lede: int, vari_levn: int, vari_plde: int, vari_epbp: int, vari_tfdl: int,
        vari_tyfg: int,
        vari_crtf: int
        ) -> list:
    """
    此函数是集合函数，聚合上述函数内容的综合型函数.
    This function is an aggregate function, a comprehensive function that aggregates the contents of the above functions.
    :param flag_pltp: 舰船科研类别 包括:"Top Solution"(最高方案)和"Decisive Plan"(决战方案)两个参数.
    The ship research category includes: "Top Solution" and "Decisive Plan" parameters.
    :param flag_pftf: 是否计算天运拟合，包括 True 和 False 两个参数。
    Whether to calculate the luck fit, including two parameters True and False.
    :param vari_lede: 需要升到的科研等级. The plan level which need.
    :param vari_levn: 目前的科研等级. The plan leve which had.
    :param vari_plde: 已拥有未使用的蓝图数量. Already have the number of unused blueprints.
    :param vari_epbp: 本级已使用的蓝图数量. The number of blueprints used by this level.
    :param vari_tfdl: 天运拟合现有等级. Tianyun fits existing grades.
    :param vari_tyfg: 天运拟合未使用蓝图数量. Number of unused blueprints.
    :param vari_crtf: 天运拟合目前经验值. Tianyun fits the current experience value.
    :return: [vari_prbt, vari_tbpt, vari_prbp, vari_tebp, vari_tbtf,
            vari_bpty]
            列表，每项内容如下：[科研图纸需求含天运拟合,已用的总蓝图数含天运拟合,科研图纸需求计算结果,已用的总蓝图数,天运拟合总需蓝图数,天运拟合总用蓝图数]。
            list, each of which is as follows: [Scientific research drawing requirements include Tianyun fitting,
            the total number of blueprints used includes Tianyun fitting, the calculation result of scientific research
            drawing requirements, the total number of blueprints used, the total number of blueprints required for Tianyun
            fitting, and the total number of Tianyun fitting number of blueprints].
    """
    if flag_pftf:
        vari_tbtf, vari_bpty = fun_cnbp_tyfi(flag_pltp, vari_tfdl, vari_tyfg, vari_crtf)
    else:
        vari_tbtf, vari_bpty = 0, 0
    vari_prbp, vari_tebp = fun_cnbp_rrcl(flag_pltp, vari_plde, vari_epbp, vari_lede, vari_levn)
    vari_prbt = vari_prbp + vari_tbtf
    vari_tbpt = vari_tebp + vari_bpty
    return [vari_prbt, vari_tbpt, vari_prbp, vari_tebp, vari_tbtf,
            vari_bpty]


# define list
list_fitt = [10, 20, 30, 40, 65]
list_fitd = [20, 30, 40, 50, 75]
