#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This data file is the important part for Azur Lane Tool Lib, the python lib in Pypi.
It is from `azurlanekeyan` product by tianqianzhiyang, Licensed under the Mulan PSL V2.
Copyright (C) 2022 tianqianzhiyang
Author: tianqianzhiyang
bilibili: https://space.bilibili.com/337285187/
git_url: https://gitee.com/iamtianqianzhiyang/azurelanekeyan

THIS FILE IS PART OF AZUR LANE TOOL BY MATT BELFAST BROWN
mode_SRS_Pyl.py - The core code part of the Azur Lane Tool.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2023-03-04
Version: 0.6.1β2
Mode Create Date: 2020-10-13
Mode Date: 2023-03-04
Mode Version: 0.1.0α1

THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2023 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU keygral Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU keygral Public License for more details.
You should have received a copy of the GNU keygral Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import copy
import random


# define class
class KsenKeyGen:
    # define internal implementation of class
    def __init__(self, meta_data: list):
        """
        This implementation sets the main parameters of the Kansen plan.
        此实现方案对舰船计划部分主要参数进行设定。
        :param meta_data: 列表 元数据 - list main data
        """
        self.keyg_kfir = [0, 0, 0, 0, 0]  # 省物资0，省魔方1，缺心智2，金：彩3，彩：装备4
        self.keyg_ksec = [0, 0, 0, 0, 0]  # 省物资5，省魔方6，缺心智7，金：彩8，彩：装备9
        self.keyg_kthi = [0, 0, 0, 0, 0]  # 省物资10，省魔方11，缺心智12，金：彩13，彩：装备14
        self.lsch_numb = [1, 2, 4, 8, 16, 32, -1, -2, -4, -8, -16, -32]
        self.data_maxn = [1024, 1024, 64, 256, 256]
        self.mtrl_work = 1  # 物资
        self.mdcb_work = 1  # 心智魔方
        self.mtut_work = 1  # 心智单元
        self.list_cnvt = []
        if meta_data[31][1] == 0:
            self.mtrl_work = 0
        if meta_data[32][1] == 0:
            self.mdcb_work = 0
        if meta_data[36][1] == 0:
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
            self.keyg_kfir[numb_rang] = random.randint(0, self.data_maxn[numb_rang])
            if numb_rang == 3:
                continue
            self.keyg_ksec[numb_rang] = random.randint(0, self.data_maxn[numb_rang])
            if numb_rang == 4:
                continue
            self.keyg_kthi[numb_rang] = random.randint(0, self.data_maxn[numb_rang])

    def iic_cont_itrt(self):
        """
        This implementation scheme preliminarily assigns the Kansen plan attributes.
        此实现方案对科研属性进行初步赋值。
        """
        numb_cnvt = random.choice(self.list_cnvt)
        numb_chge = random.choice(self.lsch_numb)
        if numb_cnvt < 5:
            self.keyg_kfir[numb_cnvt] = numb_chge + self.keyg_kfir[numb_cnvt]
            if self.keyg_kfir[numb_cnvt] < 0:
                self.keyg_kfir[numb_cnvt] = 0
        elif 5 <= numb_cnvt < 10:
            numb_cnvt -= 5
            self.keyg_ksec[numb_cnvt] = numb_chge + self.keyg_ksec[numb_cnvt]
            if self.keyg_ksec[numb_cnvt] < 0:
                self.keyg_ksec[numb_cnvt] = 0
        else:
            numb_cnvt -= 10
            self.keyg_kthi[numb_cnvt] = numb_chge + self.keyg_kthi[numb_cnvt]
            if self.keyg_kthi[numb_cnvt] < 0:
                self.keyg_kthi[numb_cnvt] = 0


class FitCal:
    # define internal implementation of class
    def __init__(self, meta_data):
        self.list_valu = [[0, 0, 0, 0, 0] for _ in range(29)]  # 总消耗, 总产出, 预期收益, 出现概率, 消耗时间
        self.list_rank = [i for i in range(29)]  # 冒泡排序列表
        self.valu_kfir = [0, 0, 0, 1.5, 1]  # 第一阶段参数 - 物资, 魔方, 心智, 金:彩, 彩:装备
        self.valu_ksec = [0, 0, 0, 1.5, 1]  # 第二阶段参数 - 物资, 魔方, 心智, 金:彩, 彩:装备
        self.valu_kthi = [0, 0, 0, 1.5, 1]  # 第三阶段参数 - 物资, 魔方, 心智, 金:彩, 彩:装备
        self.mthd_mtrl = meta_data[31][1]  # 物资限制方式
        self.numb_mtrl = meta_data[31][2]  # 物资限制数目
        self.mthd_mdcb = meta_data[32][1]  # 魔方限制方式
        self.numb_mdcb = meta_data[32][2]  # 魔方限制数目
        self.mthd_kssr = meta_data[33][1]  # 金船限制方式
        self.numb_kssr = meta_data[33][2]  # 金船限制数目
        self.mthd_ksur = meta_data[34][1]  # 彩船限制方式
        self.numb_ksur = meta_data[34][2]  # 彩船限制数目
        self.mthd_tcur = meta_data[35][1]  # 彩装限制方式
        self.numb_tcur = meta_data[35][2]  # 彩装限制数目
        self.mthd_mtut = meta_data[36][1]  # 心智限制方式
        self.numb_mtut = meta_data[36][2]  # 心智限制方式
        self.numb_hssr = meta_data[38][1]  # 金船已有数目
        self.numb_hpur = meta_data[39][1]  # 彩船已有数目
        self.list_pssr = [1524, 1524]  # 金船各期科研总需值
        self.list_prur = [1456, 1456]  # 彩船各期科研总需值
        self.para_incp = 0  # 初始性价比
        # self.para_cope = 0  # 方案性价比
        self.valu_tfir = 1500  # 时间参数值1
        self.valu_tsec = 0  # 时间参数值2
        self.incm_pint = 100  # 方案评分
        self.valu_filt = 5  # 初始过滤值
        self.numb_urse = 0  # 金船结束时彩船
        self.valu_mtrl = 0  # 物资消耗参数值
        self.valu_mdcb = 0  # 魔方消耗参数值
        self.valu_kssr = 0  # 金船图纸参数值
        self.valu_ksur = 0  # 彩船图纸参数值
        self.valu_tcur = 0  # 彩装蓝图参数值
        self.valu_mtut = 0  # 心智单元参数值
        self.numb_nssr = 0  # 金船图纸现需值
        self.numb_neur = 0  # 彩船图纸现需值
        self.time_ssrn = 0  # 金船所需时长
        self.time_urne = 0  # 彩船所需时长
        self.aver_mtrl = 0  # 日均物资消耗参数值
        self.aver_mdcb = 0  # 日均魔方消耗参数值
        # self.aver_ssrg = 0  #
        # self.aver_urga = 0  #

    def iir_outp_base(self, list_outp):
        if self.numb_urse < self.numb_neur:
            self.time_urne = (self.numb_neur - self.numb_urse) / list_outp[1][4]

    def iir_cuin_calc(self, meta_sval, meta_data, curr_stag: int):
        """收益计算"""
        self.valu_mtrl = meta_sval[0] / 200  # 物资
        self.valu_mdcb = meta_sval[1] * 10  # 魔方
        self.valu_mtut = meta_sval[2] * 0.6  # 心智
        if curr_stag == 0:
            self.valu_kssr = 1000
            self.valu_ksur = self.valu_kssr * meta_sval[3]
            self.valu_tcur = self.valu_ksur * meta_sval[4]
        elif curr_stag == 1:
            self.valu_kssr = 0
            self.valu_ksur = self.valu_kssr * meta_sval[3]
            self.valu_tcur = self.valu_ksur * meta_sval[4]
            para_medi = meta_data[10][2]
            meta_data[10][2] = 0
            meta_data[14][2] += para_medi
            para_medi = meta_data[11][2]
            meta_data[11][2] = 0
            meta_data[15][2] += para_medi
            para_medi = meta_data[12][2]
            meta_data[12][2] = 0
            meta_data[16][2] += para_medi
            para_medi = meta_data[13][2]
            meta_data[13][2] = 0
            meta_data[17][2] += para_medi
        elif curr_stag == 2:
            self.valu_kssr = 0
            self.valu_ksur = 1
            self.valu_tcur = 100000
        else:
            self.valu_kssr = 0
            self.valu_ksur = 0
            self.valu_tcur = 0
        para_numb = 0  # 用于循环的参数
        while para_numb <= 20:
            for numb_time in range(29):
                rows_numb = numb_time + 2  # 行号
                totl_cost = totl_outp = 0  # 总消耗量 = 总产出量
                totl_cost += meta_data[rows_numb][1] * self.valu_tfir + self.valu_tsec  # 时间消耗
                totl_cost += meta_data[rows_numb][3] * self.valu_mtrl  # 物资消耗
                totl_cost += meta_data[rows_numb][4] * self.valu_mdcb  # 魔方消耗
                totl_outp += meta_data[rows_numb][5] * self.valu_kssr  # 金船图纸产出
                totl_outp += meta_data[rows_numb][6] * self.valu_ksur  # 彩船图纸产出
                totl_outp += meta_data[rows_numb][7] * self.valu_tcur  # 彩装蓝图产出
                totl_outp += meta_data[rows_numb][8] * self.valu_mtut  # 心智单元产出
                totl_outp *= meta_data[rows_numb][1]
                self.list_valu[numb_time][0] = totl_cost
                self.list_valu[numb_time][1] = totl_outp
                self.list_valu[numb_time][2] = totl_outp - self.para_incp * totl_cost
                self.list_valu[numb_time][3] = meta_data[rows_numb][2]
                self.list_valu[numb_time][4] = meta_data[rows_numb][1]
            for numb_sort in range(29):  # 利用冒泡排序方法排列
                for para_sort in range(28):
                    if self.list_valu[para_sort][2] < self.list_valu[para_sort + 1][2]:
                        self.list_rank[para_sort] = para_sort + 1
                        self.list_rank[para_sort + 1] = para_sort
                    else:
                        continue
            dic_daly_fopa = self.iir_earn_fore(meta_data)
            para_itcp = dic_daly_fopa["cope_rafp"]  # 循环的性价比
            # para_dtcp = dic_daly_fopp["dlcp_rafp"]  # 循环的日性价比
            # list_foda = dic_daly_fopp["daly_foda"]  # 循环的日预测数据
            para_numb += 1
            if para_itcp == self.para_incp:
                break
            else:
                self.para_incp = para_itcp
        while True:
            self.valu_filt += 1
            dic_daly_fopr = self.iir_earn_fore(meta_data)
            para_itcr = dic_daly_fopr["cope_rafp"]  # 迭代循环的性价比
            # para_dtcr = dic_daly_fopr["dlcp_rafp"]  # 迭代循环的日性价比
            # list_fodr = dic_daly_fopr["daly_foda"]  # 迭代循环的日预测数据
            if self.para_incp < para_itcr:
                dic_daly_fopp = copy.deepcopy(dic_daly_fopr)
                continue
            else:
                self.valu_filt -= 1
                dic_daly_fopp = self.iir_earn_fore(meta_data)
                break
        para_filt = self.valu_filt
        self.valu_filt = 5
        dic_eoop_pday = dic_daly_fopp
        dic_eoop_pday["lift_coma"] = para_filt  # 迭代循环使用的过滤参量
        return dic_eoop_pday

    def iir_earn_fore(self, meta_data):
        """收益预测"""
        vari_plpr = meta_data[37][1]
        list_sefr = []  # 被选取的频率列表
        vari_proc = 1  # 剩余目标出现概率
        vari_rsra = 1  # 可供选择的比例5
        para_esra = 0  # 预计选取的比例
        time_cost = 0  # 时间消耗量
        vari_toco = 0  # 总消耗量
        vari_toop = 0  # 总产出量
        for numb_balc in range(29):
            numb_rank = self.list_rank[numb_balc]  # 循环数
            para_basp = self.list_valu[numb_rank][3]  # p0 基础概率
            para_prtp = para_basp / vari_proc
            if 8 <= numb_rank <= 15:
                para_aprp = para_prtp * vari_plpr
            else:
                para_aprp = para_prtp / 4
            para_prob = 1 - (1 - para_prtp) ** 3 * (1 - para_aprp) ** 2
            para_pobs = para_prob * vari_rsra  # 选择的概率
            list_sefr.append([para_pobs, 0])
            vari_proc -= para_basp
            vari_rsra -= para_pobs
            vari_toco += para_pobs * self.list_valu[numb_rank][0]
            vari_toop += para_pobs * self.list_valu[numb_rank][1]
            time_cost += para_pobs * self.list_valu[numb_rank][4]
            if numb_balc <= self.valu_filt:
                para_esra += para_pobs
            else:
                continue
        para_incp = vari_toop / vari_toco  # 预测用性价比
        para_rtim = 24 / time_cost  # 科研选取次数
        para_pnbs = 1 - para_esra  # 预计不会选择的概率
        para_unfr = 1 - pow(para_esra, para_rtim)  # 预计不会占用的概率空间
        para_fifp = (para_pnbs * para_rtim - para_unfr * para_esra) / para_rtim  # 选取非真值的概率
        para_fisp = 1 - para_fifp  # 选取真值的概率
        para_toco = para_toop = para_coti = 0
        list_dldt = [0, 0, 0, 0, 0, 0, 0]  # 物资, 魔方, 间隔, 金图, 彩图, 彩装, 心智
        for para_rank in range(29):
            rank_numb = self.list_rank[para_rank]  # 项目序号
            rows_numb = rank_numb + 2
            para_pobs = list_sefr[para_rank][0]  # 选取的概率
            if para_rank <= self.valu_filt:
                para_poss = (para_pobs / para_esra) * para_fisp
            else:
                para_poss = (para_pobs / para_pnbs) * para_fifp
            list_sefr[para_rank][1] = para_poss
            para_toco += self.list_valu[rank_numb][0] * para_poss  # 当前总消耗
            para_toop += self.list_valu[rank_numb][1] * para_poss  # 当前总产出
            para_coti += self.list_valu[rank_numb][4] * para_poss  # 当前总耗时
            list_dldt[0] += meta_data[rows_numb][1] * para_poss  # 日常消耗时间
            list_dldt[1] += meta_data[rows_numb][3] * para_poss  # 日常物资消耗
            list_dldt[2] += meta_data[rows_numb][4] * para_poss  # 日常魔方消耗
            list_dldt[3] += meta_data[rows_numb][1] * meta_data[rows_numb][5] * para_poss  # 每日金图产出
            list_dldt[4] += meta_data[rows_numb][1] * meta_data[rows_numb][6] * para_poss  # 每日彩图产出
            list_dldt[5] += meta_data[rows_numb][1] * meta_data[rows_numb][7] * para_poss  # 每日彩装产出
            list_dldt[6] += meta_data[rows_numb][1] * meta_data[rows_numb][8] * para_poss  # 每日心智产出
        para_reti = 24 / para_coti  # 每日科研的次数
        for numb_dldt in range(7):
            if numb_dldt == 2:
                list_dldt[numb_dldt] *= 5
            else:
                list_dldt[numb_dldt] *= para_reti
        para_dlcp = para_toop / para_toco  # 预测用每日性价比
        dic_daly_fore = {"cope_rafp": para_incp, "dlcp_rafp": para_dlcp, "daly_foda": list_dldt}
        return dic_daly_fore

    def iir_calu_baio(self, vari_plpe, clas_gene, meta_data):
        """基础收益产出"""
        self.valu_kfir = fun_gain_valu(clas_gene.keyg_kfir)  # 第一阶段参数 - 物资, 魔方, 心智, 金:彩, 彩:装备
        self.valu_ksec = fun_gain_valu(clas_gene.keyg_ksec)  # 第二阶段参数 - 物资, 魔方, 心智, 金:彩, 彩:装备
        self.valu_kthi = fun_gain_valu(clas_gene.keyg_kthi)  # 第三阶段参数 - 物资, 魔方, 心智, 金:彩, 彩:装备
        dic_oupt_firs = self.iir_cuin_calc(self.valu_kfir, meta_data, 0)  # 第一阶段基础产出
        dic_oupt_seco = self.iir_cuin_calc(self.valu_ksec, meta_data, 1)  # 第二阶段基础产出
        dic_oupt_thir = self.iir_cuin_calc(self.valu_kthi, meta_data, 2)  # 第三阶段基础产出
        list_oupt = [dic_oupt_firs, dic_oupt_seco, dic_oupt_thir]  # 基础产出列表
        para_evsc = self.iir_fitn_calc(vari_plpe, list_oupt)  # 基础收益产出计算
        return para_evsc

    def iir_gain_opls(self, vari_plpe, list_oupt):
        """计算收益产出列表"""
        self.numb_nssr = self.list_pssr[vari_plpe] - self.numb_hssr  # 金船现需求数
        self.numb_neur = self.list_prur[vari_plpe] - self.numb_hpur  # 彩船现需求数
        self.time_ssrn = self.numb_nssr / list_oupt[0]["daly_foda"][3]  # 金船所需时长
        self.numb_urse = self.time_ssrn * list_oupt[0]["daly_foda"][4]  # 金船结束时彩船的需求数
        if self.numb_urse < self.numb_neur:
            self.time_urne = (self.numb_neur - self.numb_urse) / list_oupt[0]["daly_foda"][4]  # 彩船所需时长
        else:
            self.time_urne = 0
        if self.time_ssrn <= 365:
            self.valu_mtrl += self.time_ssrn * list_oupt[0]["daly_foda"][0]  # 物资消耗参数值
            self.valu_mdcb += self.time_ssrn * list_oupt[0]["daly_foda"][1]  # 魔方消耗参数值
            self.valu_tcur += self.time_ssrn * list_oupt[0]["daly_foda"][5]  # 彩装蓝图参数值
            self.valu_mtut += self.time_ssrn * list_oupt[0]["daly_foda"][6]  # 心智单元参数值
            if self.time_ssrn + self.time_urne <= 365:
                self.valu_mtrl += self.time_urne * list_oupt[1]["daly_foda"][0]
                self.valu_mtrl += (365 - self.time_ssrn - self.time_urne) * list_oupt[2]["daly_foda"][0]
                self.valu_mdcb += self.time_urne * list_oupt[1]["daly_foda"][1]
                self.valu_mdcb += (365 - self.time_ssrn - self.time_urne) * list_oupt[2]["daly_foda"][1]
                self.valu_tcur += self.time_urne * list_oupt[1]["daly_foda"][5]
                self.valu_tcur += (365 - self.time_ssrn - self.time_urne) * list_oupt[2]["daly_foda"][5]
                self.valu_mtut += self.time_urne * list_oupt[1]["daly_foda"][6]
                self.valu_mtut += (365 - self.time_ssrn - self.time_urne) * list_oupt[2]["daly_foda"][6]
            else:
                self.valu_mtrl += (365 - self.time_urne) * list_oupt[1]["daly_foda"][0]
                self.valu_mdcb += (365 - self.time_urne) * list_oupt[1]["daly_foda"][1]
                self.valu_tcur += (365 - self.time_urne) * list_oupt[1]["daly_foda"][5]
                self.valu_mtut += (365 - self.time_urne) * list_oupt[1]["daly_foda"][6]
        else:
            self.valu_mtrl += 365 * list_oupt[0]["daly_foda"][0]
            self.valu_mdcb += 365 * list_oupt[0]["daly_foda"][1]
            self.valu_tcur += 365 * list_oupt[0]["daly_foda"][5]
            self.valu_mtut += 365 * list_oupt[0]["daly_foda"][6]
        self.aver_mtrl = self.valu_mtrl / 365
        self.aver_mdcb = self.valu_mtrl / 365
        self.time_urne += self.time_ssrn

    def iir_fitn_calc(self, vari_plpe, list_oupt):
        """适应度计算"""
        self.numb_tcur *= 50
        vari_evsc = self.incm_pint
        self.iir_gain_opls(vari_plpe, list_oupt)
        para_pont = 0
        para_dvsr = 1
        if self.mthd_mtrl == 2:  # 物资消耗限制
            para_pont += (40000 - self.aver_mtrl) / 70
            para_dvsr *= 1
        elif self.mthd_mtrl == 1:
            para_pont += 0
            if self.numb_mtrl <= self.aver_mtrl:
                para_dvsr *= (1 + (self.aver_mtrl - self.numb_mtrl) * 0.001)
            else:
                para_dvsr *= 1
        else:
            para_pont += 0
            para_dvsr *= 1
        if self.mthd_mdcb == 2:  # 魔方消耗限制
            para_pont += (60 - self.aver_mdcb) * 6
            para_dvsr *= 1
        elif self.mthd_mdcb == 1:
            para_pont += 0
            if self.numb_mdcb <= self.aver_mdcb:
                para_dvsr *= (1 + (self.aver_mdcb - self.numb_mdcb))
            else:
                para_dvsr *= 1
        else:
            para_pont += 0
            para_dvsr *= 1
        if self.mthd_kssr == 2:  # 金船图纸限制
            para_pont += (365 - self.time_ssrn)
            para_dvsr *= 1
        elif self.mthd_kssr == 1:
            para_pont += 0
            if self.numb_kssr <= self.time_ssrn:
                para_dvsr *= (1 + (self.time_ssrn - self.numb_kssr) * 20)
            else:
                para_dvsr *= 1
        else:
            para_pont += 0
            para_dvsr *= 0
        if self.mthd_ksur == 2:  # 彩船图纸限制
            para_pont += (365 - self.time_urne)
            para_dvsr *= 1
        elif self.mthd_ksur == 1:
            para_pont += 0
            if self.numb_ksur <= self.time_urne:
                para_dvsr *= (1 + (self.time_urne - self.numb_ksur) * 30)
            else:
                para_dvsr *= 1
        else:
            para_pont += 0
            para_dvsr *= 1
        if self.mthd_tcur == 2:  # 彩装蓝图限制
            para_pont += self.valu_tcur
            para_dvsr *= 1
        elif self.mthd_tcur == 1:
            para_pont += 0
            if self.valu_tcur <= self.numb_ksur:
                para_dvsr *= (1 + (self.numb_ksur - self.valu_tcur) * 400)
            else:
                para_dvsr *= 1
        else:
            para_pont += 0
            para_dvsr *= 1
        if self.mthd_mtut == 2:  # 心智单元限制
            para_pont += self.valu_mtut / 180
            para_dvsr *= 1
        elif self.mthd_mtut == 1:
            para_pont += 0
            if self.valu_mtut <= self.numb_mtut:
                para_dvsr *= (1 + (self.valu_mtut - self.numb_mtut) * 0.5)
            else:
                para_dvsr *= 1
        else:
            para_pont += 0
            para_dvsr *= 1
        self.numb_urse = 0  # 重置彩剩余参数
        self.valu_mtrl = 0  # 重置物资参数值
        self.valu_mdcb = 0  # 重置魔方参数值
        self.valu_kssr = 0  # 重置金图纸参数
        self.valu_ksur = 0  # 重置彩图纸参数
        self.valu_tcur = 0  # 重置彩蓝图参数
        self.valu_mtut = 0  # 重置心智参数值
        self.numb_nssr = 0  # 重置金图纸现需
        self.numb_neur = 0  # 重置彩图纸现需
        self.time_ssrn = 0  # 重置金船需时长
        self.time_urne = 0  # 重置彩船需时长
        self.aver_mtrl = 0  # 重置日物资参数
        self.aver_mdcb = 0  # 重置日魔方参数
        return vari_evsc


def fun_gain_valu(lsit_keyg):
    meta_valu = [0, 0, 0, 1.5, 1]
    meta_valu[0] += 0.5 * lsit_keyg[0]
    meta_valu[1] += 0.5 * lsit_keyg[1]
    meta_valu[2] += 0.1 * lsit_keyg[2]
    meta_valu[3] += 0.5 * lsit_keyg[3]
    meta_valu[4] += 2 * lsit_keyg[4]
    return meta_valu


def fun_mkmt_data():
    """
    This function is going to make a list for save the data.
    此函数用于生成储存数据的列表。
    :return: list_mida 列表 存储数据的列表 - list the list which the data save.
    """
    list_mida = []
    list_mdda = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numb_rows = 1
    while numb_rows <= 40:
        list_mida.append(list_mdda)
        numb_rows += 1
    return list_mida
