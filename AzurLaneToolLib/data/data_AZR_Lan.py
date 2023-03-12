#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL BY MATT BELFAST BROWN
data_AZR_Lan.py - The core data part of the Azur Lane Tool.

This file"s data comes from `Azur Lane Fleet Tool`(https://github.com/x94fujo6rpg/AzurLaneFleet) by x94fujo6rpg licensed
under MIT License and `Azur Lane Chinese Wiki` (https://wiki.biligame.com/blhx/%E9%A6%96%E9%A1%B5) licensed under CC BY-NC-SA
3.0

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2023-03-11
Version: 0.6.4
Data Create Date: 2022-10-18
Data Version Date: 2023-03-05
Data Version: 0.2.2

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

#  The software is designed to provide functions for Azur Lane Tools.
#  Copyright (C) 2019-2023 Matt Belfast Brown
#  Copyright (c) 2023.
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

dic_ksen_natl = {  # 舰船阵营代码
    "64000": {"vari_ntid": 64000, "zhcn_name": "其他", "zhtw_name": "其他", "engb_name": "Other", "jajp_name": "その他"},
    "64001": {
        "vari_ntid": 64001, "zhcn_name": "白鹰", "zhtw_name": "白鷹", "engb_name": "Eagle Union",
        "jajp_name": "ユニオン"
        },
    "64002": {
        "vari_ntid": 64002, "zhcn_name": "皇家", "zhtw_name": "皇家", "engb_name": "Royal Navy",
        "jajp_name": "ロイヤル"
        },
    "64003": {
        "vari_ntid": 64003, "zhcn_name": "重樱", "zhtw_name": "重櫻", "engb_name": "Sakura Empire",
        "jajp_name": "重桜"
        },
    "64004": {
        "vari_ntid": 64004, "zhcn_name": "铁血", "zhtw_name": "鐵血", "engb_name": "Iron Blood",
        "jajp_name": "鉄血"
        },
    "64005": {
        "vari_ntid": 64005, "zhcn_name": "东煌", "zhtw_name": "東煌", "engb_name": "Dragon Empery",
        "jajp_name": "東煌"
        },
    "64006": {
        "vari_ntid": 64006, "zhcn_name": "撒丁帝国", "zhtw_name": "撒丁帝國", "engb_name": "Sardegna Empire",
        "jajp_name": "サディア"
        },
    "64007": {
        "vari_ntid": 64007, "zhcn_name": "北方联合", "zhtw_name": "北方聯合", "engb_name": "Northern Parliam",
        "jajp_name": "北連"
        },
    "64008": {
        "vari_ntid": 64008, "zhcn_name": "自由鸢尾", "zhtw_name": "自由鳶尾", "engb_name": "Iris Libre",
        "jajp_name": "アイリス"
        },
    "64009": {
        "vari_ntid": 64009, "zhcn_name": "维希教廷", "zhtw_name": "維希教廷", "engb_name": "Vichya Dominion",
        "jajp_name": "ヴィシア"
        },
    "64099": {"vari_ntid": 64099, "zhcn_name": "布里", "zhtw_name": "布里", "engb_name": "buli", "jajp_name": "ブイ"},
    "64100": {"vari_ntid": 64100, "zhcn_name": "META", "zhtw_name": "META", "engb_name": "META", "jajp_name": "META"},
    "64901": {
        "vari_ntid": 64901, "zhcn_name": "海王星", "zhtw_name": "海王星", "engb_name": "Neptune",
        "jajp_name": "海王星"
        },
    "64902": {
        "vari_ntid": 64903, "zhcn_name": "哔哩哔哩", "zhtw_name": "嗶哩嗶哩", "engb_name": "bilibili",
        "jajp_name": "ビリビリ"
        },
    "64903": {
        "vari_ntid": 64903, "zhcn_name": "传颂之物", "zhtw_name": "傳頌之物", "engb_name": "Utawarerumono",
        "jajp_name": "うたわれるもの"
        },
    "64904": {
        "vari_ntid": 64904, "zhcn_name": "绊爱", "zhtw_name": "絆愛", "engb_name": "KizunaAI",
        "jajp_name": "絆愛"
        },
    "64905": {
        "vari_ntid": 64905, "zhcn_name": "hololive", "zhtw_name": "hololive", "engb_name": "hololive",
        "jajp_name": "hololive"
        },
    "64906": {
        "vari_ntid": 64906, "zhcn_name": "维纳斯假期", "zhtw_name": "維納斯假期", "engb_name": "Venus Vacation",
        "jajp_name": "アイドルマスター"
        },
    "64907": {
        "vari_ntid": 64907, "zhcn_name": "偶像大师", "zhtw_name": "偶像大師", "engb_name": " IDOLM@STER",
        "jajp_name": "hololive"
        },
    "64908": {
        "vari_ntid": 64908, "zhcn_name": "SSSS", "zhtw_name": "SSSS", "engb_name": "SSSS",
        "jajp_name": "SSSS"
        }
    }

dic_eqip_type = {  # 舰船装备代码
    "8501": {
        "vari_eqid": 8501, "zhcn_name": "驱逐炮", "zhtw_name": "驅逐砲", "engb_name": "DD Gun",
        "jajp_name": "駆逐砲"
        },
    "8502": {
        "vari_eqid": 8502, "zhcn_name": "轻巡炮", "zhtw_name": "輕巡砲", "engb_name": "CL Gun",
        "jajp_name": "軽巡砲"
        },
    "8503": {
        "vari_eqid": 8503, "zhcn_name": "重巡炮", "zhtw_name": "重巡砲", "engb_name": "CA Gun",
        "jajp_name": "重巡砲"
        },
    "8504": {
        "vari_eqid": 8504, "zhcn_name": "战列炮", "zhtw_name": "戰艦砲", "engb_name": "BB Gun",
        "jajp_name": "戦艦砲"
        },
    "8505": {
        "vari_eqid": 8505, "zhcn_name": "水面鱼雷", "zhtw_name": "水面魚雷", "engb_name": "Torpedoe",
        "jajp_name": "魚雷"
        },
    "8506": {
        "vari_eqid": 8506, "zhcn_name": "防空炮", "zhtw_name": "防空砲", "engb_name": "Anti-Air Gun",
        "jajp_name": "対空砲"
        },
    "8507": {
        "vari_eqid": 8507, "zhcn_name": "战斗机", "zhtw_name": "戰鬥機", "engb_name": "Fighter",
        "jajp_name": "戦闘機"
        },
    "8508": {
        "vari_eqid": 8508, "zhcn_name": "鱼雷机", "zhtw_name": "魚雷機", "engb_name": "Torpedo Bomber",
        "jajp_name": "攻撃機"
        },
    "8509": {
        "vari_eqid": 8509, "zhcn_name": "轰炸机", "zhtw_name": "轟炸機", "engb_name": "Dive Bomber",
        "jajp_name": "爆撃機"
        },
    "8510": {
        "vari_eqid": 8510, "zhcn_name": "设备", "zhtw_name": "設備", "engb_name": "Auxiliary",
        "jajp_name": "設備"
        },
    "8511": {
        "vari_eqid": 8511, "zhcn_name": "超巡炮", "zhtw_name": "超巡砲", "engb_name": "CB Gun",
        "jajp_name": "超巡砲"
        },
    "8512": {
        "vari_eqid": 8512, "zhcn_name": "水上机", "zhtw_name": "水上機", "engb_name": "Seaplane",
        "jajp_name": "水上機"
        },
    "8513": {
        "vari_eqid": 8513, "zhcn_name": "潜艇鱼雷", "zhtw_name": "潛艇用魚雷", "engb_name": "Submarine Torpedoe",
        "jajp_name": "潜水艦魚雷"
        },
    "8514": {
        "vari_eqid": 8514, "zhcn_name": "深水炸弹", "zhtw_name": "爆雷", "engb_name": "Depth Charge",
        "jajp_name": "爆雷"
        },
    "8515": {
        "vari_eqid": 8515, "zhcn_name": "反潜机", "zhtw_name": "反潛機", "engb_name": "ASW Bomber",
        "jajp_name": "対潜機"
        },
    "8517": {
        "vari_eqid": 8517, "zhcn_name": "直升机", "zhtw_name": "直升機", "engb_name": "ASW Helicopter",
        "jajp_name": "ヘリ"
        },
    "8518": {"vari_eqid": 8518, "zhcn_name": "货物", "zhtw_name": "貨物", "engb_name": "Cargo", "jajp_name": "積載"},
    "8520": {"vari_eqid": 8520, "zhcn_name": "导弹", "zhtw_name": "導彈", "engb_name": "Missile", "jajp_name": "ミサイル"}
    }

dic_ksen_type = {  # 舰船类型代码
    "801": {
        "ksen_tpid": "801", "zhcn_name": "潜艇", "zhtw_name": "潛艇", "engb_name": "Submarine",
        "jajp_name": "潜水艦", "pos": "sub"
        },
    "881": {
        "ksen_tpid": "881", "zhcn_name": "潜母", "zhtw_name": "潛母", "engb_name": "Submarine Carrier",
        "jajp_name": "潜水空母", "pos": "sub"
        },
    "100": {
        "ksen_tpid": "100", "zhcn_name": "驱逐", "zhtw_name": "驅逐", "engb_name": "Destroyer", "jajp_name": "駆逐",
        "pos": "front"
        },
    "370": {
        "ksen_tpid": "370", "zhcn_name": "航战", "zhtw_name": "航戰", "engb_name": "Battleship",
        "jajp_name": "航戰", "pos": "back"
        },
    "540": {
        "ksen_tpid": "540", "zhcn_name": "运输", "zhtw_name": "運輸", "engb_name": "Transport", "jajp_name": "運輸",
        "pos": "back"
        },
    "140": {
        "ksen_tpid": "140", "zhcn_name": "导驱", "zhtw_name": "導驅", "engb_name": "Missile Equipped Destroyer",
        "jajp_name": "ミサイル駆逐"
        },
    "210": {
        "ksen_tpid": "210", "zhcn_name": "轻巡", "zhtw_name": "輕巡", "engb_name": "Light Cruiser",
        "jajp_name": "軽巡", "pos": "front"
        },
    "220": {
        "ksen_tpid": "220", "zhcn_name": "重巡", "zhtw_name": "重巡", "engb_name": "Heavy Cruiser",
        "jajp_name": "重巡", "pos": "front"
        },
    "250": {
        "ksen_tpid": "250", "zhcn_name": "超巡", "zhtw_name": "超巡", "engb_name": "Large Cruiser",
        "jajp_name": "超巡", "pos": "front"
        },
    "302": {
        "ksen_tpid": "302", "zhcn_name": "战巡", "zhtw_name": "戰巡", "engb_name": "Battle Cruiser",
        "jajp_name": "巡洋戦艦", "pos": "back"
        },
    "300": {
        "ksen_tpid": "300", "zhcn_name": "战列", "zhtw_name": "戰列", "engb_name": "Battle Ship",
        "jajp_name": "戦艦", "pos": "back"
        },
    "710": {
        "ksen_tpid": "710", "zhcn_name": "轻航", "zhtw_name": "輕航", "engb_name": "Light Carrier",
        "jajp_name": "軽空母", "pos": "back"
        },
    "702": {
        "ksen_tpid": "702", "zhcn_name": "航母", "zhtw_name": "航母", "engb_name": "Aircraft Carrier",
        "jajp_name": "空母", "pos": "back"
        },
    "330": {
        "ksen_tpid": "330", "zhcn_name": "重炮", "zhtw_name": "重砲", "engb_name": "Monitor", "jajp_name": "砲艦",
        "pos": "back"
        },
    "510": {
        "ksen_tpid": "510", "zhcn_name": "维修", "zhtw_name": "維修", "engb_name": "Repair Ship",
        "jajp_name": "工作", "pos": "back"
        },
    "900": {"ksen_tpid": "900", "zhcn_name": "其他", "zhtw_name": "其他", "engb_name": "Other", "jajp_name": "その他"}
    }

dic_ksen_rari = {  # 舰船稀有度代码
    "6": {
        "ksen_raid": 6, "zhcn_name": "海上传奇", "zhtw_name": "海上傳奇", "engb_name": "Ultra Rare",
        "jajp_name": "UR"
        },
    "5": {"ksen_raid": 5, "zhcn_name": "超稀有", "zhtw_name": "超稀有", "engb_name": "SuperRare", "jajp_name": "SSR"},
    "4": {"ksen_raid": 4, "zhcn_name": "精锐", "zhtw_name": "精銳", "engb_name": "Elite", "jajp_name": "SR"},
    "3": {"ksen_raid": 3, "zhcn_name": "稀有", "zhtw_name": "稀有", "engb_name": "Rare", "jajp_name": "R"},
    "2": {"ksen_raid": 2, "zhcn_name": "普通", "zhtw_name": "普通", "engb_name": "Normal", "jajp_name": "N"}
    }

dic_ksen_data = {  # 舰船数据
    "2280000100": {
        "vari_ksid": 2280000100, "zhcn_name": "猎人", "zhtw_name": "獵人", "jajp_name": "ハンター",
        "engb_name": "Hunter", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年03月07日"
        },
    "2280000101": {
        "vari_ksid": 2280000101, "zhcn_name": "标枪改", "zhtw_name": "標槍改", "jajp_name": "ジャベリン改",
        "engb_name": "Javelin (Retrofit)", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年10月26日"
        },
    "2280000102": {
        "vari_ksid": 2280000102, "zhcn_name": "天后", "zhtw_name": "天后", "jajp_name": "ジュノー",
        "engb_name": "Juno", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000103": {
        "vari_ksid": 2280000103, "zhcn_name": "吸血鬼", "zhtw_name": "吸血鬼", "jajp_name": "ヴァンパイア",
        "engb_name": "Vampire", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年06月08日"
        },
    "2280000104": {
        "vari_ksid": 2280000104, "zhcn_name": "利安得改", "zhtw_name": "利安得改", "jajp_name": "リアンダー改",
        "engb_name": "Leander (Retrofit)", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年10月16日"
        },
    "2280000105": {
        "vari_ksid": 2280000105, "zhcn_name": "阿基里斯改", "zhtw_name": "阿基里斯改",
        "jajp_name": "アキリーズ改",
        "engb_name": "Achilles (Retrofit)", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年01月19日"
        },
    "2280000106": {
        "vari_ksid": 2280000106, "zhcn_name": "阿贾克斯改", "zhtw_name": "阿賈克斯改",
        "jajp_name": "エイジャックス改",
        "engb_name": "Ajax (Retrofit)", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年08月02日"
        },
    "2280000107": {
        "vari_ksid": 2280000107, "zhcn_name": "黛朵", "zhtw_name": "黛朵", "jajp_name": "ダイドー",
        "engb_name": "Dido", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年01月21日"
        },
    "2280000110": {
        "vari_ksid": 2280000110, "zhcn_name": "南安普顿", "zhtw_name": "南安普敦", "jajp_name": "サウサンプトン",
        "engb_name": "Southampton", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2019年06月"
        },
    "2280000111": {
        "vari_ksid": 2280000111, "zhcn_name": "谢菲尔德", "zhtw_name": "謝菲爾德", "jajp_name": "シェフィールド",
        "engb_name": "Sheffield", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月26日"
        },
    "2280000113": {
        "vari_ksid": 2280000113, "zhcn_name": "格罗斯特", "zhtw_name": "格洛斯特", "jajp_name": "グロスター",
        "engb_name": "Gloucester", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年01月21日"
        },
    "2280000114": {
        "vari_ksid": 2280000114, "zhcn_name": "爱丁堡", "zhtw_name": "愛丁堡", "jajp_name": "エディンバラ",
        "engb_name": "Edinburgh", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年07月06日"
        },
    "2280000115": {
        "vari_ksid": 2280000115, "zhcn_name": "贝尔法斯特", "zhtw_name": "貝爾法斯特", "jajp_name": "ベルファスト",
        "engb_name": "Belfast", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年07月06日"
        },
    "2280000116": {
        "vari_ksid": 2280000116, "zhcn_name": "阿瑞托莎", "zhtw_name": "阿瑞托莎", "jajp_name": "アリシューザ",
        "engb_name": "Arethusa", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000117": {
        "vari_ksid": 2280000117, "zhcn_name": "加拉蒂亚", "zhtw_name": "加拉蒂亞", "jajp_name": "ガラティア",
        "engb_name": "Galatea", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000118": {
        "vari_ksid": 2280000118, "zhcn_name": "欧若拉", "zhtw_name": "歐若拉", "jajp_name": "オーロラ",
        "engb_name": "Aurora", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月12日"
        },
    "2280000119": {
        "vari_ksid": 2280000119, "zhcn_name": "伦敦改", "zhtw_name": "倫敦改", "jajp_name": "ロンドン改",
        "engb_name": "London (Retrofit)", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86003], [86001, 86005], [86006], [86010], [86010]],
        "onln_date": "2019年07月18日"
        },
    "2280000120": {
        "vari_ksid": 2280000120, "zhcn_name": "什罗普郡", "zhtw_name": "什羅普郡", "jajp_name": "シュロップシャー",
        "engb_name": "Shropshire", "vari_rari": 3, "vari_kstp": "220", "vari_natl": 64002, "bool_retr": 1,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000121": {
        "vari_ksid": 2280000121, "zhcn_name": "肯特", "zhtw_name": "肯特", "jajp_name": "ケント",
        "engb_name": "Kent", "vari_rari": 3, "vari_kstp": "220", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000122": {
        "vari_ksid": 2280000122, "zhcn_name": "萨福克改", "zhtw_name": "薩福克改", "jajp_name": "サフォーク改",
        "engb_name": "Suffolk (Retrofit)", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86003], [86005], [86006], [86010], [86010]],
        "onln_date": "2017年07月06日"
        },
    "2280000123": {
        "vari_ksid": 2280000123, "zhcn_name": "诺福克", "zhtw_name": "諾福克", "jajp_name": "ノーフォーク",
        "engb_name": "Norfolk", "vari_rari": 3, "vari_kstp": "220", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000124": {
        "vari_ksid": 2280000124, "zhcn_name": "多塞特郡", "zhtw_name": "多塞特郡", "jajp_name": "ドーセットシャー",
        "engb_name": "Dorsetshire", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000125": {
        "vari_ksid": 2280000125, "zhcn_name": "约克改", "zhtw_name": "約克改", "jajp_name": "ヨーク改",
        "engb_name": "York (Retrofit)", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86003], [86005], [86006], [86010], [86010]],
        "onln_date": "2018年12月20日"
        },
    "2280000126": {
        "vari_ksid": 2280000126, "zhcn_name": "埃克塞特改", "zhtw_name": "埃克塞特改",
        "jajp_name": "エクセター改",
        "engb_name": "Exeter (Retrofit)", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86003], [86005], [86006], [86010], [86010]],
        "onln_date": "2018年01月19日"
        },
    "2280000127": {
        "vari_ksid": 2280000127, "zhcn_name": "声望", "zhtw_name": "聲望", "jajp_name": "レナウン",
        "engb_name": "Renown", "vari_rari": 4, "vari_kstp": "302", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000128": {
        "vari_ksid": 2280000128, "zhcn_name": "反击", "zhtw_name": "反擊", "jajp_name": "レパルス",
        "engb_name": "Repulse", "vari_rari": 3, "vari_kstp": "302", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000129": {
        "vari_ksid": 2280000129, "zhcn_name": "胡德", "zhtw_name": "胡德", "jajp_name": "フッド",
        "engb_name": "Hood", "vari_rari": 5, "vari_kstp": "302", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000130": {
        "vari_ksid": 2280000130, "zhcn_name": "伊丽莎白女王", "zhtw_name": "伊莉莎白女王",
        "jajp_name": "クイーン・エリザベス",
        "engb_name": "Queen Elizabeth", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]],
        "onln_date": "2017年05月25日"
        },
    "2280000131": {
        "vari_ksid": 2280000131, "zhcn_name": "厌战改", "zhtw_name": "厭戰改", "jajp_name": "ウォースパイト改",
        "engb_name": "Warspite (Retrofit)", "vari_rari": 6, "vari_kstp": "300", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86004], [86001, 86002], [86006], [86010, 86015], [86010]],
        "onln_date": "2019年01月31日"
        },
    "2280000132": {
        "vari_ksid": 2280000132, "zhcn_name": "纳尔逊", "zhtw_name": "納爾遜", "jajp_name": "ネルソン",
        "engb_name": "Nelson", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000133": {
        "vari_ksid": 2280000133, "zhcn_name": "罗德尼", "zhtw_name": "羅德尼", "jajp_name": "ロドニー",
        "engb_name": "Rodney", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000134": {
        "vari_ksid": 2280000134, "zhcn_name": "英王乔治五世", "zhtw_name": "英王喬治五世",
        "jajp_name": "キング・ジョージ5世",
        "engb_name": "King George V", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2019年05月23日"
        },
    "2280000135": {
        "vari_ksid": 2280000135, "zhcn_name": "威尔士亲王", "zhtw_name": "威爾斯親王",
        "jajp_name": "プリンス・オブ・ウェールズ",
        "engb_name": "Prince of Wales", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]],
        "onln_date": "2017年06月08日"
        },
    "2280000136": {
        "vari_ksid": 2280000136, "zhcn_name": "约克公爵", "zhtw_name": "約克公爵",
        "jajp_name": "デューク・オブ・ヨーク",
        "engb_name": "Duke of York", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2018年02月26日"
        },
    "2280000137": {
        "vari_ksid": 2280000137, "zhcn_name": "前卫", "zhtw_name": "前衛*", "jajp_name": "ヴァンガード",
        "engb_name": "Vanguard", "vari_rari": 6, "vari_kstp": "300", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2022年05月26日"
        },
    "2280000140": {
        "vari_ksid": 2280000140, "zhcn_name": "竞技神改", "zhtw_name": "競技神改", "jajp_name": "ハーミーズ改",
        "engb_name": "Hermes (Retrofit)", "vari_rari": 3, "vari_kstp": "701", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86008], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2019年05月09日"
        },
    "2280000142": {
        "vari_ksid": 2280000142, "zhcn_name": "独角兽改", "zhtw_name": "獨角獸改", "jajp_name": "ユニコーン改",
        "engb_name": "Unicorn (Retrofit)", "vari_rari": 5, "vari_kstp": "701", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2022年05月26日"
        },
    "2280000143": {
        "vari_ksid": 2280000143, "zhcn_name": "鹰", "zhtw_name": "鷹", "jajp_name": "イーグル",
        "engb_name": "Eagle", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86002, 86009], [86010], [86010]], "onln_date": "2020年07月23日"
        },
    "2280000144": {
        "vari_ksid": 2280000144, "zhcn_name": "皇家方舟改", "zhtw_name": "皇家方舟改",
        "jajp_name": "アーク・ロイヤル改",
        "engb_name": "Ark Royal (Retrofit)", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86008], [86008], [86009], [86010], [86010]],
        "onln_date": "2021年08月12日"
        },
    "2280000145": {
        "vari_ksid": 2280000145, "zhcn_name": "光辉", "zhtw_name": "光輝", "jajp_name": "イラストリアス",
        "engb_name": "Illustrious", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86007], [86007], [86008], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000146": {
        "vari_ksid": 2280000146, "zhcn_name": "胜利", "zhtw_name": "勝利", "jajp_name": "ヴィクトリアス",
        "engb_name": "Victorious", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2018年02月26日"
        },
    "2280000147": {
        "vari_ksid": 2280000147, "zhcn_name": "可畏", "zhtw_name": "可畏", "jajp_name": "フォーミダブル",
        "engb_name": "Formidable", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86007, 86009], [86008], [86008], [86010], [86010]], "onln_date": "2019年09月11日"
        },
    "2280000148": {
        "vari_ksid": 2280000148, "zhcn_name": "光荣", "zhtw_name": "光榮", "jajp_name": "グロリアス",
        "engb_name": "Glorious", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86008], [86010], [86010]], "onln_date": "2017年10月26日"
        },
    "2280000149": {
        "vari_ksid": 2280000149, "zhcn_name": "黑暗界", "zhtw_name": "黑暗界", "jajp_name": "エレバス",
        "engb_name": "Erebus", "vari_rari": 4, "vari_kstp": "330", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000150": {
        "vari_ksid": 2280000150, "zhcn_name": "恐怖", "zhtw_name": "恐怖", "jajp_name": "テラー",
        "engb_name": "Terror", "vari_rari": 4, "vari_kstp": "330", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000151": {
        "vari_ksid": 2280000151, "zhcn_name": "吹雪", "zhtw_name": "吹雪", "jajp_name": "吹雪",
        "engb_name": "Fubuki", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年12月07日"
        },
    "2280000152": {
        "vari_ksid": 2280000152, "zhcn_name": "白雪", "zhtw_name": "白雪*", "jajp_name": "白雪",
        "engb_name": "Shirayuki", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年06月24日"
        },
    "2280000155": {
        "vari_ksid": 2280000155, "zhcn_name": "绫波改", "zhtw_name": "綾波改", "jajp_name": "綾波改",
        "engb_name": "Ayanami (Retrofit)", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月12日"
        },
    "2280000159": {
        "vari_ksid": 2280000159, "zhcn_name": "晓", "zhtw_name": "曉", "jajp_name": "暁",
        "engb_name": "Akatsuki", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年09月28日"
        },
    "2280000160": {
        "vari_ksid": 2280000160, "zhcn_name": "响", "zhtw_name": "響", "jajp_name": "響",
        "engb_name": "Hibiki",
        "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年12月26日"
        },
    "2280000161": {
        "vari_ksid": 2280000161, "zhcn_name": "雷", "zhtw_name": "雷", "jajp_name": "雷",
        "engb_name": "Ikazuchi", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年07月14日"
        },
    "2280000162": {
        "vari_ksid": 2280000162, "zhcn_name": "电", "zhtw_name": "電", "jajp_name": "電",
        "engb_name": "Inazuma", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年07月14日"
        },
    "2280000163": {
        "vari_ksid": 2280000163, "zhcn_name": "白露", "zhtw_name": "白露", "jajp_name": "白露",
        "engb_name": "Shiratsuyu", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000164": {
        "vari_ksid": 2280000164, "zhcn_name": "夕立改", "zhtw_name": "夕立改", "jajp_name": "夕立改",
        "engb_name": "Yuudachi (Retrofit)", "vari_rari": 6, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年09月30日"
        },
    "2280000165": {
        "vari_ksid": 2280000165, "zhcn_name": "时雨改", "zhtw_name": "時雨改", "jajp_name": "時雨改",
        "engb_name": "Shigure (Retrofit)", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年09月26日"
        },
    "2280000166": {
        "vari_ksid": 2280000166, "zhcn_name": "雪风", "zhtw_name": "雪風", "jajp_name": "雪風",
        "engb_name": "Yukikaze", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年03月29日"
        },
    "2280000167": {
        "vari_ksid": 2280000167, "zhcn_name": "阳炎改", "zhtw_name": "陽炎改", "jajp_name": "陽炎改",
        "engb_name": "Kagerou (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年08月15日"
        },
    "2280000168": {
        "vari_ksid": 2280000168, "zhcn_name": "不知火改", "zhtw_name": "不知火改", "jajp_name": "不知火改",
        "engb_name": "Shiranui (Retrofit)", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年04月26日"
        },
    "2280000170": {
        "vari_ksid": 2280000170, "zhcn_name": "野分", "zhtw_name": "野分", "jajp_name": "野分",
        "engb_name": "Nowaki", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年09月28日"
        },
    "2280000171": {
        "vari_ksid": 2280000171, "zhcn_name": "初春改", "zhtw_name": "初春改", "jajp_name": "初春改",
        "engb_name": "Hatsuharu (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年12月26日"
        },
    "2280000173": {
        "vari_ksid": 2280000173, "zhcn_name": "若叶", "zhtw_name": "若葉", "jajp_name": "若葉",
        "engb_name": "Wakaba", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2018年01月"
        },
    "2280000174": {
        "vari_ksid": 2280000174, "zhcn_name": "初霜改", "zhtw_name": "初霜改", "jajp_name": "初霜改",
        "engb_name": "Hatsushimo (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年06月03日"
        },
    "2280000175": {
        "vari_ksid": 2280000175, "zhcn_name": "有明改", "zhtw_name": "有明改", "jajp_name": "有明改",
        "engb_name": "Ariake (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年09月30日"
        },
    "2280000176": {
        "vari_ksid": 2280000176, "zhcn_name": "夕暮改", "zhtw_name": "夕暮改", "jajp_name": "夕暮改",
        "engb_name": "Yuugure (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年09月26日"
        },
    "2280000177": {
        "vari_ksid": 2280000177, "zhcn_name": "黑潮", "zhtw_name": "黑潮", "jajp_name": "黒潮",
        "engb_name": "Kuroshio", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年12月01日"
        },
    "2280000178": {
        "vari_ksid": 2280000178, "zhcn_name": "亲潮", "zhtw_name": "親潮", "jajp_name": "親潮",
        "engb_name": "Oyashio", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年12月01日"
        },
    "2280000179": {
        "vari_ksid": 2280000179, "zhcn_name": "夕张改", "zhtw_name": "夕張改", "jajp_name": "夕張改",
        "engb_name": "Yuubari (Retrofit)", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年04月04日"
        },
    "2280000182": {
        "vari_ksid": 2280000182, "zhcn_name": "长良", "zhtw_name": "長良", "jajp_name": "長良",
        "engb_name": "Nagara", "vari_rari": 2, "vari_kstp": "210", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年09月08日"
        },
    "2280000183": {
        "vari_ksid": 2280000183, "zhcn_name": "五十铃改", "zhtw_name": "五十鈴改", "jajp_name": "五十鈴改",
        "engb_name": "Isuzu (Retrofit)", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年04月23日"
        },
    "2280000185": {
        "vari_ksid": 2280000185, "zhcn_name": "由良", "zhtw_name": "由良", "jajp_name": "由良",
        "engb_name": "Yura", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年09月16日"
        },
    "2280000186": {
        "vari_ksid": 2280000186, "zhcn_name": "鬼怒改", "zhtw_name": "鬼怒改", "jajp_name": "鬼怒改",
        "engb_name": "Kinu (Retrofit)", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年12月26日"
        },
    "2280000187": {
        "vari_ksid": 2280000187, "zhcn_name": "阿武隈改", "zhtw_name": "阿武隈改", "jajp_name": "阿武隈改",
        "engb_name": "Abukuma (Retrofit)", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年07月14日"
        },
    "2280000188": {
        "vari_ksid": 2280000188, "zhcn_name": "最上改", "zhtw_name": "最上改", "jajp_name": "最上改",
        "engb_name": "Mogami (Retrofit)", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86003], [86005], [86006], [86010], [86010]],
        "onln_date": "2018年03月29日"
        },
    "2280000189": {
        "vari_ksid": 2280000189, "zhcn_name": "三隈", "zhtw_name": "三隈", "jajp_name": "三隈",
        "engb_name": "Mikuma", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年03月29日"
        },
    "2280000190": {
        "vari_ksid": 2280000190, "zhcn_name": "古鹰改", "zhtw_name": "古鷹改", "jajp_name": "古鷹改",
        "engb_name": "Furutaka (Retrofit)", "vari_rari": 3, "vari_kstp": "220", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86003], [86005], [86006], [86010], [86010]],
        "onln_date": "2017年11月02日"
        },
    "2280000191": {
        "vari_ksid": 2280000191, "zhcn_name": "加古改", "zhtw_name": "加古改", "jajp_name": "加古改",
        "engb_name": "Kako (Retrofit)", "vari_rari": 3, "vari_kstp": "220", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86003], [86005], [86006], [86010], [86010]],
        "onln_date": "2017年11月02日"
        },
    "2280000192": {
        "vari_ksid": 2280000192, "zhcn_name": "青叶", "zhtw_name": "青葉", "jajp_name": "青葉",
        "engb_name": "Aoba", "vari_rari": 2, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年08月23日"
        },
    "2280000193": {
        "vari_ksid": 2280000193, "zhcn_name": "衣笠", "zhtw_name": "衣笠", "jajp_name": "衣笠",
        "engb_name": "Kinugasa", "vari_rari": 2, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年08月23日"
        },
    "2280000195": {
        "vari_ksid": 2280000195, "zhcn_name": "筑摩", "zhtw_name": "築摩", "jajp_name": "筑摩",
        "engb_name": "Chikuma", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2021年09月16日"
        },
    "2280000196": {
        "vari_ksid": 2280000196, "zhcn_name": "妙高", "zhtw_name": "妙高", "jajp_name": "妙高",
        "engb_name": "Myoukou", "vari_rari": 3, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年06月23日"
        },
    "2280000197": {
        "vari_ksid": 2280000197, "zhcn_name": "那智", "zhtw_name": "那智", "jajp_name": "那智",
        "engb_name": "Nachi", "vari_rari": 3, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年06月23日"
        },
    "2280000198": {
        "vari_ksid": 2280000198, "zhcn_name": "足柄", "zhtw_name": "足柄", "jajp_name": "足柄",
        "engb_name": "Ashigara", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2018年12月27日"
        },
    "2280000200": {
        "vari_ksid": 2280000200, "zhcn_name": "高雄", "zhtw_name": "高雄", "jajp_name": "高雄",
        "engb_name": "Takao", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000201": {
        "vari_ksid": 2280000201, "zhcn_name": "爱宕", "zhtw_name": "愛宕", "jajp_name": "愛宕",
        "engb_name": "Atago", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年06月08日"
        },
    "2280000202": {
        "vari_ksid": 2280000202, "zhcn_name": "摩耶", "zhtw_name": "摩耶", "jajp_name": "摩耶",
        "engb_name": "Maya", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年06月23日"
        },
    "2280000203": {
        "vari_ksid": 2280000203, "zhcn_name": "鸟海", "zhtw_name": "鳥海", "jajp_name": "鳥海",
        "engb_name": "Choukai", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2018年04月26日"
        },
    "2280000204": {
        "vari_ksid": 2280000204, "zhcn_name": "金刚", "zhtw_name": "金剛", "jajp_name": "金剛",
        "engb_name": "Kongou", "vari_rari": 4, "vari_kstp": "302", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2018年06月07日"
        },
    "2280000205": {
        "vari_ksid": 2280000205, "zhcn_name": "比叡", "zhtw_name": "比叡", "jajp_name": "比叡",
        "engb_name": "Hiei", "vari_rari": 4, "vari_kstp": "302", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2017年12月01日"
        },
    "2280000206": {
        "vari_ksid": 2280000206, "zhcn_name": "榛名", "zhtw_name": "榛名", "jajp_name": "榛名",
        "engb_name": "Haruna", "vari_rari": 4, "vari_kstp": "302", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2018年06月07日"
        },
    "2280000207": {
        "vari_ksid": 2280000207, "zhcn_name": "雾岛", "zhtw_name": "霧島", "jajp_name": "霧島",
        "engb_name": "Kirishima", "vari_rari": 4, "vari_kstp": "302", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2018年05月31日"
        },
    "2280000208": {
        "vari_ksid": 2280000208, "zhcn_name": "扶桑改", "zhtw_name": "扶桑改", "jajp_name": "扶桑改",
        "engb_name": "Fusou (Retrofit)", "vari_rari": 4, "vari_kstp": "370", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86004], [86007, 86008, 86009, 86012], [86006], [86010], [86010]],
        "onln_date": "2018年05月10日"
        },
    "2280000209": {
        "vari_ksid": 2280000209, "zhcn_name": "山城改", "zhtw_name": "山城改", "jajp_name": "山城改",
        "engb_name": "Yamashiro (Retrofit)", "vari_rari": 4, "vari_kstp": "370", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86004], [86007, 86008, 86009, 86012], [86006], [86010], [86010]],
        "onln_date": "2017年09月28日"
        },
    "2280000210": {
        "vari_ksid": 2280000210, "zhcn_name": "伊势改", "zhtw_name": "伊勢改", "jajp_name": "伊勢改",
        "engb_name": "Ise (Retrofit)", "vari_rari": 4, "vari_kstp": "370", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86004], [86007, 86008, 86009, 86012], [86006], [86010], [86010]],
        "onln_date": "2018年08月30日"
        },
    "2280000211": {
        "vari_ksid": 2280000211, "zhcn_name": "日向改", "zhtw_name": "日向改", "jajp_name": "日向改",
        "engb_name": "Hyuuga (Retrofit)", "vari_rari": 4, "vari_kstp": "370", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86004], [86007, 86008, 86009, 86012], [86006], [86010], [86010]],
        "onln_date": "2018年08月30日"
        },
    "2280000212": {
        "vari_ksid": 2280000212, "zhcn_name": "长门", "zhtw_name": "長門", "jajp_name": "長門",
        "engb_name": "Nagato", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2018年06月07日"
        },
    "2280000213": {
        "vari_ksid": 2280000213, "zhcn_name": "陆奥", "zhtw_name": "陸奧", "jajp_name": "陸奧",
        "engb_name": "Mutsu", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2018年06月07日"
        },
    "2280000214": {
        "vari_ksid": 2280000214, "zhcn_name": "纪伊", "zhtw_name": "紀伊", "jajp_name": "紀伊",
        "engb_name": "Kii",
        "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2020年09月17日"
        },
    "2280000215": {
        "vari_ksid": 2280000215, "zhcn_name": "土佐", "zhtw_name": "土佐", "jajp_name": "土佐",
        "engb_name": "Tosa", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2020年04月23日"
        },
    "2280000218": {
        "vari_ksid": 2280000218, "zhcn_name": "飞鹰", "zhtw_name": "飛鷹", "jajp_name": "飛鷹",
        "engb_name": "Hiyou", "vari_rari": 3, "vari_kstp": "701", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010, 86015], [86010, 86015]],
        "onln_date": "2018年04月26日"
        },
    "2280000219": {
        "vari_ksid": 2280000219, "zhcn_name": "隼鹰", "zhtw_name": "隼鷹", "jajp_name": "隼鷹",
        "engb_name": "Junyou", "vari_rari": 3, "vari_kstp": "701", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010, 86015], [86010, 86015]],
        "onln_date": "2018年04月26日"
        },
    "2280000220": {
        "vari_ksid": 2280000220, "zhcn_name": "凤翔", "zhtw_name": "鳳翔", "jajp_name": "鳳翔",
        "engb_name": "Houshou", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86002], [86007], [86008], [86010, 86015], [86010, 86015]],
        "onln_date": "2017年05月25日"
        },
    "2280000222": {
        "vari_ksid": 2280000222, "zhcn_name": "祥凤改", "zhtw_name": "祥鳳改", "jajp_name": "祥鳳改",
        "engb_name": "Shouhou (Retrofit)", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86009], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2017年09月28日"
        },
    "2280000223": {
        "vari_ksid": 2280000223, "zhcn_name": "龙骧", "zhtw_name": "龍驤", "jajp_name": "龍驤",
        "engb_name": "Ryuujou", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2018年12月20日"
        },
    "2280000224": {
        "vari_ksid": 2280000224, "zhcn_name": "赤城", "zhtw_name": "赤城", "jajp_name": "赤城",
        "engb_name": "Akagi", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000225": {
        "vari_ksid": 2280000225, "zhcn_name": "加贺", "zhtw_name": "加賀", "jajp_name": "加賀",
        "engb_name": "Kaga", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000226": {
        "vari_ksid": 2280000226, "zhcn_name": "苍龙改", "zhtw_name": "蒼龍改", "jajp_name": "蒼龍改",
        "engb_name": "Souryuu (Retrofit)", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86007], [86009], [86008], [86010], [86010]],
        "onln_date": "2018年12月27日"
        },
    "2280000227": {
        "vari_ksid": 2280000227, "zhcn_name": "飞龙改", "zhtw_name": "飛龍改", "jajp_name": "飛龍改",
        "engb_name": "Hiryuu (Retrofit)", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86007], [86009], [86008], [86010], [86010]],
        "onln_date": "2018年12月27日"
        },
    "2280000228": {
        "vari_ksid": 2280000228, "zhcn_name": "翔鹤", "zhtw_name": "翔鶴", "jajp_name": "翔鶴",
        "engb_name": "Shoukaku", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2017年09月28日"
        },
    "2280000229": {
        "vari_ksid": 2280000229, "zhcn_name": "瑞鹤", "zhtw_name": "瑞鶴", "jajp_name": "瑞鹤",
        "engb_name": "Zuikaku", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2017年09月28日"
        },
    "2280000230": {
        "vari_ksid": 2280000230, "zhcn_name": "大凤", "zhtw_name": "大鳳", "jajp_name": "大鳳",
        "engb_name": "Taihou", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2018年09月14日"
        },
    "2280000231": {
        "vari_ksid": 2280000231, "zhcn_name": "信浓", "zhtw_name": "信濃", "jajp_name": "信濃",
        "engb_name": "Shinano", "vari_rari": 6, "vari_kstp": "702", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007, 86008, 86009], [86009], [86008], [86010], [86010]],
        "onln_date": "2020年09月17日"
        },
    "2280000232": {
        "vari_ksid": 2280000232, "zhcn_name": "明石", "zhtw_name": "明石", "jajp_name": "明石",
        "engb_name": "Akashi", "vari_rari": 5, "vari_kstp": "510", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86010], [86006], [86006], [86010], [86010]], "onln_date": "2017年08月02日"
        },
    "2280000233": {
        "vari_ksid": 2280000233, "zhcn_name": "Z1改", "zhtw_name": "Z1改", "jajp_name": "Z1改",
        "engb_name": "Z1 (Retrofit)", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年06月06日"
        },
    "2280000236": {
        "vari_ksid": 2280000236, "zhcn_name": "Z23改", "zhtw_name": "Z23改", "jajp_name": "Z23改",
        "engb_name": "Z23 (Retrofit)", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64004,
        "bool_retr": 0, "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年06月07日"
        },
    "2280000237": {
        "vari_ksid": 2280000237, "zhcn_name": "Z25", "zhtw_name": "Z25", "jajp_name": "Z25",
        "engb_name": "Z25", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年06月28日"
        },
    "2280000238": {
        "vari_ksid": 2280000238, "zhcn_name": "柯尼斯堡", "zhtw_name": "柯尼斯堡", "jajp_name": "ケーニヒスベルク",
        "engb_name": "Königsberg", "vari_rari": 2, "vari_kstp": "210", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000239": {
        "vari_ksid": 2280000239, "zhcn_name": "卡尔斯鲁厄改", "zhtw_name": "卡爾斯魯厄改",
        "jajp_name": "カールスルーエ改",
        "engb_name": "Karlsruhe (Retrofit)", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64004,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年12月29日"
        },
    "2280000240": {
        "vari_ksid": 2280000240, "zhcn_name": "科隆改", "zhtw_name": "科隆改", "jajp_name": "ケルン改",
        "engb_name": "Köln (Retrofit)", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64004,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014, 86017], [86010, 86014]],
        "onln_date": "2019年05月23日"
        },
    "2280000241": {
        "vari_ksid": 2280000241, "zhcn_name": "莱比锡改", "zhtw_name": "萊比錫改", "jajp_name": "ライプツィヒ改",
        "engb_name": "Leipzig (Retrofit)", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64004,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年06月06日"
        },
    "2280000242": {
        "vari_ksid": 2280000242, "zhcn_name": "希佩尔海军上将", "zhtw_name": "希佩爾將軍",
        "jajp_name": "アドミラル・ヒッパー",
        "engb_name": "Admiral Hipper", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64004,
        "bool_retr": 0, "type_equp": [[86003], [86005], [86006], [86010], [86010]],
        "onln_date": "2017年08月02日"
        },
    "2280000244": {
        "vari_ksid": 2280000244, "zhcn_name": "欧根亲王", "zhtw_name": "歐根親王", "jajp_name": "プリンツ・オイゲン",
        "engb_name": "Prinz Eugen", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000245": {
        "vari_ksid": 2280000245, "zhcn_name": "德意志", "zhtw_name": "德意志", "jajp_name": "ドイッチュラント",
        "engb_name": "Deutschland", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86003, 86011], [86005], [86006], [86010], [86010]], "onln_date": "2017年08月02日"
        },
    "2280000246": {
        "vari_ksid": 2280000246, "zhcn_name": "斯佩伯爵海军上将", "zhtw_name": "施佩伯爵將軍",
        "jajp_name": "アドミラル・グラーフ・シュペー", "engb_name": "Admiral Graf Spee", "vari_rari": 4, "vari_kstp": "220",
        "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86003, 86011], [86005], [86006], [86010], [86010]], "onln_date": "2018年01月19日"
        },
    "2280000248": {
        "vari_ksid": 2280000248, "zhcn_name": "沙恩霍斯特", "zhtw_name": "沙恩霍斯特",
        "jajp_name": "シャルンホルスト",
        "engb_name": "Scharnhorst", "vari_rari": 4, "vari_kstp": "302", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2017年08月02日"
        },
    "2280000249": {
        "vari_ksid": 2280000249, "zhcn_name": "格奈森瑙", "zhtw_name": "格奈森瑙", "jajp_name": "グナイゼナウ",
        "engb_name": "Gneisenau", "vari_rari": 4, "vari_kstp": "302", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2017年08月02日"
        },
    "2280000250": {
        "vari_ksid": 2280000250, "zhcn_name": "俾斯麦", "zhtw_name": "俾斯麥", "jajp_name": "ビスマルク",
        "engb_name": "Bismarck", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2019年05月23日"
        },
    "2280000251": {
        "vari_ksid": 2280000251, "zhcn_name": "提尔比茨", "zhtw_name": "鐵必制", "jajp_name": "ティルピッツ",
        "engb_name": "Tirpitz", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2017年08月02日"
        },
    "2280000252": {
        "vari_ksid": 2280000252, "zhcn_name": "齐柏林伯爵", "zhtw_name": "齊柏林伯爵",
        "jajp_name": "グラーフ・ツェッペリン",
        "engb_name": "Graf Zeppelin", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008, 86009], [86010], [86010]], "onln_date": "2017年08月02日"
        },
    "2280000253": {
        "vari_ksid": 2280000253, "zhcn_name": "鞍山改", "zhtw_name": "鞍山改", "jajp_name": "鞍山改",
        "engb_name": "An Shan (Retrofit)", "vari_rari": 5, "vari_kstp": "140", "vari_natl": 64005,
        "bool_retr": 0, "type_equp": [[86001], [86020], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年01月27日"
        },
    "2280000254": {
        "vari_ksid": 2280000254, "zhcn_name": "抚顺", "zhtw_name": "撫順", "jajp_name": "撫順",
        "engb_name": "Fu Shun", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64005, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月12日"
        },
    "2280000255": {
        "vari_ksid": 2280000255, "zhcn_name": "长春改", "zhtw_name": "長春改", "jajp_name": "長春改",
        "engb_name": "Chang Chun (Retrofit)", "vari_rari": 5, "vari_kstp": "140", "vari_natl": 64005,
        "bool_retr": 0, "type_equp": [[86001], [86020], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年01月27日"
        },
    "2280000256": {
        "vari_ksid": 2280000256, "zhcn_name": "太原", "zhtw_name": "太原", "jajp_name": "太原",
        "engb_name": "Tai Yuan", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64005, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月12日"
        },
    "2280000257": {
        "vari_ksid": 2280000257, "zhcn_name": "逸仙", "zhtw_name": "逸仙", "jajp_name": "逸仙",
        "engb_name": "Yat Sen", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64005, "bool_retr": 0,
        "type_equp": [[86002], [86002], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年09月20日"
        },
    "2280000258": {
        "vari_ksid": 2280000258, "zhcn_name": "宁海改", "zhtw_name": "寧海改", "jajp_name": "寧海改",
        "engb_name": "Ning Hai (Retrofit)", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64005,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年12月13日"
        },
    "2280000259": {
        "vari_ksid": 2280000259, "zhcn_name": "平海改", "zhtw_name": "平海改", "jajp_name": "平海改",
        "engb_name": "Ping Hai (Retrofit)", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64005,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年12月13日"
        },
    "2280000262": {
        "vari_ksid": 2280000262, "zhcn_name": "阿芙乐尔", "zhtw_name": "曙光", "jajp_name": "アヴローラ",
        "engb_name": "Avrora", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000263": {
        "vari_ksid": 2280000263, "zhcn_name": "贝利改", "zhtw_name": "貝利改", "jajp_name": "ベイリー改",
        "engb_name": "Bailey (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年01月19日"
        },
    "2280000264": {
        "vari_ksid": 2280000264, "zhcn_name": "Z19", "zhtw_name": "Z19", "jajp_name": "Z19",
        "engb_name": "Z19", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年08月02日"
        },
    "2280000265": {
        "vari_ksid": 2280000265, "zhcn_name": "Z20", "zhtw_name": "Z20", "jajp_name": "Z20",
        "engb_name": "Z20", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年08月02日"
        },
    "2280000266": {
        "vari_ksid": 2280000266, "zhcn_name": "Z21", "zhtw_name": "Z21", "jajp_name": "Z21",
        "engb_name": "Z21", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年08月02日"
        },
    "2280000267": {
        "vari_ksid": 2280000267, "zhcn_name": "Z46", "zhtw_name": "Z46", "jajp_name": "Z46",
        "engb_name": "Z46", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年08月02日"
        },
    "2280000268": {
        "vari_ksid": 2280000268, "zhcn_name": "岛风", "zhtw_name": "島風", "jajp_name": "島風",
        "engb_name": "Shimakaze", "vari_rari": 6, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年09月16日"
        },
    "2280000269": {
        "vari_ksid": 2280000269, "zhcn_name": "神风改", "zhtw_name": "神風改", "jajp_name": "神風改",
        "engb_name": "Kamikaze (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年03月15日"
        },
    "2280000270": {
        "vari_ksid": 2280000270, "zhcn_name": "松风改", "zhtw_name": "松風改", "jajp_name": "松風改",
        "engb_name": "Matsukaze (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年03月15日"
        },
    "2280000271": {
        "vari_ksid": 2280000271, "zhcn_name": "睦月改", "zhtw_name": "睦月改", "jajp_name": "睦月改",
        "engb_name": "Mutsuki (Retrofit)", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年06月21日"
        },
    "2280000272": {
        "vari_ksid": 2280000272, "zhcn_name": "如月改", "zhtw_name": "如月改", "jajp_name": "如月改",
        "engb_name": "Kisaragi (Retrofit)", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年04月26日"
        },
    "2280000274": {
        "vari_ksid": 2280000274, "zhcn_name": "卯月", "zhtw_name": "卯月", "jajp_name": "卯月",
        "engb_name": "Uzuki", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年12月07日"
        },
    "2280000276": {
        "vari_ksid": 2280000276, "zhcn_name": "水无月", "zhtw_name": "水無月", "jajp_name": "水無月",
        "engb_name": "Minazuki", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年11月16日"
        },
    "2280000277": {
        "vari_ksid": 2280000277, "zhcn_name": "文月", "zhtw_name": "文月", "jajp_name": "文月",
        "engb_name": "Fumizuki", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年06月07日"
        },
    "2280000278": {
        "vari_ksid": 2280000278, "zhcn_name": "长月", "zhtw_name": "長月", "jajp_name": "長月",
        "engb_name": "Nagatsuki", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2018年12月"
        },
    "2280000280": {
        "vari_ksid": 2280000280, "zhcn_name": "三日月", "zhtw_name": "三日月", "jajp_name": "三日月",
        "engb_name": "Mikazuki", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年11月16日"
        },
    "2280000286": {
        "vari_ksid": 2280000286, "zhcn_name": "海风", "zhtw_name": "海風", "jajp_name": "海風",
        "engb_name": "Umikaze", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年09月16日"
        },
    "2280000287": {
        "vari_ksid": 2280000287, "zhcn_name": "山风", "zhtw_name": "山風", "jajp_name": "山風",
        "engb_name": "Yamakaze", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年09月16日"
        },
    "2280000288": {
        "vari_ksid": 2280000288, "zhcn_name": "江风", "zhtw_name": "江風", "jajp_name": "江風",
        "engb_name": "Kawakaze", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年06月07日"
        },
    "2280000293": {
        "vari_ksid": 2280000293, "zhcn_name": "清波", "zhtw_name": "清波", "jajp_name": "清波",
        "engb_name": "Kiyonami", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2019年09月"
        },
    "2280000296": {
        "vari_ksid": 2280000296, "zhcn_name": "春月", "zhtw_name": "春月", "jajp_name": "春月",
        "engb_name": "Harutsuki", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年06月07日"
        },
    "2280000297": {
        "vari_ksid": 2280000297, "zhcn_name": "宵月", "zhtw_name": "宵月", "jajp_name": "宵月",
        "engb_name": "Yoizuki", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年06月07日"
        },
    "2280000299": {
        "vari_ksid": 2280000299, "zhcn_name": "拉德福特", "zhtw_name": "拉德福特", "jajp_name": "ラドフォード",
        "engb_name": "Radford", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年09月20日"
        },
    "2280000300": {
        "vari_ksid": 2280000300, "zhcn_name": "杰金斯", "zhtw_name": "傑金斯", "jajp_name": "ジェンキンス",
        "engb_name": "Jenkins", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年09月20日"
        },
    "2280000301": {
        "vari_ksid": 2280000301, "zhcn_name": "尼古拉斯改", "zhtw_name": "尼古拉斯改", "jajp_name": "ニコラス改",
        "engb_name": "Nicholas (Retrofit)", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年07月17日"
        },
    "2280000303": {
        "vari_ksid": 2280000303, "zhcn_name": "里士满", "zhtw_name": "里奇蒙", "jajp_name": "リッチモンド",
        "engb_name": "Richmond", "vari_rari": 2, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年09月08日"
        },
    "2280000304": {
        "vari_ksid": 2280000304, "zhcn_name": "火奴鲁鲁", "zhtw_name": "火奴魯魯", "jajp_name": "ホノルル",
        "engb_name": "Honolulu", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年11月16日"
        },
    "2280000305": {
        "vari_ksid": 2280000305, "zhcn_name": "圣路易斯", "zhtw_name": "聖路易斯", "jajp_name": "セントルイス",
        "engb_name": "St. Louis", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年11月16日"
        },
    "2280000306": {
        "vari_ksid": 2280000306, "zhcn_name": "丘比特", "zhtw_name": "丘比特", "jajp_name": "ジュピター",
        "engb_name": "Jupiter", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2017年10月"
        },
    "2280000307": {
        "vari_ksid": 2280000307, "zhcn_name": "泽西", "zhtw_name": "澤西", "jajp_name": "ジャージー",
        "engb_name": "Jersey", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2017年11月"
        },
    "2280000308": {
        "vari_ksid": 2280000308, "zhcn_name": "川内改", "zhtw_name": "川內改", "jajp_name": "川内改",
        "engb_name": "Sendai (Retrofit)", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年04月26日"
        },
    "2280000309": {
        "vari_ksid": 2280000309, "zhcn_name": "神通改", "zhtw_name": "神通改", "jajp_name": "神通改",
        "engb_name": "Jintsuu (Retrofit)", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年11月16日"
        },
    "2280000310": {
        "vari_ksid": 2280000310, "zhcn_name": "那珂", "zhtw_name": "那珂", "jajp_name": "那珂",
        "engb_name": "Naka", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年12月27日"
        },
    "2280000316": {
        "vari_ksid": 2280000316, "zhcn_name": "浦风", "zhtw_name": "浦風", "jajp_name": "浦風",
        "engb_name": "Urakaze", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2018年02月"
        },
    "2280000317": {
        "vari_ksid": 2280000317, "zhcn_name": "矶风", "zhtw_name": "磯風", "jajp_name": "磯風",
        "engb_name": "Isokaze", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2018年03月"
        },
    "2280000318": {
        "vari_ksid": 2280000318, "zhcn_name": "滨风改", "zhtw_name": "濱風改", "jajp_name": "浜風改",
        "engb_name": "Hamakaze (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年12月01日"
        },
    "2280000319": {
        "vari_ksid": 2280000319, "zhcn_name": "谷风改", "zhtw_name": "谷風改", "jajp_name": "谷風改",
        "engb_name": "Tanikaze (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年01月19日"
        },
    "2280000320": {
        "vari_ksid": 2280000320, "zhcn_name": "三笠", "zhtw_name": "三笠", "jajp_name": "三笠",
        "engb_name": "Mikasa", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86001], [86010], [86010]], "onln_date": "2017年12月01日"
        },
    "2280000321": {
        "vari_ksid": 2280000321, "zhcn_name": "阿贺野", "zhtw_name": "阿賀野", "jajp_name": "阿賀野",
        "engb_name": "Agano", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年03月21日"
        },
    "2280000322": {
        "vari_ksid": 2280000322, "zhcn_name": "能代", "zhtw_name": "能代", "jajp_name": "能代",
        "engb_name": "Noshiro", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年12月26日"
        },
    "2280000325": {
        "vari_ksid": 2280000325, "zhcn_name": "无敌", "zhtw_name": "無敵", "jajp_name": "マッチレス",
        "engb_name": "Matchless", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月26日"
        },
    "2280000326": {
        "vari_ksid": 2280000326, "zhcn_name": "火枪手", "zhtw_name": "火槍手", "jajp_name": "マスケティーア",
        "engb_name": "Musketeer", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月26日"
        },
    "2280000327": {
        "vari_ksid": 2280000327, "zhcn_name": "斐济", "zhtw_name": "斐濟", "jajp_name": "フィジー",
        "engb_name": "Fiji", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月26日"
        },
    "2280000328": {
        "vari_ksid": 2280000328, "zhcn_name": "牙买加", "zhtw_name": "牙買加", "jajp_name": "ジャマイカ",
        "engb_name": "Jamaica", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月26日"
        },
    "2280000329": {
        "vari_ksid": 2280000329, "zhcn_name": "蒙彼利埃", "zhtw_name": "蒙彼利埃", "jajp_name": "モントピリア",
        "engb_name": "Montpelier", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年03月21日"
        },
    "2280000330": {
        "vari_ksid": 2280000330, "zhcn_name": "丹佛", "zhtw_name": "丹佛", "jajp_name": "デンバー",
        "engb_name": "Denver", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年03月21日"
        },
    "2280000331": {
        "vari_ksid": 2280000331, "zhcn_name": "朝潮", "zhtw_name": "朝潮", "jajp_name": "朝潮",
        "engb_name": "Asashio", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年06月07日"
        },
    "2280000332": {
        "vari_ksid": 2280000332, "zhcn_name": "大潮", "zhtw_name": "大潮", "jajp_name": "大潮",
        "engb_name": "Ooshio", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年06月07日"
        },
    "2280000333": {
        "vari_ksid": 2280000333, "zhcn_name": "满潮", "zhtw_name": "滿潮", "jajp_name": "満潮",
        "engb_name": "Michishio", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2018年04月"
        },
    "2280000334": {
        "vari_ksid": 2280000334, "zhcn_name": "荒潮", "zhtw_name": "荒潮", "jajp_name": "荒潮",
        "engb_name": "Arashio", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2018年09月"
        },
    "2280000335": {
        "vari_ksid": 2280000335, "zhcn_name": "小贝法", "zhtw_name": "小貝法", "jajp_name": "ベルファスト",
        "engb_name": "Little Bel", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年04月26日"
        },
    "2280000336": {
        "vari_ksid": 2280000336, "zhcn_name": "阿贝克隆比", "zhtw_name": "阿貝克隆比",
        "jajp_name": "アバークロンビー",
        "engb_name": "Abercrombie", "vari_rari": 4, "vari_kstp": "330", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2018年05月10日"
        },
    "2280000337": {
        "vari_ksid": 2280000337, "zhcn_name": "苏塞克斯", "zhtw_name": "蘇塞克斯", "jajp_name": "サセックス",
        "engb_name": "Sussex", "vari_rari": 3, "vari_kstp": "220", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2018年05月10日"
        },
    "2280000338": {
        "vari_ksid": 2280000338, "zhcn_name": "伊19", "zhtw_name": "伊19", "jajp_name": "伊19",
        "engb_name": "I-19", "vari_rari": 5, "vari_kstp": "801", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2018年05月31日"
        },
    "2280000339": {
        "vari_ksid": 2280000339, "zhcn_name": "伊26", "zhtw_name": "伊26", "jajp_name": "伊26",
        "engb_name": "I-26", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2018年05月31日"
        },
    "2280000340": {
        "vari_ksid": 2280000340, "zhcn_name": "伊58", "zhtw_name": "伊58", "jajp_name": "伊58",
        "engb_name": "I-58", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2018年05月31日"
        },
    "2280000341": {
        "vari_ksid": 2280000341, "zhcn_name": "U-81", "zhtw_name": "U-81", "jajp_name": "U-81",
        "engb_name": "U-81", "vari_rari": 5, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2018年05月31日"
        },
    "2280000342": {
        "vari_ksid": 2280000342, "zhcn_name": "鲦鱼", "zhtw_name": "鰷魚", "jajp_name": "デイス",
        "engb_name": "Dace", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2018年05月31日"
        },
    "2280000343": {
        "vari_ksid": 2280000343, "zhcn_name": "U-47", "zhtw_name": "U-47", "jajp_name": "U-47",
        "engb_name": "U-47", "vari_rari": 5, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2018年06月28日"
        },
    "2280000344": {
        "vari_ksid": 2280000344, "zhcn_name": "U-557", "zhtw_name": "U-557", "jajp_name": "U557",
        "engb_name": "U-557", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2018年06月28日"
        },
    "2280000345": {
        "vari_ksid": 2280000345, "zhcn_name": "Z35", "zhtw_name": "Z35", "jajp_name": "Z35",
        "engb_name": "Z35", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年06月28日"
        },
    "2280000346": {
        "vari_ksid": 2280000346, "zhcn_name": "Z18", "zhtw_name": "Z18", "jajp_name": "Z18",
        "engb_name": "Z18", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年07月21日"
        },
    "2280000347": {
        "vari_ksid": 2280000347, "zhcn_name": "凯旋", "zhtw_name": "凱旋", "jajp_name": "ル・トリオンファン",
        "engb_name": "Le Triomphant", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年07月26日"
        },
    "2280000348": {
        "vari_ksid": 2280000348, "zhcn_name": "福尔班改", "zhtw_name": "福爾班改", "jajp_name": "フォルバン改",
        "engb_name": "Forbin (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64008,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年07月26日"
        },
    "2280000349": {
        "vari_ksid": 2280000349, "zhcn_name": "埃米尔·贝尔汀改", "zhtw_name": "埃米爾•貝爾坦改",
        "jajp_name": "エミール・ベルタン改",
        "engb_name": "Émile Bertin (Retrofit)", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64008,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年06月27日"
        },
    "2280000350": {
        "vari_ksid": 2280000350, "zhcn_name": "絮库夫", "zhtw_name": "速科夫", "jajp_name": "シュルクーフ",
        "engb_name": "Surcouf", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86003], [86010], [86010]], "onln_date": "2018年07月26日"
        },
    "2280000351": {
        "vari_ksid": 2280000351, "zhcn_name": "勒马尔改", "zhtw_name": "勒馬爾改", "jajp_name": "ル・マルス改",
        "engb_name": "Le Mars (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64009,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年07月26日"
        },
    "2280000352": {
        "vari_ksid": 2280000352, "zhcn_name": "敦刻尔克", "zhtw_name": "敦克爾克", "jajp_name": "ダンケルク",
        "engb_name": "Dunkerque", "vari_rari": 4, "vari_kstp": "302", "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2018年07月26日"
        },
    "2280000353": {
        "vari_ksid": 2280000353, "zhcn_name": "让·巴尔", "zhtw_name": "讓·巴爾", "jajp_name": "ジャン・バール",
        "engb_name": "Jean Bart", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2018年07月26日"
        },
    "2280000354": {
        "vari_ksid": 2280000354, "zhcn_name": "马萨诸塞", "zhtw_name": "麻薩諸塞", "jajp_name": "マサチューセッツ",
        "engb_name": "Massachusetts", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2018年07月26日"
        },
    "2280000355": {
        "vari_ksid": 2280000355, "zhcn_name": "布什", "zhtw_name": "布希", "jajp_name": "ブッシュ",
        "engb_name": "Bush", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2018年08月"
        },
    "2280000356": {
        "vari_ksid": 2280000356, "zhcn_name": "半人马", "zhtw_name": "半人馬", "jajp_name": "セントー",
        "engb_name": "Centaur", "vari_rari": 5, "vari_kstp": "701", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86007], [86007], [86008], [86010, 86015], [86010, 86015]],
        "onln_date": "2018年08月20日"
        },
    "2280000357": {
        "vari_ksid": 2280000357, "zhcn_name": "埃塞克斯", "zhtw_name": "艾塞克斯", "jajp_name": "エセックス",
        "engb_name": "Essex", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2018年09月14日"
        },
    "2280000358": {
        "vari_ksid": 2280000358, "zhcn_name": "大青花鱼", "zhtw_name": "大青花魚", "jajp_name": "アルバコア",
        "engb_name": "Albacore", "vari_rari": 5, "vari_kstp": "801", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2018年09月14日"
        },
    "2280000359": {
        "vari_ksid": 2280000359, "zhcn_name": "鲁莽", "zhtw_name": "魯莽", "jajp_name": "ル・テメレール",
        "engb_name": "Le Téméraire", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年09月14日"
        },
    "2280000360": {
        "vari_ksid": 2280000360, "zhcn_name": "孟菲斯", "zhtw_name": "曼非斯", "jajp_name": "メンフィス",
        "engb_name": "Memphis", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2018年10月"
        },
    "2280000361": {
        "vari_ksid": 2280000361, "zhcn_name": "纽卡斯尔改", "zhtw_name": "紐卡斯爾改",
        "jajp_name": "ニューカッスル改",
        "engb_name": "Newcastle (Retrofit)", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年09月28日"
        },
    "2280000362": {
        "vari_ksid": 2280000362, "zhcn_name": "霍比", "zhtw_name": "霍比", "jajp_name": "ホビー",
        "engb_name": "Hobby", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年10月25日"
        },
    "2280000363": {
        "vari_ksid": 2280000363, "zhcn_name": "科尔克", "zhtw_name": "科爾克", "jajp_name": "カーク",
        "engb_name": "Kalk", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年10月25日"
        },
    "2280000364": {
        "vari_ksid": 2280000364, "zhcn_name": "明尼阿波利斯", "zhtw_name": "明尼亞波利斯",
        "jajp_name": "ミネアポリス",
        "engb_name": "Minneapolis", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2018年10月25日"
        },
    "2280000365": {
        "vari_ksid": 2280000365, "zhcn_name": "黑泽伍德", "zhtw_name": "黑澤伍德", "jajp_name": "ヘイゼルウッド",
        "engb_name": "Hazelwood", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2018年11月"
        },
    "2280000366": {
        "vari_ksid": 2280000366, "zhcn_name": "康克德", "zhtw_name": "康克德", "jajp_name": "コンコード",
        "engb_name": "Concord", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年11月14日"
        },
    "2280000367": {
        "vari_ksid": 2280000367, "zhcn_name": "天城", "zhtw_name": "天城", "jajp_name": "天城",
        "engb_name": "Amagi", "vari_rari": 5, "vari_kstp": "302", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2018年12月27日"
        },
    "2280000369": {
        "vari_ksid": 2280000369, "zhcn_name": "旗风", "zhtw_name": "旗風", "jajp_name": "旗風",
        "engb_name": "Hatakaze", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年12月27日"
        },
    "2280000370": {
        "vari_ksid": 2280000370, "zhcn_name": "卷波", "zhtw_name": "卷波", "jajp_name": "巻波",
        "engb_name": "Makinami", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年12月27日"
        },
    "2280000371": {
        "vari_ksid": 2280000371, "zhcn_name": "天狼星", "zhtw_name": "天狼星", "jajp_name": "シリアス",
        "engb_name": "Sirius", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年01月24日"
        },
    "2280000372": {
        "vari_ksid": 2280000372, "zhcn_name": "库拉索改", "zhtw_name": "庫拉索改", "jajp_name": "キュラソー改",
        "engb_name": "Curacoa (Retrofit)", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86001, 86002], [86006], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年06月13日"
        },
    "2280000373": {
        "vari_ksid": 2280000373, "zhcn_name": "杓鹬改", "zhtw_name": "杓鷸改", "jajp_name": "カーリュー改",
        "engb_name": "Curlew (Retrofit)", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86001, 86002], [86006], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年06月13日"
        },
    "2280000374": {
        "vari_ksid": 2280000374, "zhcn_name": "金伯利", "zhtw_name": "金伯利", "jajp_name": "キンバリー",
        "engb_name": "Kimberly", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年01月31日"
        },
    "2280000375": {
        "vari_ksid": 2280000375, "zhcn_name": "马拉尼", "zhtw_name": "馬拉尼", "jajp_name": "マラニー",
        "engb_name": "Mullany", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年01月31日"
        },
    "2280000376": {
        "vari_ksid": 2280000376, "zhcn_name": "追赶者", "zhtw_name": "追趕者", "jajp_name": "チェイサー",
        "engb_name": "Chaser", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2019年01月31日"
        },
    "2280000377": {
        "vari_ksid": 2280000377, "zhcn_name": "独立改", "zhtw_name": "獨立改", "jajp_name": "インディペンデンス改",
        "engb_name": "Independence (Retrofit)", "vari_rari": 5, "vari_kstp": "701", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2021年05月27日"
        },
    "2280000378": {
        "vari_ksid": 2280000378, "zhcn_name": "香格里拉", "zhtw_name": "香格里拉", "jajp_name": "シャングリラ",
        "engb_name": "Shangri-La", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2019年02月28日"
        },
    "2280000379": {
        "vari_ksid": 2280000379, "zhcn_name": "Z2", "zhtw_name": "Z2", "jajp_name": "Z2", "engb_name": "Z2",
        "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年03月07日"
        },
    "2280000380": {
        "vari_ksid": 2280000380, "zhcn_name": "邦克山", "zhtw_name": "碉堡山", "jajp_name": "バンカー・ヒル",
        "engb_name": "Bunker Hill", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2019年03月22日"
        },
    "2280000381": {
        "vari_ksid": 2280000381, "zhcn_name": "伊13", "zhtw_name": "伊13", "jajp_name": "伊13",
        "engb_name": "I-13", "vari_rari": 5, "vari_kstp": "881", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86012], [86010], [86010]], "onln_date": "2019年03月28日"
        },
    "2280000382": {
        "vari_ksid": 2280000382, "zhcn_name": "铃谷", "zhtw_name": "鈴谷", "jajp_name": "鈴谷",
        "engb_name": "Suzuya", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86002, 86003], [86005], [86006], [86010], [86010]], "onln_date": "2019年03月28日"
        },
    "2280000383": {
        "vari_ksid": 2280000383, "zhcn_name": "小比叡", "zhtw_name": "小比叡", "jajp_name": "比叡ちゃん",
        "engb_name": "Hiei-chan", "vari_rari": 4, "vari_kstp": "302", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2019年04月26日"
        },
    "2280000384": {
        "vari_ksid": 2280000384, "zhcn_name": "小赤城", "zhtw_name": "小赤城", "jajp_name": "赤城ちゃん",
        "engb_name": "Akagi-chan", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2019年04月26日"
        },
    "2280000385": {
        "vari_ksid": 2280000385, "zhcn_name": "小齐柏林", "zhtw_name": "小齊柏林", "jajp_name": "ツェッペリンちゃん",
        "engb_name": "Zeppy", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86002, 86009], [86010], [86010]], "onln_date": "2019年04月26日"
        },
    "2280000386": {
        "vari_ksid": 2280000386, "zhcn_name": "U-556", "zhtw_name": "U-556", "jajp_name": "U-556",
        "engb_name": "U-556", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2019年05月23日"
        },
    "2280000387": {
        "vari_ksid": 2280000387, "zhcn_name": "U-73", "zhtw_name": "U-73", "jajp_name": "U-73",
        "engb_name": "U-73", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2019年05月23日"
        },
    "2280000388": {
        "vari_ksid": 2280000388, "zhcn_name": "Z36", "zhtw_name": "Z36", "jajp_name": "Z36",
        "engb_name": "Z36", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年05月23日"
        },
    "2280000389": {
        "vari_ksid": 2280000389, "zhcn_name": "回声", "zhtw_name": "回聲", "jajp_name": "エコー",
        "engb_name": "Echo", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年05月23日"
        },
    "2280000390": {
        "vari_ksid": 2280000390, "zhcn_name": "小海伦娜", "zhtw_name": "小海倫娜", "jajp_name": "リトル・ヘレナ",
        "engb_name": "Lena", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年05月30日"
        },
    "2280000391": {
        "vari_ksid": 2280000391, "zhcn_name": "小克利夫兰", "zhtw_name": "小克里夫蘭",
        "jajp_name": "リトル・クリーブランド",
        "engb_name": "Clevelad", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年05月30日"
        },
    "2280000392": {
        "vari_ksid": 2280000392, "zhcn_name": "小圣地亚哥", "zhtw_name": "小聖地牙哥",
        "jajp_name": "リトル・サンディエゴ",
        "engb_name": "Lili Sandy", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年05月30日"
        },
    "2280000393": {
        "vari_ksid": 2280000393, "zhcn_name": "确捷", "zhtw_name": "確捷", "jajp_name": "スウィフトシュア",
        "engb_name": "Swiftsure", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年06月13日"
        },
    "2280000394": {
        "vari_ksid": 2280000394, "zhcn_name": "恶毒", "zhtw_name": "惡毒", "jajp_name": "ル・マラン",
        "engb_name": "Le Malin", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年06月27日"
        },
    "2280000395": {
        "vari_ksid": 2280000395, "zhcn_name": "倔强", "zhtw_name": "倔強", "jajp_name": "ルピニャート",
        "engb_name": "L' Opiniâtre", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年06月27日"
        },
    "2280000396": {
        "vari_ksid": 2280000396, "zhcn_name": "伊25", "zhtw_name": "伊25", "jajp_name": "伊25",
        "engb_name": "I-25", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2019年07月11日"
        },
    "2280000397": {
        "vari_ksid": 2280000397, "zhcn_name": "伊56", "zhtw_name": "伊56", "jajp_name": "伊56",
        "engb_name": "I-56", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2019年07月11日"
        },
    "2280000398": {
        "vari_ksid": 2280000398, "zhcn_name": "伊168", "zhtw_name": "伊168", "jajp_name": "伊168",
        "engb_name": "I-168", "vari_rari": 5, "vari_kstp": "801", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2019年07月11日"
        },
    "2280000399": {
        "vari_ksid": 2280000399, "zhcn_name": "U-101", "zhtw_name": "U-101", "jajp_name": "U-101",
        "engb_name": "U-101", "vari_rari": 5, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2019年07月11日"
        },
    "2280000400": {
        "vari_ksid": 2280000400, "zhcn_name": "U-522", "zhtw_name": "U-522", "jajp_name": "U-522",
        "engb_name": "U-522", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2019年07月11日"
        },
    "2280000401": {
        "vari_ksid": 2280000401, "zhcn_name": "阿拉巴马", "zhtw_name": "阿拉巴馬", "jajp_name": "アラバマ",
        "engb_name": "Alabama", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2019年07月31日"
        },
    "2280000402": {
        "vari_ksid": 2280000402, "zhcn_name": "棘鳍", "zhtw_name": "棘鰭", "jajp_name": "カヴァラ",
        "engb_name": "Cavalla", "vari_rari": 5, "vari_kstp": "801", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2019年07月31日"
        },
    "2280000403": {
        "vari_ksid": 2280000403, "zhcn_name": "巴丹", "zhtw_name": "巴丹", "jajp_name": "バターン",
        "engb_name": "Bataan", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2019年07月31日"
        },
    "2280000404": {
        "vari_ksid": 2280000404, "zhcn_name": "圣胡安", "zhtw_name": "聖胡安", "jajp_name": "サンフアン",
        "engb_name": "San Juan", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年07月31日"
        },
    "2280000405": {
        "vari_ksid": 2280000405, "zhcn_name": "伯明翰", "zhtw_name": "伯明罕", "jajp_name": "バーミンガム",
        "engb_name": "Birmingham", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年07月31日"
        },
    "2280000406": {
        "vari_ksid": 2280000406, "zhcn_name": "艾尔温", "zhtw_name": "艾爾文", "jajp_name": "エールウィン",
        "engb_name": "Aylwin", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年07月31日"
        },
    "2280000407": {
        "vari_ksid": 2280000407, "zhcn_name": "贝奇", "zhtw_name": "貝奇", "jajp_name": "バッチ",
        "engb_name": "Bache", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年08月29日"
        },
    "2280000408": {
        "vari_ksid": 2280000408, "zhcn_name": "黑太子", "zhtw_name": "黑太子", "jajp_name": "ブラック・プリンス",
        "engb_name": "Black Prince", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年08月29日"
        },
    "2280000409": {
        "vari_ksid": 2280000409, "zhcn_name": "斯坦利", "zhtw_name": "斯坦利", "jajp_name": "スタンリー",
        "engb_name": "Stanly", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年09月05日"
        },
    "2280000410": {
        "vari_ksid": 2280000410, "zhcn_name": "利托里奥", "zhtw_name": "利托里奧", "jajp_name": "リットリオ",
        "engb_name": "Littorio", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2019年09月11日"
        },
    "2280000411": {
        "vari_ksid": 2280000411, "zhcn_name": "加富尔伯爵", "zhtw_name": "加富爾伯爵",
        "jajp_name": "コンテ・ディ・カブール",
        "engb_name": "Conte di Cavour", "vari_rari": 3, "vari_kstp": "300", "vari_natl": 64006,
        "bool_retr": 0, "type_equp": [[86004], [86001], [86006], [86010], [86010]],
        "onln_date": "2019年09月11日"
        },
    "2280000412": {
        "vari_ksid": 2280000412, "zhcn_name": "朱利奥·凯撒", "zhtw_name": "朱利奧·凱撒",
        "jajp_name": "ジュリオ・チェザーレ",
        "engb_name": "Giulio Cesare", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2019年09月11日"
        },
    "2280000413": {
        "vari_ksid": 2280000413, "zhcn_name": "扎拉", "zhtw_name": "扎拉", "jajp_name": "ザラ",
        "engb_name": "Zara", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2019年09月11日"
        },
    "2280000414": {
        "vari_ksid": 2280000414, "zhcn_name": "特伦托", "zhtw_name": "特倫托", "jajp_name": "トレント",
        "engb_name": "Trento", "vari_rari": 3, "vari_kstp": "220", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2019年09月11日"
        },
    "2280000415": {
        "vari_ksid": 2280000415, "zhcn_name": "龙骑兵", "zhtw_name": "龍騎兵", "jajp_name": "カラビニエーレ",
        "engb_name": "Carabiniere", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年09月11日"
        },
    "2280000416": {
        "vari_ksid": 2280000416, "zhcn_name": "U-110", "zhtw_name": "U-110", "jajp_name": "U-110",
        "engb_name": "U-110", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2019年10月17日"
        },
    "2280000417": {
        "vari_ksid": 2280000417, "zhcn_name": "斯莫利", "zhtw_name": "斯莫利", "jajp_name": "スモーリー",
        "engb_name": "Smalley", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年10月23日"
        },
    "2280000418": {
        "vari_ksid": 2280000418, "zhcn_name": "加斯科涅(μ兵装)", "zhtw_name": "加斯科涅(μ兵裝)",
        "jajp_name": "ガスコーニュ(μ兵装)", "engb_name": "Gascogne μ", "vari_rari": 5, "vari_kstp": "300",
        "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2019年10月31日"
        },
    "2280000419": {
        "vari_ksid": 2280000419, "zhcn_name": "赤城(μ兵装)", "zhtw_name": "赤城(μ兵裝)",
        "jajp_name": "赤城(μ兵装)",
        "engb_name": "Akagi μ", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2019年10月31日"
        },
    "2280000420": {
        "vari_ksid": 2280000420, "zhcn_name": "克利夫兰(μ兵装)", "zhtw_name": "克里夫蘭(μ兵裝)",
        "jajp_name": "クリーブランド(μ兵装)", "engb_name": "Cleveland μ", "vari_rari": 4, "vari_kstp": "210",
        "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年10月31日"
        },
    "2280000421": {
        "vari_ksid": 2280000421, "zhcn_name": "谢菲尔德(μ兵装)", "zhtw_name": "謝菲爾德(μ兵裝)",
        "jajp_name": "シェフィールド(μ兵装)", "engb_name": "Sheffield μ", "vari_rari": 4, "vari_kstp": "210",
        "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年10月31日"
        },
    "2280000422": {
        "vari_ksid": 2280000422, "zhcn_name": "希佩尔海军上将(μ兵装)", "zhtw_name": "希佩爾將軍(μ兵裝)",
        "jajp_name": "アドミラル・ヒッパー(μ兵装)", "engb_name": "Admiral Hipper μ", "vari_rari": 4,
        "vari_kstp": "220",
        "vari_natl": 64004, "bool_retr": 0, "type_equp": [[86003], [86005], [86006], [86010], [86010]],
        "onln_date": "2019年10月31日"
        },
    "2280000423": {
        "vari_ksid": 2280000423, "zhcn_name": "格拉斯哥", "zhtw_name": "格拉斯哥", "jajp_name": "グラスゴー",
        "engb_name": "Glasgow", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年11月14日"
        },
    "2280000424": {
        "vari_ksid": 2280000424, "zhcn_name": "霞改", "zhtw_name": "霞改", "jajp_name": "霞改",
        "engb_name": "Kasumi (Retrofit)", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64003,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年06月24日"
        },
    "2280000425": {
        "vari_ksid": 2280000425, "zhcn_name": "骏河", "zhtw_name": "駿河", "jajp_name": "駿河",
        "engb_name": "Suruga", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2019年12月26日"
        },
    "2280000426": {
        "vari_ksid": 2280000426, "zhcn_name": "龙凤", "zhtw_name": "龍鳳", "jajp_name": "龍鳳",
        "engb_name": "Ryuuhou", "vari_rari": 5, "vari_kstp": "701", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2019年12月26日"
        },
    "2280000427": {
        "vari_ksid": 2280000427, "zhcn_name": "哈尔西·鲍威尔", "zhtw_name": "海爾賽‧鮑威爾",
        "jajp_name": "ハルゼー・パウエル",
        "engb_name": "Halsey Powell", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年01月21日"
        },
    "2280000428": {
        "vari_ksid": 2280000428, "zhcn_name": "比洛克西", "zhtw_name": "比洛克西", "jajp_name": "ビロクシ",
        "engb_name": "Biloxi", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年01月21日"
        },
    "2280000429": {
        "vari_ksid": 2280000429, "zhcn_name": "浦波", "zhtw_name": "浦波", "jajp_name": "浦波",
        "engb_name": "Uranami", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年01月21日"
        },
    "2280000431": {
        "vari_ksid": 2280000431, "zhcn_name": "威严", "zhtw_name": "威嚴", "jajp_name": "グロズヌイ",
        "engb_name": "Grozny", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年02月27日"
        },
    "2280000432": {
        "vari_ksid": 2280000432, "zhcn_name": "明斯克", "zhtw_name": "明斯克", "jajp_name": "ミンスク",
        "engb_name": "Minsk", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年02月27日"
        },
    "2280000433": {
        "vari_ksid": 2280000433, "zhcn_name": "塔什干", "zhtw_name": "塔什干", "jajp_name": "タシュケント",
        "engb_name": "Tashkent", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年02月27日"
        },
    "2280000434": {
        "vari_ksid": 2280000434, "zhcn_name": "水星纪念改", "zhtw_name": "水星紀念改",
        "jajp_name": "パーミャチ・メルクーリヤ改",
        "engb_name": "Pamiat' Merkuria (Retrofit)", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64007,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年02月25日"
        },
    "2280000435": {
        "vari_ksid": 2280000435, "zhcn_name": "基洛夫", "zhtw_name": "基洛夫", "jajp_name": "キーロフ",
        "engb_name": "Kirov", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年02月25日"
        },
    "2280000436": {
        "vari_ksid": 2280000436, "zhcn_name": "恰巴耶夫", "zhtw_name": "恰巴耶夫", "jajp_name": "チャパエフ",
        "engb_name": "Chapayev", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年02月27日"
        },
    "2280000437": {
        "vari_ksid": 2280000437, "zhcn_name": "甘古特", "zhtw_name": "甘古特", "jajp_name": "ガングート",
        "engb_name": "Gangut", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2020年02月27日"
        },
    "2280000440": {
        "vari_ksid": 2280000440, "zhcn_name": "苏维埃贝拉罗斯", "zhtw_name": "蘇維埃白俄羅斯",
        "jajp_name": "ソビエツカヤ・ベラルーシア", "engb_name": "Sovetskaya Belorussiya", "vari_rari": 5,
        "vari_kstp": "300", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2021年02月25日"
        },
    "2280000441": {
        "vari_ksid": 2280000441, "zhcn_name": "苏维埃罗西亚", "zhtw_name": "蘇維埃俄羅斯",
        "jajp_name": "ソビエツカヤ・ロシア",
        "engb_name": "Sovetskaya Rossiya", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64007,
        "bool_retr": 0, "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]],
        "onln_date": "2020年02月27日"
        },
    "2280000442": {
        "vari_ksid": 2280000442, "zhcn_name": "无畏", "zhtw_name": "無畏", "jajp_name": "イントレピッド",
        "engb_name": "Intrepid", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2020年03月26日"
        },
    "2280000443": {
        "vari_ksid": 2280000443, "zhcn_name": "布莱默顿", "zhtw_name": "布雷默頓", "jajp_name": "ブレマートン",
        "engb_name": "Bremerton", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2020年03月26日"
        },
    "2280000444": {
        "vari_ksid": 2280000444, "zhcn_name": "库珀", "zhtw_name": "庫珀", "jajp_name": "クーパー",
        "engb_name": "Cooper", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年03月26日"
        },
    "2280000445": {
        "vari_ksid": 2280000445, "zhcn_name": "里诺", "zhtw_name": "雷諾", "jajp_name": "リノ",
        "engb_name": "Reno", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年03月26日"
        },
    "2280000446": {
        "vari_ksid": 2280000446, "zhcn_name": "蓝鳃鱼", "zhtw_name": "藍鰓魚", "jajp_name": "ブルーギル",
        "engb_name": "Bluegill", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2020年03月26日"
        },
    "2280000447": {
        "vari_ksid": 2280000447, "zhcn_name": "卡萨布兰卡", "zhtw_name": "卡薩布蘭卡", "jajp_name": "カサブランカ",
        "engb_name": "Casablanca", "vari_rari": 3, "vari_kstp": "701", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2020年03月26日"
        },
    "2280000448": {
        "vari_ksid": 2280000448, "zhcn_name": "马布尔黑德", "zhtw_name": "馬布爾黑德",
        "jajp_name": "マーブルヘッド",
        "engb_name": "Marblehead", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年03月26日"
        },
    "2280000449": {
        "vari_ksid": 2280000449, "zhcn_name": "花月", "zhtw_name": "花月", "jajp_name": "花月",
        "engb_name": "Hanazuki", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年04月23日"
        },
    "2280000450": {
        "vari_ksid": 2280000450, "zhcn_name": "长波", "zhtw_name": "長波", "jajp_name": "長波",
        "engb_name": "Naganami", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年04月23日"
        },
    "2280000451": {
        "vari_ksid": 2280000451, "zhcn_name": "小声望", "zhtw_name": "小聲望", "jajp_name": "リトル・レナウン",
        "engb_name": "Little Renown", "vari_rari": 4, "vari_kstp": "302", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2020年04月23日"
        },
    "2280000452": {
        "vari_ksid": 2280000452, "zhcn_name": "塔尔图", "zhtw_name": "塔爾圖", "jajp_name": "タルテュ",
        "engb_name": "Tartu", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年05月07日"
        },
    "2280000453": {
        "vari_ksid": 2280000453, "zhcn_name": "黎塞留", "zhtw_name": "黎胥留", "jajp_name": "リシュリュー",
        "engb_name": "Richelieu", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2020年05月21日"
        },
    "2280000454": {
        "vari_ksid": 2280000454, "zhcn_name": "圣女贞德", "zhtw_name": "聖女貞德", "jajp_name": "ジャンヌ・ダルク",
        "engb_name": "Jeanne d' Arc", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年05月21日"
        },
    "2280000455": {
        "vari_ksid": 2280000455, "zhcn_name": "阿尔及利亚", "zhtw_name": "阿爾及利亞", "jajp_name": "アルジェリー",
        "engb_name": "Algérie", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2020年05月21日"
        },
    "2280000456": {
        "vari_ksid": 2280000456, "zhcn_name": "拉·加利索尼埃", "zhtw_name": "拉·加利索尼埃",
        "jajp_name": "ラ・ガリソニエール",
        "engb_name": "La Galissonnière", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64009,
        "bool_retr": 0, "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年05月21日"
        },
    "2280000457": {
        "vari_ksid": 2280000457, "zhcn_name": "沃克兰", "zhtw_name": "沃克蘭", "jajp_name": "ヴォークラン",
        "engb_name": "Vauquelin", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年05月21日"
        },
    "2280000458": {
        "vari_ksid": 2280000458, "zhcn_name": "贝亚恩", "zhtw_name": "貝亞恩", "jajp_name": "ベアルン",
        "engb_name": "Béarn", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86002, 86009], [86010], [86010]], "onln_date": "2020年05月21日"
        },
    "2280000459": {
        "vari_ksid": 2280000459, "zhcn_name": "小光辉", "zhtw_name": "小光輝", "jajp_name": "リトル・イラストリアス",
        "engb_name": "Little Illustrious", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86007], [86007], [86008], [86010], [86010]],
        "onln_date": "2020年05月28日"
        },
    "2280000460": {
        "vari_ksid": 2280000460, "zhcn_name": "爱斯基摩人", "zhtw_name": "愛斯基摩", "jajp_name": "エスキモー",
        "engb_name": "Eskimo", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年06月03日"
        },
    "2280000461": {
        "vari_ksid": 2280000461, "zhcn_name": "豪", "zhtw_name": "豪", "jajp_name": "ハウ",
        "engb_name": "Howe",
        "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2020年07月23日"
        },
    "2280000462": {
        "vari_ksid": 2280000462, "zhcn_name": "英仙座", "zhtw_name": "英仙座", "jajp_name": "パーシュース",
        "engb_name": "Perseus", "vari_rari": 5, "vari_kstp": "701", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2020年07月23日"
        },
    "2280000463": {
        "vari_ksid": 2280000463, "zhcn_name": "赫敏", "zhtw_name": "赫敏", "jajp_name": "ハーマイオニー",
        "engb_name": "Hermione", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年07月23日"
        },
    "2280000464": {
        "vari_ksid": 2280000464, "zhcn_name": "英勇", "zhtw_name": "英勇", "jajp_name": "ヴァリアント",
        "engb_name": "Valiant", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2020年07月23日"
        },
    "2280000465": {
        "vari_ksid": 2280000465, "zhcn_name": "伊卡洛斯", "zhtw_name": "伊卡洛斯", "jajp_name": "イカルス",
        "engb_name": "Icarus", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年07月23日"
        },
    "2280000466": {
        "vari_ksid": 2280000466, "zhcn_name": "Z26", "zhtw_name": "Z26", "jajp_name": "Z26",
        "engb_name": "Z26", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年08月20日"
        },
    "2280000467": {
        "vari_ksid": 2280000467, "zhcn_name": "U-96", "zhtw_name": "U-96", "jajp_name": "U-96",
        "engb_name": "U-96", "vari_rari": 5, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2020年08月20日"
        },
    "2280000468": {
        "vari_ksid": 2280000468, "zhcn_name": "凉月", "zhtw_name": "涼月", "jajp_name": "涼月",
        "engb_name": "Suzutsuki", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年09月17日"
        },
    "2280000469": {
        "vari_ksid": 2280000469, "zhcn_name": "熊野", "zhtw_name": "熊野", "jajp_name": "熊野",
        "engb_name": "Kumano", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86002, 86003], [86005], [86006], [86010], [86010]], "onln_date": "2020年09月17日"
        },
    "2280000470": {
        "vari_ksid": 2280000470, "zhcn_name": "千岁", "zhtw_name": "千歲", "jajp_name": "千歳",
        "engb_name": "Chitose", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2020年09月17日"
        },
    "2280000471": {
        "vari_ksid": 2280000471, "zhcn_name": "千代田", "zhtw_name": "千代田", "jajp_name": "千代田",
        "engb_name": "Chiyoda", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2020年09月17日"
        },
    "2280000472": {
        "vari_ksid": 2280000472, "zhcn_name": "樫野", "zhtw_name": "樫野", "jajp_name": "樫野",
        "engb_name": "Kashino", "vari_rari": 4, "vari_kstp": "540", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86006], [86010, 86018], [86010, 86018], [86010, 86018]],
        "onln_date": "2020年09月17日"
        },
    "2280000473": {
        "vari_ksid": 2280000473, "zhcn_name": "普林斯顿", "zhtw_name": "普林斯頓", "jajp_name": "プリンストン",
        "engb_name": "Princeton", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2020年10月12日"
        },
    "2280000474": {
        "vari_ksid": 2280000474, "zhcn_name": "大凤(μ兵装)", "zhtw_name": "大鳳(μ兵裝)",
        "jajp_name": "大鳳(μ兵装)",
        "engb_name": "Taihou μ", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2020年10月29日"
        },
    "2280000475": {
        "vari_ksid": 2280000475, "zhcn_name": "塔什干(μ兵装)", "zhtw_name": "塔什干(μ兵裝)",
        "jajp_name": "タシュケント(μ兵装)", "engb_name": "Tashkent μ", "vari_rari": 5, "vari_kstp": "100",
        "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年10月29日"
        },
    "2280000476": {
        "vari_ksid": 2280000476, "zhcn_name": "黛朵(μ兵装)", "zhtw_name": "黛朵(μ兵裝)",
        "jajp_name": "ダイドー(μ兵装)",
        "engb_name": "Dido μ", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年10月29日"
        },
    "2280000477": {
        "vari_ksid": 2280000477, "zhcn_name": "大青花鱼(μ兵装)", "zhtw_name": "大青花魚(μ兵裝)",
        "jajp_name": "アルバコア(μ兵装)", "engb_name": "Albacore μ", "vari_rari": 4, "vari_kstp": "801",
        "vari_natl": 64001, "bool_retr": 0, "type_equp": [[86013], [86013], [86001], [86010], [86010]],
        "onln_date": "2020年10月29日"
        },
    "2280000478": {
        "vari_ksid": 2280000478, "zhcn_name": "巴尔的摩(μ兵装)", "zhtw_name": "巴爾的摩(μ兵裝)",
        "jajp_name": "ボルチモア(μ兵装)", "engb_name": "Baltimore μ", "vari_rari": 4, "vari_kstp": "220",
        "vari_natl": 64001, "bool_retr": 0, "type_equp": [[86003], [86001], [86006], [86010], [86010]],
        "onln_date": "2020年10月29日"
        },
    "2280000479": {
        "vari_ksid": 2280000479, "zhcn_name": "罗恩(μ兵装)", "zhtw_name": "羅恩(μ兵裝)",
        "jajp_name": "ローン(μ兵装)",
        "engb_name": "Roon μ", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2020年10月29日"
        },
    "2280000480": {
        "vari_ksid": 2280000480, "zhcn_name": "光辉(μ兵装)", "zhtw_name": "光輝(μ兵裝)",
        "jajp_name": "イラストリアス(μ兵装)",
        "engb_name": "Illustrious μ", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86007], [86007], [86008], [86010], [86010]], "onln_date": "2020年10月29日"
        },
    "2280000481": {
        "vari_ksid": 2280000481, "zhcn_name": "恶毒(μ兵装)", "zhtw_name": "惡毒(μ兵裝)",
        "jajp_name": "ル・マラン(μ兵装)",
        "engb_name": "Le Malin μ", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年10月29日"
        },
    "2280000482": {
        "vari_ksid": 2280000482, "zhcn_name": "彼得·史特拉塞", "zhtw_name": "彼得·史特拉塞",
        "jajp_name": "ペーター・シュトラッサー",
        "engb_name": "Peter Strasser", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64004,
        "bool_retr": 0, "type_equp": [[86007], [86009], [86008], [86010], [86010]],
        "onln_date": "2020年12月29日"
        },
    "2280000483": {
        "vari_ksid": 2280000483, "zhcn_name": "海因里希亲王", "zhtw_name": "海因里希親王",
        "jajp_name": "プリンツ・ハインリヒ",
        "engb_name": "Prinz Heinrich", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64004,
        "bool_retr": 0, "type_equp": [[86003, 86011], [86005], [86006], [86010], [86010]],
        "onln_date": "2020年12月29日"
        },
    "2280000484": {
        "vari_ksid": 2280000484, "zhcn_name": "U-37", "zhtw_name": "U-37", "jajp_name": "U-37",
        "engb_name": "U-37", "vari_rari": 5, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2020年12月29日"
        },
    "2280000485": {
        "vari_ksid": 2280000485, "zhcn_name": "威悉", "zhtw_name": "威悉", "jajp_name": "ヴェーザー",
        "engb_name": "Weser", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2020年12月29日"
        },
    "2280000486": {
        "vari_ksid": 2280000486, "zhcn_name": "纽伦堡", "zhtw_name": "紐倫堡", "jajp_name": "ニュルンベルク",
        "engb_name": "Nürnberg", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年12月29日"
        },
    "2280000487": {
        "vari_ksid": 2280000487, "zhcn_name": "Z24", "zhtw_name": "Z24", "jajp_name": "Z24",
        "engb_name": "Z24", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年12月29日"
        },
    "2280000488": {
        "vari_ksid": 2280000488, "zhcn_name": "Z28", "zhtw_name": "Z28", "jajp_name": "Z28",
        "engb_name": "Z28", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年12月29日"
        },
    "2280000489": {
        "vari_ksid": 2280000489, "zhcn_name": "波拉", "zhtw_name": "波拉*", "jajp_name": "ポーラ",
        "engb_name": "Pola", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2021年01月21日"
        },
    "2280000490": {
        "vari_ksid": 2280000490, "zhcn_name": "文琴佐·焦贝蒂", "zhtw_name": "文琴佐·焦貝蒂*",
        "jajp_name": "ヴィンチェンツォ・ジョベルティ", "engb_name": "Vincenzo Gioberti", "vari_rari": 4, "vari_kstp": "100",
        "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年01月21日"
        },
    "2280000491": {
        "vari_ksid": 2280000491, "zhcn_name": "神速", "zhtw_name": "神速", "jajp_name": "ストレミテルヌイ",
        "engb_name": "Stremitelny", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2021年02月"
        },
    "2280000492": {
        "vari_ksid": 2280000492, "zhcn_name": "U-410", "zhtw_name": "U-410", "jajp_name": "U-410",
        "engb_name": "U-410", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2021年02月04日"
        },
    "2280000493": {
        "vari_ksid": 2280000493, "zhcn_name": "应瑞", "zhtw_name": "應瑞", "jajp_name": "応瑞",
        "engb_name": "Ying Swei", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64005, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86005], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年02月04日"
        },
    "2280000494": {
        "vari_ksid": 2280000494, "zhcn_name": "肇和", "zhtw_name": "肇和", "jajp_name": "肇和",
        "engb_name": "Chao Ho", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64005, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86005], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年02月04日"
        },
    "2280000495": {
        "vari_ksid": 2280000495, "zhcn_name": "佩内洛珀", "zhtw_name": "佩內洛珀", "jajp_name": "ペネロピ",
        "engb_name": "Penelope", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年02月04日"
        },
    "2280000496": {
        "vari_ksid": 2280000496, "zhcn_name": "塔林", "zhtw_name": "塔林", "jajp_name": "タリン",
        "engb_name": "Tallinn", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86002, 86003], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年02月25日"
        },
    "2280000497": {
        "vari_ksid": 2280000497, "zhcn_name": "雷鸣", "zhtw_name": "雷鳴", "jajp_name": "グレミャーシュチ",
        "engb_name": "Gremyashchy", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年02月25日"
        },
    "2280000498": {
        "vari_ksid": 2280000498, "zhcn_name": "摩尔曼斯克", "zhtw_name": "摩爾曼斯克", "jajp_name": "ムルマンスク",
        "engb_name": "Murmansk", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年02月25日"
        },
    "2280000499": {
        "vari_ksid": 2280000499, "zhcn_name": "洪亮", "zhtw_name": "洪亮", "jajp_name": "グロームキィ",
        "engb_name": "Gromky", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年02月25日"
        },
    "2280000500": {
        "vari_ksid": 2280000500, "zhcn_name": "维托里奥·维内托", "zhtw_name": "維托里奧·維內托",
        "jajp_name": "ヴィットリオ・ヴェネト", "engb_name": "Vittorio Veneto", "vari_rari": 5, "vari_kstp": "300",
        "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2021年04月22日"
        },
    "2280000501": {
        "vari_ksid": 2280000501, "zhcn_name": "阿布鲁齐公爵", "zhtw_name": "阿布魯齊公爵",
        "jajp_name": "ドゥーカ・デッリ・アブルッツィ", "engb_name": "Duca degli Abruzzi", "vari_rari": 5,
        "vari_kstp": "210", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年04月22日"
        },
    "2280000502": {
        "vari_ksid": 2280000502, "zhcn_name": "天鹰", "zhtw_name": "天鷹", "jajp_name": "アクィラ",
        "engb_name": "Aquila", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86007], [86007, 86009], [86008], [86010], [86010]], "onln_date": "2021年04月22日"
        },
    "2280000503": {
        "vari_ksid": 2280000503, "zhcn_name": "托里拆利", "zhtw_name": "托里切利", "jajp_name": "トリチェリ",
        "engb_name": "Torricelli", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2021年04月22日"
        },
    "2280000504": {
        "vari_ksid": 2280000504, "zhcn_name": "西北风", "zhtw_name": "西北風", "jajp_name": "マエストラーレ",
        "engb_name": "Maestrale", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年04月22日"
        },
    "2280000505": {
        "vari_ksid": 2280000505, "zhcn_name": "西南风", "zhtw_name": "西南風", "jajp_name": "リベッチオ",
        "engb_name": "Libeccio", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年04月22日"
        },
    "2280000506": {
        "vari_ksid": 2280000506, "zhcn_name": "尼科洛索·达雷科", "zhtw_name": "尼科洛索·達·雷科",
        "jajp_name": "ニコロソ・ダ・レッコ", "engb_name": "Nicoloso da Recco", "vari_rari": 4, "vari_kstp": "100",
        "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年04月22日"
        },
    "2280000507": {
        "vari_ksid": 2280000507, "zhcn_name": "追风", "zhtw_name": "追風", "jajp_name": "追風",
        "engb_name": "Oite", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2021年04月"
        },
    "2280000508": {
        "vari_ksid": 2280000508, "zhcn_name": "艾伦·萨姆纳", "zhtw_name": "艾倫·薩姆納*",
        "jajp_name": "アレン・M・サムナー",
        "engb_name": "Allen M. Sumner", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年03月25日"
        },
    "2280000509": {
        "vari_ksid": 2280000509, "zhcn_name": "史蒂芬·波特", "zhtw_name": "史蒂芬·波特*",
        "jajp_name": "ステフェン・ポッター",
        "engb_name": "Stephen Potter", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年03月25日"
        },
    "2280000510": {
        "vari_ksid": 2280000510, "zhcn_name": "小天城", "zhtw_name": "小天城", "jajp_name": "天城ちゃん",
        "engb_name": "Amagi-chan", "vari_rari": 4, "vari_kstp": "302", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2021年04月22日"
        },
    "2280000511": {
        "vari_ksid": 2280000511, "zhcn_name": "提康德罗加", "zhtw_name": "提康德羅加",
        "jajp_name": "タイコンデロガ",
        "engb_name": "Ticonderoga", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2021年05月27日"
        },
    "2280000512": {
        "vari_ksid": 2280000512, "zhcn_name": "旧金山", "zhtw_name": "舊金山", "jajp_name": "サンフランシスコ",
        "engb_name": "San Francisco", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2021年05月27日"
        },
    "2280000513": {
        "vari_ksid": 2280000513, "zhcn_name": "射水鱼", "zhtw_name": "射水魚", "jajp_name": "アーチャーフィッシュ",
        "engb_name": "Archerfish", "vari_rari": 5, "vari_kstp": "801", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2021年05月27日"
        },
    "2280000514": {
        "vari_ksid": 2280000514, "zhcn_name": "博伊西", "zhtw_name": "波夕", "jajp_name": "ボイシ",
        "engb_name": "Boise", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年05月27日"
        },
    "2280000515": {
        "vari_ksid": 2280000515, "zhcn_name": "莫里森", "zhtw_name": "莫里森", "jajp_name": "モリソン",
        "engb_name": "Morrison", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年05月27日"
        },
    "2280000516": {
        "vari_ksid": 2280000516, "zhcn_name": "小企业", "zhtw_name": "小企業", "jajp_name": "リトル・エンタープライズ",
        "engb_name": "Little Enterprise", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86007], [86009], [86008], [86010], [86010]],
        "onln_date": "2021年05月27日"
        },
    "2280000517": {
        "vari_ksid": 2280000517, "zhcn_name": "风云", "zhtw_name": "風雲*", "jajp_name": "風雲",
        "engb_name": "Kazagumo", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年06月24日"
        },
    "2280000518": {
        "vari_ksid": 2280000518, "zhcn_name": "英格拉罕", "zhtw_name": "英格拉罕*", "jajp_name": "イングラハム",
        "engb_name": "Ingraham", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年08月19日"
        },
    "2280000519": {
        "vari_ksid": 2280000519, "zhcn_name": "鹦鹉螺", "zhtw_name": "鸚鵡螺*", "jajp_name": "ノーチラス",
        "engb_name": "Nautilus", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001, 86002], [86010], [86010]], "onln_date": "2021年08月19日"
        },
    "2280000520": {
        "vari_ksid": 2280000520, "zhcn_name": "葛城", "zhtw_name": "葛城", "jajp_name": "葛城",
        "engb_name": "Katsuragi", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2021年09月16日"
        },
    "2280000521": {
        "vari_ksid": 2280000521, "zhcn_name": "新奥尔良", "zhtw_name": "紐奧良", "jajp_name": "ニューオリンズ",
        "engb_name": "New Orleans", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2021年10月21日"
        },
    "2280000522": {
        "vari_ksid": 2280000522, "zhcn_name": "可怖", "zhtw_name": "可怖", "jajp_name": "ル・テリブル",
        "engb_name": "Le Terrible", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年10月28日"
        },
    "2280000523": {
        "vari_ksid": 2280000523, "zhcn_name": "马耶·布雷泽", "zhtw_name": "馬耶·布雷澤",
        "jajp_name": "マイレ・ブレゼ",
        "engb_name": "Maillé Brézé", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年10月28日"
        },
    "2280000524": {
        "vari_ksid": 2280000524, "zhcn_name": "福煦", "zhtw_name": "福煦*", "jajp_name": "フォッシュ",
        "engb_name": "Foch", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2021年11月11日"
        },
    "2280000525": {
        "vari_ksid": 2280000525, "zhcn_name": "马格德堡", "zhtw_name": "馬格德堡*", "jajp_name": "マクデブルク",
        "engb_name": "Magdeburg", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年12月29日"
        },
    "2280000526": {
        "vari_ksid": 2280000526, "zhcn_name": "易北", "zhtw_name": "易北*", "jajp_name": "エルベ",
        "engb_name": "Elbe", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2021年12月29日"
        },
    "2280000527": {
        "vari_ksid": 2280000527, "zhcn_name": "阿达尔伯特亲王", "zhtw_name": "阿達爾伯特親王*",
        "jajp_name": "プリンツ・アーダルベルト", "engb_name": "Prinz Adalbert", "vari_rari": 5, "vari_kstp": "220",
        "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86003, 86011], [86005], [86006], [86010], [86010]], "onln_date": "2021年12月29日"
        },
    "2280000528": {
        "vari_ksid": 2280000528, "zhcn_name": "U-1206", "zhtw_name": "U-1206*", "jajp_name": "U-1206",
        "engb_name": "U-1206", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2021年12月29日"
        },
    "2280000529": {
        "vari_ksid": 2280000529, "zhcn_name": "乌尔里希·冯·胡滕", "zhtw_name": "烏爾里希·馮·胡滕*",
        "jajp_name": "ウルリッヒ・フォン・フッテン", "engb_name": "Ulrich von Hutten", "vari_rari": 6, "vari_kstp": "300",
        "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2021年12月29日"
        },
    "2280000530": {
        "vari_ksid": 2280000530, "zhcn_name": "卡律布狄斯", "zhtw_name": "卡律布狄斯*",
        "jajp_name": "カリブディス",
        "engb_name": "Charybdis", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年01月27日"
        },
    "2280000531": {
        "vari_ksid": 2280000531, "zhcn_name": "海天", "zhtw_name": "海天*", "jajp_name": "海天",
        "engb_name": "Hai Tien", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64005, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86005], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年01月27日"
        },
    "2280000532": {
        "vari_ksid": 2280000532, "zhcn_name": "海圻", "zhtw_name": "海圻*", "jajp_name": "海圻",
        "engb_name": "Hai Chi", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64005, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86005], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年01月27日"
        },
    "2280000533": {
        "vari_ksid": 2280000533, "zhcn_name": "布里斯托尔", "zhtw_name": "布裡斯托爾*", "jajp_name": "ブリストル",
        "engb_name": "Bristol", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年01月27日"
        },
    "2280000534": {
        "vari_ksid": 2280000534, "zhcn_name": "镇海", "zhtw_name": "鎮海*", "jajp_name": "鎮海",
        "engb_name": "Chen Hai", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64005, "bool_retr": 0,
        "type_equp": [[86012], [86001, 86012], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年01月27日"
        },
    "2280000535": {
        "vari_ksid": 2280000535, "zhcn_name": "基辅", "zhtw_name": "基輔*", "jajp_name": "キエフ",
        "engb_name": "Kiev", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年02月24日"
        },
    "2280000536": {
        "vari_ksid": 2280000536, "zhcn_name": "阿尔汉格尔斯克", "zhtw_name": "阿爾漢格爾斯克*",
        "jajp_name": "アルハンゲリスク",
        "engb_name": "Arkhangelsk", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2022年02月24日"
        },
    "2280000537": {
        "vari_ksid": 2280000537, "zhcn_name": "灵敏", "zhtw_name": "靈敏*", "jajp_name": "ソオブラジーテリヌイ",
        "engb_name": "Soobrazitelny", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年02月24日"
        },
    "2280000538": {
        "vari_ksid": 2280000538, "zhcn_name": "伏尔加", "zhtw_name": "伏爾加*", "jajp_name": "ヴォルガ",
        "engb_name": "Volga", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2022年02月24日"
        },
    "2280000539": {
        "vari_ksid": 2280000539, "zhcn_name": "喀琅施塔得", "zhtw_name": "喀琅施塔得*",
        "jajp_name": "クロンシュタット",
        "engb_name": "Kronshtadt", "vari_rari": 6, "vari_kstp": "250", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86003, 86011], [86002], [86006], [86010], [86010]], "onln_date": "2022年02月24日"
        },
    "2280000540": {
        "vari_ksid": 2280000540, "zhcn_name": "帝国", "zhtw_name": "帝國", "jajp_name": "インペロ",
        "engb_name": "Impero", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86007, 86009], [86009], [86008], [86010], [86010]], "onln_date": "2022年03月24日"
        },
    "2280000541": {
        "vari_ksid": 2280000541, "zhcn_name": "庞培·马格诺", "zhtw_name": "龐培·馬格諾",
        "jajp_name": "ポンペオ・マーニョ",
        "engb_name": "Pompeo Magno", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年03月24日"
        },
    "2280000542": {
        "vari_ksid": 2280000542, "zhcn_name": "的里雅斯特", "zhtw_name": "的里雅斯德", "jajp_name": "トリエステ",
        "engb_name": "Trieste", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2022年03月24日"
        },
    "2280000543": {
        "vari_ksid": 2280000543, "zhcn_name": "塞德利茨", "zhtw_name": "塞德利茨*", "jajp_name": "ザイドリッツ",
        "engb_name": "Seydlitz", "vari_rari": 5, "vari_kstp": "302", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86001, 86006], [86010], [86010]],
        "onln_date": "2022年04月28日"
        },
    "2280000544": {
        "vari_ksid": 2280000544, "zhcn_name": "吕佐夫", "zhtw_name": "呂佐夫*", "jajp_name": "リュッツォウ",
        "engb_name": "Lützow", "vari_rari": 5, "vari_kstp": "302", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86001, 86006], [86010], [86010]],
        "onln_date": "2022年04月28日"
        },
    "2280000545": {
        "vari_ksid": 2280000545, "zhcn_name": "图林根", "zhtw_name": "圖林根*", "jajp_name": "テューリンゲン",
        "engb_name": "Thüringen", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86001, 86006], [86010], [86010]],
        "onln_date": "2022年04月28日"
        },
    "2280000546": {
        "vari_ksid": 2280000546, "zhcn_name": "约克", "zhtw_name": "約克*", "jajp_name": "ヨルク",
        "engb_name": "Yorck", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86003], [86001, 86002], [86005], [86010], [86010]], "onln_date": "2022年04月28日"
        },
    "2280000547": {
        "vari_ksid": 2280000547, "zhcn_name": "埃姆登", "zhtw_name": "埃姆登*", "jajp_name": "エムデン",
        "engb_name": "Emden", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86001], [86001, 86002], [86005], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年04月28日"
        },
    "2280000548": {
        "vari_ksid": 2280000548, "zhcn_name": "埃尔宾", "zhtw_name": "埃爾賓*", "jajp_name": "エルビング",
        "engb_name": "Elbing", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86001, 86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年04月28日"
        },
    "2280000549": {
        "vari_ksid": 2280000549, "zhcn_name": "小欧根", "zhtw_name": "小歐根*", "jajp_name": "プリンツ・オイゲンちゃん",
        "engb_name": "Little Prinz Eugen", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64004,
        "bool_retr": 0, "type_equp": [[86003], [86005], [86006], [86010], [86010]],
        "onln_date": "2022年04月28日"
        },
    "2280000550": {
        "vari_ksid": 2280000550, "zhcn_name": "贾维斯", "zhtw_name": "賈維斯*", "jajp_name": "ジャーヴィス",
        "engb_name": "Jervis", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年05月26日"
        },
    "2280000551": {
        "vari_ksid": 2280000551, "zhcn_name": "司战女神", "zhtw_name": "司戰女神*", "jajp_name": "ベローナ",
        "engb_name": "Bellona", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年05月26日"
        },
    "2280000552": {
        "vari_ksid": 2280000552, "zhcn_name": "小柴郡", "zhtw_name": "小柴郡", "jajp_name": "リトル・チェシャー",
        "engb_name": "Little Cheshire", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86003], [86005], [86006], [86010], [86010]],
        "onln_date": "2022年05月26日"
        },
    "2280000553": {
        "vari_ksid": 2280000553, "zhcn_name": "不挠", "zhtw_name": "不撓*", "jajp_name": "インドミタブル",
        "engb_name": "Indomitable", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86007], [86007], [86008], [86010], [86010]], "onln_date": "2022年05月26日"
        },
    "2280000554": {
        "vari_ksid": 2280000554, "zhcn_name": "复仇", "zhtw_name": "復仇*", "jajp_name": "リヴェンジ",
        "engb_name": "Revenge", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2022年05月26日"
        },
    "2280000555": {
        "vari_ksid": 2280000555, "zhcn_name": "霞飞", "zhtw_name": "霞飛*", "jajp_name": "ジョッフル",
        "engb_name": "Joffre", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86009], [86010], [86010]], "onln_date": "2022年06月30日"
        },
    "2280000556": {
        "vari_ksid": 2280000556, "zhcn_name": "不屈", "zhtw_name": "不屈*", "jajp_name": "ランドンターブル",
        "engb_name": "L' Indomptable", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年06月30日"
        },
    "2280000557": {
        "vari_ksid": 2280000557, "zhcn_name": "进取", "zhtw_name": "進取*", "jajp_name": "エンタープライズ",
        "engb_name": "Enterprise", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年06月30日"
        },
    "2280000558": {
        "vari_ksid": 2280000558, "zhcn_name": "莱昂纳多·达·芬奇", "zhtw_name": "萊昂納多·達·芬奇*",
        "jajp_name": "レオナルド・ダ・ヴィンチ", "engb_name": "Leonardo da Vinci", "vari_rari": 5, "vari_kstp": "801",
        "vari_natl": 64006, "bool_retr": 0, "type_equp": [[86013], [86013], [86001], [86010], [86010]],
        "onln_date": "2022年07月28日"
        },
    "2280000559": {
        "vari_ksid": 2280000559, "zhcn_name": "朱塞佩·加里波第", "zhtw_name": "朱塞佩·加里波第*",
        "jajp_name": "ジュゼッペ・ガリバルディ", "engb_name": "Giuseppe Garibaldi", "vari_rari": 5, "vari_kstp": "210",
        "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年07月28日"
        },
    "2280000560": {
        "vari_ksid": 2280000560, "zhcn_name": "博尔扎诺", "zhtw_name": "博爾扎諾*", "jajp_name": "ボルツァーノ",
        "engb_name": "Bolzano", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2022年07月28日"
        },
    "2280000561": {
        "vari_ksid": 2280000561, "zhcn_name": "罗马", "zhtw_name": "羅馬*", "jajp_name": "ローマ",
        "engb_name": "Roma", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2022年07月28日"
        },
    "2280000562": {
        "vari_ksid": 2280000562, "zhcn_name": "阿尔弗雷多·奥里亚尼", "zhtw_name": "阿爾弗雷多·奧里亞尼*",
        "jajp_name": "アルフレード・オリアーニ", "engb_name": "Alfredo Oriani", "vari_rari": 4, "vari_kstp": "100",
        "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年07月28日"
        },
    "2280000563": {
        "vari_ksid": 2280000563, "zhcn_name": "埃曼努埃尔·佩萨格诺", "zhtw_name": "埃曼努埃爾·佩薩格諾*",
        "jajp_name": "エマヌエーレ・ペッサーニョ", "engb_name": "Emanuele Pessagno", "vari_rari": 4, "vari_kstp": "100",
        "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年07月28日"
        },
    "2280000001": {
        "vari_ksid": 2280000001, "zhcn_name": "泛用型布里", "zhtw_name": "泛用型布里",
        "jajp_name": "汎用型ブリ",
        "engb_name": "Universal Bulin", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64098,
        "bool_retr": 0, "type_equp": [[86001], [86006], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000002": {
        "vari_ksid": 2280000002, "zhcn_name": "试作型布里MKII", "zhtw_name": "試作型布里MKII",
        "jajp_name": "試作型ブリMKII", "engb_name": "Prototype Bulin MKII", "vari_rari": 5, "vari_kstp": "100",
        "vari_natl": 64098, "bool_retr": 0,
        "type_equp": [[86001], [86006], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000003": {
        "vari_ksid": 2280000003, "zhcn_name": "特装型布里MKIII", "zhtw_name": "特裝型布里MKIII",
        "jajp_name": "特装型ブリMKIII", "engb_name": "Specialized Bulin Custom MKIII", "vari_rari": 6,
        "vari_kstp": "100", "vari_natl": 64098, "bool_retr": 0,
        "type_equp": [[86001], [86006], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年09月17日"
        },
    "2280000004": {
        "vari_ksid": 2280000004, "zhcn_name": "杜威", "zhtw_name": "杜威", "jajp_name": "デューイ",
        "engb_name": "Dewey", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年03月22日"
        },
    "2280000005": {
        "vari_ksid": 2280000005, "zhcn_name": "卡辛改", "zhtw_name": "卡辛改", "jajp_name": "カッシン改",
        "engb_name": "Cassin (Retrofit)", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年11月23日"
        },
    "2280000006": {
        "vari_ksid": 2280000006, "zhcn_name": "唐斯改", "zhtw_name": "唐斯改", "jajp_name": "ダウンズ改",
        "engb_name": "Downes (Retrofit)", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年11月23日"
        },
    "2280000007": {
        "vari_ksid": 2280000007, "zhcn_name": "格里德利", "zhtw_name": "格里德利", "jajp_name": "グリッドレイ",
        "engb_name": "Gridley", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000008": {
        "vari_ksid": 2280000008, "zhcn_name": "克雷文", "zhtw_name": "克雷文", "jajp_name": "クレイヴン",
        "engb_name": "Craven", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000009": {
        "vari_ksid": 2280000009, "zhcn_name": "麦考尔", "zhtw_name": "麥考爾", "jajp_name": "マッコール",
        "engb_name": "McCall", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000010": {
        "vari_ksid": 2280000010, "zhcn_name": "莫里", "zhtw_name": "莫里", "jajp_name": "モーリー",
        "engb_name": "Maury", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000011": {
        "vari_ksid": 2280000011, "zhcn_name": "弗莱彻", "zhtw_name": "佛萊契爾", "jajp_name": "フレッチャー",
        "engb_name": "Fletcher", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000013": {
        "vari_ksid": 2280000013, "zhcn_name": "查尔斯·奥斯本", "zhtw_name": "查爾斯·奧斯本",
        "jajp_name": "チャールズ・オースバーン",
        "engb_name": "Charles Ausburne", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64001,
        "bool_retr": 1, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000014": {
        "vari_ksid": 2280000014, "zhcn_name": "撒切尔", "zhtw_name": "柴契爾", "jajp_name": "サッチャー",
        "engb_name": "Thatcher", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000015": {
        "vari_ksid": 2280000015, "zhcn_name": "奥利克", "zhtw_name": "奧利克", "jajp_name": "オーリック",
        "engb_name": "Aulick", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000016": {
        "vari_ksid": 2280000016, "zhcn_name": "富特", "zhtw_name": "富特", "jajp_name": "フート",
        "engb_name": "Foote", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000017": {
        "vari_ksid": 2280000017, "zhcn_name": "斯彭斯", "zhtw_name": "斯彭斯", "jajp_name": "スペンス",
        "engb_name": "Spence", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000018": {
        "vari_ksid": 2280000018, "zhcn_name": "本森", "zhtw_name": "班森", "jajp_name": "ベンソン",
        "engb_name": "Benson", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]], "onln_date": "2017年06月"
        },
    "2280000019": {
        "vari_ksid": 2280000019, "zhcn_name": "拉菲改", "zhtw_name": "拉菲改", "jajp_name": "ラフィー改",
        "engb_name": "Laffey (Retrofit)", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年03月29日"
        },
    "2280000026": {
        "vari_ksid": 2280000026, "zhcn_name": "西姆斯改", "zhtw_name": "西姆斯改", "jajp_name": "シムス改",
        "engb_name": "Sims (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年02月21日"
        },
    "2280000027": {
        "vari_ksid": 2280000027, "zhcn_name": "哈曼改", "zhtw_name": "哈曼改", "jajp_name": "ハムマン改",
        "engb_name": "Hammann (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年07月06日"
        },
    "2280000028": {
        "vari_ksid": 2280000028, "zhcn_name": "埃尔德里奇", "zhtw_name": "埃爾德里奇", "jajp_name": "エルドリッジ",
        "engb_name": "Eldridge", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000029": {
        "vari_ksid": 2280000029, "zhcn_name": "奥马哈", "zhtw_name": "奧馬哈", "jajp_name": "オマハ",
        "engb_name": "Omaha", "vari_rari": 2, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000030": {
        "vari_ksid": 2280000030, "zhcn_name": "罗利", "zhtw_name": "羅利", "jajp_name": "ローリー",
        "engb_name": "Raleigh", "vari_rari": 2, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000031": {
        "vari_ksid": 2280000031, "zhcn_name": "布鲁克林", "zhtw_name": "布魯克林", "jajp_name": "ブルックリン",
        "engb_name": "Brooklyn", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000032": {
        "vari_ksid": 2280000032, "zhcn_name": "菲尼克斯", "zhtw_name": "菲尼克斯", "jajp_name": "フェニックス",
        "engb_name": "Phoenix", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000033": {
        "vari_ksid": 2280000033, "zhcn_name": "海伦娜改", "zhtw_name": "海倫娜改", "jajp_name": "ヘレナ改",
        "engb_name": "Helena (Retrofit)", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年06月03日"
        },
    "2280000034": {
        "vari_ksid": 2280000034, "zhcn_name": "亚特兰大", "zhtw_name": "亞特蘭大", "jajp_name": "アトランタ",
        "engb_name": "Atlanta", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000035": {
        "vari_ksid": 2280000035, "zhcn_name": "朱诺", "zhtw_name": "朱諾", "jajp_name": "ジュノー",
        "engb_name": "Juneau", "vari_rari": 3, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 1,
        "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000036": {
        "vari_ksid": 2280000036, "zhcn_name": "圣地亚哥改", "zhtw_name": "聖地牙哥改",
        "jajp_name": "サンディエゴ改",
        "engb_name": "San Diego (Retrofit)", "vari_rari": 6, "vari_kstp": "210", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86001, 86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年09月28日"
        },
    "2280000037": {
        "vari_ksid": 2280000037, "zhcn_name": "克利夫兰", "zhtw_name": "克里夫蘭", "jajp_name": "クリーブランド",
        "engb_name": "Cleveland", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000038": {
        "vari_ksid": 2280000038, "zhcn_name": "哥伦比亚", "zhtw_name": "哥倫比亞", "jajp_name": "コロンビア",
        "engb_name": "Columbia", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年03月21日"
        },
    "2280000039": {
        "vari_ksid": 2280000039, "zhcn_name": "彭萨科拉", "zhtw_name": "彭薩科拉", "jajp_name": "ペンサコーラ",
        "engb_name": "Pensacola", "vari_rari": 2, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000040": {
        "vari_ksid": 2280000040, "zhcn_name": "盐湖城", "zhtw_name": "鹽湖城", "jajp_name": "ソルトレイクシティ",
        "engb_name": "Salt Lake City", "vari_rari": 2, "vari_kstp": "220", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86003], [86001], [86006], [86010], [86010]],
        "onln_date": "2017年06月23日"
        },
    "2280000041": {
        "vari_ksid": 2280000041, "zhcn_name": "北安普敦", "zhtw_name": "北安普敦", "jajp_name": "ノーザンプトン",
        "engb_name": "Northampton", "vari_rari": 3, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000042": {
        "vari_ksid": 2280000042, "zhcn_name": "芝加哥", "zhtw_name": "芝加哥", "jajp_name": "シカゴ",
        "engb_name": "Chicago", "vari_rari": 3, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000043": {
        "vari_ksid": 2280000043, "zhcn_name": "休斯敦", "zhtw_name": "休士頓", "jajp_name": "ヒューストン",
        "engb_name": "Houston", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000044": {
        "vari_ksid": 2280000044, "zhcn_name": "波特兰改", "zhtw_name": "波特蘭改", "jajp_name": "ポートランド改",
        "engb_name": "Portland (Retrofit)", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86003], [86001], [86006], [86010], [86010]],
        "onln_date": "2017年07月14日"
        },
    "2280000045": {
        "vari_ksid": 2280000045, "zhcn_name": "印第安纳波利斯", "zhtw_name": "印第安納波利斯",
        "jajp_name": "インディアナポリス",
        "engb_name": "Indianapolis", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000046": {
        "vari_ksid": 2280000046, "zhcn_name": "阿斯托利亚", "zhtw_name": "阿斯托利亞", "jajp_name": "アストリア",
        "engb_name": "Astoria", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2018年07月17日"
        },
    "2280000047": {
        "vari_ksid": 2280000047, "zhcn_name": "昆西", "zhtw_name": "昆西", "jajp_name": "クインシー",
        "engb_name": "Quincy", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2018年07月17日"
        },
    "2280000048": {
        "vari_ksid": 2280000048, "zhcn_name": "文森斯", "zhtw_name": "文森尼斯", "jajp_name": "ヴィンセンス",
        "engb_name": "Vincennes", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2018年07月17日"
        },
    "2280000049": {
        "vari_ksid": 2280000049, "zhcn_name": "威奇塔", "zhtw_name": "威奇塔", "jajp_name": "ウィチタ",
        "engb_name": "Wichita", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000050": {
        "vari_ksid": 2280000050, "zhcn_name": "巴尔的摩", "zhtw_name": "巴爾的摩", "jajp_name": "ボルチモア",
        "engb_name": "Baltimore", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2019年07月31日"
        },
    "2280000052": {
        "vari_ksid": 2280000052, "zhcn_name": "内华达改", "zhtw_name": "內華達改", "jajp_name": "ネバダ改",
        "engb_name": "Nevada (Retrofit)", "vari_rari": 3, "vari_kstp": "300", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86004], [86001], [86006], [86010], [86010]],
        "onln_date": "2018年06月21日"
        },
    "2280000053": {
        "vari_ksid": 2280000053, "zhcn_name": "俄克拉荷马改", "zhtw_name": "奧克拉荷馬改",
        "jajp_name": "オクラホマ改",
        "engb_name": "Oklahoma (Retrofit)", "vari_rari": 3, "vari_kstp": "300", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86004], [86001], [86006], [86010], [86010]],
        "onln_date": "2018年04月26日"
        },
    "2280000054": {
        "vari_ksid": 2280000054, "zhcn_name": "宾夕法尼亚", "zhtw_name": "賓夕法尼亞",
        "jajp_name": "ペンシルベニア",
        "engb_name": "Pennsylvania", "vari_rari": 3, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000055": {
        "vari_ksid": 2280000055, "zhcn_name": "亚利桑那", "zhtw_name": "亞利桑那", "jajp_name": "アリゾナ",
        "engb_name": "Arizona", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000058": {
        "vari_ksid": 2280000058, "zhcn_name": "田纳西", "zhtw_name": "田納西", "jajp_name": "テネシー",
        "engb_name": "Tennessee", "vari_rari": 3, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000059": {
        "vari_ksid": 2280000059, "zhcn_name": "加利福尼亚", "zhtw_name": "加利福尼亞",
        "jajp_name": "カリフォルニア",
        "engb_name": "California", "vari_rari": 3, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000060": {
        "vari_ksid": 2280000060, "zhcn_name": "科罗拉多", "zhtw_name": "科羅拉多", "jajp_name": "コロラド",
        "engb_name": "Colorado", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年12月29日"
        },
    "2280000061": {
        "vari_ksid": 2280000061, "zhcn_name": "马里兰", "zhtw_name": "馬里蘭", "jajp_name": "メリーランド",
        "engb_name": "Maryland", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年12月29日"
        },
    "2280000062": {
        "vari_ksid": 2280000062, "zhcn_name": "西弗吉尼亚", "zhtw_name": "西維吉尼亞",
        "jajp_name": "ウェストバージニア",
        "engb_name": "West Virginia", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年12月29日"
        },
    "2280000063": {
        "vari_ksid": 2280000063, "zhcn_name": "北卡罗来纳", "zhtw_name": "北卡羅來納",
        "jajp_name": "ノースカロライナ",
        "engb_name": "North Carolina", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86004], [86001], [86006], [86010], [86010]],
        "onln_date": "2017年12月29日"
        },
    "2280000064": {
        "vari_ksid": 2280000064, "zhcn_name": "华盛顿", "zhtw_name": "華盛頓", "jajp_name": "ワシントン",
        "engb_name": "Washington", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年12月29日"
        },
    "2280000065": {
        "vari_ksid": 2280000065, "zhcn_name": "南达科他", "zhtw_name": "南達科他", "jajp_name": "サウスダコタ",
        "engb_name": "South Dakota", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000068": {
        "vari_ksid": 2280000068, "zhcn_name": "新泽西", "zhtw_name": "紐澤西", "jajp_name": "ニュージャージー",
        "engb_name": "New Jersey", "vari_rari": 6, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2021年05月27日"
        },
    "2280000070": {
        "vari_ksid": 2280000070, "zhcn_name": "长岛改", "zhtw_name": "長島改", "jajp_name": "ロング・アイランド改",
        "engb_name": "Long Island (Retrofit)", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86007], [86009], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2017年10月16日"
        },
    "2280000071": {
        "vari_ksid": 2280000071, "zhcn_name": "博格改", "zhtw_name": "博格改", "jajp_name": "ボーグ改",
        "engb_name": "Bogue (Retrofit)", "vari_rari": 3, "vari_kstp": "701", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86007], [86009], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2017年08月23日"
        },
    "2280000072": {
        "vari_ksid": 2280000072, "zhcn_name": "兰利改", "zhtw_name": "蘭利改", "jajp_name": "ラングレー改",
        "engb_name": "Langley (Retrofit)", "vari_rari": 3, "vari_kstp": "701", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86007], [86007], [86009], [86010, 86015], [86010, 86015]],
        "onln_date": "2017年08月02日"
        },
    "2280000073": {
        "vari_ksid": 2280000073, "zhcn_name": "列克星敦", "zhtw_name": "列星頓", "jajp_name": "レキシントン",
        "engb_name": "Lexington", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86009], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000074": {
        "vari_ksid": 2280000074, "zhcn_name": "萨拉托加改", "zhtw_name": "薩拉托加改", "jajp_name": "サラトガ改",
        "engb_name": "Saratoga (Retrofit)", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86007], [86009], [86009], [86010], [86010]],
        "onln_date": "2018年05月24日"
        },
    "2280000075": {
        "vari_ksid": 2280000075, "zhcn_name": "突击者改", "zhtw_name": "遊騎兵改", "jajp_name": "レンジャー改",
        "engb_name": "Ranger (Retrofit)", "vari_rari": 3, "vari_kstp": "701", "vari_natl": 64001,
        "bool_retr": 0, "type_equp": [[86008], [86009], [86009], [86010, 86015], [86010, 86015]],
        "onln_date": "2017年09月08日"
        },
    "2280000076": {
        "vari_ksid": 2280000076, "zhcn_name": "约克城", "zhtw_name": "約克鎮", "jajp_name": "ヨークタウン",
        "engb_name": "Yorktown", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000077": {
        "vari_ksid": 2280000077, "zhcn_name": "企业", "zhtw_name": "企業", "jajp_name": "エンタープライズ",
        "engb_name": "Enterprise", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000078": {
        "vari_ksid": 2280000078, "zhcn_name": "大黄蜂", "zhtw_name": "大黃蜂", "jajp_name": "ホーネット",
        "engb_name": "Hornet", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280000079": {
        "vari_ksid": 2280000079, "zhcn_name": "胡蜂", "zhtw_name": "胡蜂", "jajp_name": "ワスプ",
        "engb_name": "Wasp", "vari_rari": 3, "vari_kstp": "702", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2017年12月29日"
        },
    "2280000080": {
        "vari_ksid": 2280000080, "zhcn_name": "女灶神", "zhtw_name": "女灶神", "jajp_name": "ヴェスタル",
        "engb_name": "Vestal", "vari_rari": 4, "vari_kstp": "510", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86010], [86006], [86006], [86010], [86010]], "onln_date": "2017年05月25日"
        },
    "2280030007": {
        "vari_ksid": 2280030007, "zhcn_name": "西雅图", "zhtw_name": "西雅圖", "jajp_name": "シアトル",
        "engb_name": "Seattle", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86002], [86002, 86006], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年04月18日"
        },
    "2280030008": {
        "vari_ksid": 2280030008, "zhcn_name": "佐治亚", "zhtw_name": "喬治亞", "jajp_name": "ジョージア",
        "engb_name": "Georgia", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2019年04月18日"
        },
    "2280030018": {
        "vari_ksid": 2280030018, "zhcn_name": "安克雷奇", "zhtw_name": "安克拉治", "jajp_name": "アンカレッジ",
        "engb_name": "Anchorage", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64001, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2021年07月08日"
        },
    "2280000081": {
        "vari_ksid": 2280000081, "zhcn_name": "女将改", "zhtw_name": "女將改", "jajp_name": "アマゾン改",
        "engb_name": "Amazon (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年01月21日"
        },
    "2280000082": {
        "vari_ksid": 2280000082, "zhcn_name": "阿卡司塔改", "zhtw_name": "阿卡司塔改", "jajp_name": "アカスタ改",
        "engb_name": "Acasta (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年05月18日"
        },
    "2280000083": {
        "vari_ksid": 2280000083, "zhcn_name": "热心改", "zhtw_name": "熱心改", "jajp_name": "アーデント改",
        "engb_name": "Ardent (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年05月18日"
        },
    "2280000086": {
        "vari_ksid": 2280000086, "zhcn_name": "小猎兔犬", "zhtw_name": "小獵兔犬", "jajp_name": "ビーグル",
        "engb_name": "Beagle", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000087": {
        "vari_ksid": 2280000087, "zhcn_name": "大斗犬", "zhtw_name": "大鬥犬", "jajp_name": "ブルドッグ",
        "engb_name": "Bulldog", "vari_rari": 2, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000088": {
        "vari_ksid": 2280000088, "zhcn_name": "彗星改", "zhtw_name": "彗星改", "jajp_name": "コメット改",
        "engb_name": "Comet (Retrofit)", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年12月15日"
        },
    "2280000089": {
        "vari_ksid": 2280000089, "zhcn_name": "新月改", "zhtw_name": "新月改", "jajp_name": "クレセント改",
        "engb_name": "Crescent (Retrofit)", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年12月15日"
        },
    "2280000090": {
        "vari_ksid": 2280000090, "zhcn_name": "小天鹅改", "zhtw_name": "小天鵝改", "jajp_name": "シグニット改",
        "engb_name": "Cygnet (Retrofit)", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年07月06日"
        },
    "2280000091": {
        "vari_ksid": 2280000091, "zhcn_name": "狐提改", "zhtw_name": "狐提改", "jajp_name": "フォックスハウンド改",
        "engb_name": "Foxhound (Retrofit)", "vari_rari": 3, "vari_kstp": "100", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月26日"
        },
    "2280000092": {
        "vari_ksid": 2280000092, "zhcn_name": "命运女神改", "zhtw_name": "命運女神改",
        "jajp_name": "フォーチュン改",
        "engb_name": "Fortune (Retrofit)", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002,
        "bool_retr": 0, "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年07月06日"
        },
    "2280000093": {
        "vari_ksid": 2280000093, "zhcn_name": "格伦维尔", "zhtw_name": "格倫維爾", "jajp_name": "グレンヴィル",
        "engb_name": "Grenville", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年01月24日"
        },
    "2280000094": {
        "vari_ksid": 2280000094, "zhcn_name": "萤火虫", "zhtw_name": "螢火蟲", "jajp_name": "グローウォーム",
        "engb_name": "Glowworm", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2017年05月25日"
        },
    "2280000096": {
        "vari_ksid": 2280000096, "zhcn_name": "勇敢", "zhtw_name": "勇敢", "jajp_name": "ハーディ",
        "engb_name": "Hardy", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年03月07日"
        },
    "2280030001": {
        "vari_ksid": 2280030001, "zhcn_name": "海王星", "zhtw_name": "海王星", "jajp_name": "ネプチューン",
        "engb_name": "Neptune", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年04月26日"
        },
    "2280030002": {
        "vari_ksid": 2280030002, "zhcn_name": "君主", "zhtw_name": "君主", "jajp_name": "モナーク",
        "engb_name": "Monarch", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2018年04月26日"
        },
    "2280030013": {
        "vari_ksid": 2280030013, "zhcn_name": "柴郡", "zhtw_name": "柴郡", "jajp_name": "チェシャー",
        "engb_name": "Cheshire", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2020年07月09日"
        },
    "2280030014": {
        "vari_ksid": 2280030014, "zhcn_name": "德雷克", "zhtw_name": "德雷克", "jajp_name": "ドレイク",
        "engb_name": "Drake", "vari_rari": 6, "vari_kstp": "220", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2020年07月09日"
        },
    "2280030023": {
        "vari_ksid": 2280030023, "zhcn_name": "普利茅斯", "zhtw_name": "普利茅斯*", "jajp_name": "プリマス",
        "engb_name": "Plymouth", "vari_rari": 6, "vari_kstp": "210", "vari_natl": 64002, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年07月14日"
        },
    "2280030003": {
        "vari_ksid": 2280030003, "zhcn_name": "伊吹", "zhtw_name": "伊吹", "jajp_name": "伊吹",
        "engb_name": "Ibuki", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2018年04月26日"
        },
    "2280030004": {
        "vari_ksid": 2280030004, "zhcn_name": "出云", "zhtw_name": "出雲", "jajp_name": "出雲",
        "engb_name": "Izumo", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2018年04月26日"
        },
    "2280030009": {
        "vari_ksid": 2280030009, "zhcn_name": "北风", "zhtw_name": "北風", "jajp_name": "北風",
        "engb_name": "Kitakaze", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年04月18日"
        },
    "2280030010": {
        "vari_ksid": 2280030010, "zhcn_name": "吾妻", "zhtw_name": "吾妻", "jajp_name": "吾妻",
        "engb_name": "Azuma", "vari_rari": 6, "vari_kstp": "250", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86003, 86011], [86001], [86006], [86010], [86010]], "onln_date": "2019年04月18日"
        },
    "2280030019": {
        "vari_ksid": 2280030019, "zhcn_name": "白龙", "zhtw_name": "白龍", "jajp_name": "白龍",
        "engb_name": "Hakuryuu", "vari_rari": 6, "vari_kstp": "702", "vari_natl": 64003, "bool_retr": 0,
        "type_equp": [[86007, 86008], [86009], [86008, 86009], [86010], [86010]],
        "onln_date": "2021年07月08日"
        },
    "2280030005": {
        "vari_ksid": 2280030005, "zhcn_name": "罗恩", "zhtw_name": "羅恩", "jajp_name": "ローン",
        "engb_name": "Roon", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2018年04月26日"
        },
    "2280030011": {
        "vari_ksid": 2280030011, "zhcn_name": "腓特烈大帝", "zhtw_name": "腓特烈大帝",
        "jajp_name": "フリードリヒ・デア・グローセ",
        "engb_name": "Friedrich der Große", "vari_rari": 6, "vari_kstp": "300", "vari_natl": 64004,
        "bool_retr": 0, "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]],
        "onln_date": "2019年04月18日"
        },
    "2280030015": {
        "vari_ksid": 2280030015, "zhcn_name": "美因茨", "zhtw_name": "美因茲", "jajp_name": "マインツ",
        "engb_name": "Mainz", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年07月09日"
        },
    "2280030016": {
        "vari_ksid": 2280030016, "zhcn_name": "奥丁", "zhtw_name": "奧丁", "jajp_name": "オーディン",
        "engb_name": "Odin", "vari_rari": 5, "vari_kstp": "302", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86004], [86005], [86006], [86010], [86010]], "onln_date": "2020年07月09日"
        },
    "2280030020": {
        "vari_ksid": 2280030020, "zhcn_name": "埃吉尔", "zhtw_name": "埃吉爾", "jajp_name": "エーギル",
        "engb_name": "Ägir", "vari_rari": 6, "vari_kstp": "250", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86003, 86011], [86005], [86006], [86010], [86010]], "onln_date": "2021年07月08日"
        },
    "2280030021": {
        "vari_ksid": 2280030021, "zhcn_name": "奥古斯特·冯·帕塞瓦尔", "zhtw_name": "奧古斯特·馮·帕塞瓦爾",
        "jajp_name": "アウグスト・フォン・パーセヴァル", "engb_name": "August von Parseval", "vari_rari": 5,
        "vari_kstp": "702", "vari_natl": 64004, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2021年07月08日"
        },
    "2280030024": {
        "vari_ksid": 2280030024, "zhcn_name": "鲁普雷希特亲王", "zhtw_name": "魯普雷希特親王*",
        "jajp_name": "プリンツ・ループレヒト",
        "engb_name": "Prinz Rupprecht", "vari_rari": 5, "vari_kstp": "302", "vari_natl": 64004,
        "bool_retr": 0, "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]],
        "onln_date": "2022年07月14日"
        },
    "2280030025": {
        "vari_ksid": 2280030025, "zhcn_name": "哈尔滨", "zhtw_name": "哈爾濱*", "jajp_name": "ハルビン",
        "engb_name": "Harbin", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64005, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年07月14日"
        },
    "2280030022": {
        "vari_ksid": 2280030022, "zhcn_name": "马可波罗", "zhtw_name": "馬可波羅", "jajp_name": "マルコ・ポーロ",
        "engb_name": "Marco Polo", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64006, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2021年07月08日"
        },
    "2280030026": {
        "vari_ksid": 2280030026, "zhcn_name": "契卡洛夫", "zhtw_name": "契卡洛夫*", "jajp_name": "チカロフ",
        "engb_name": "Chkalov", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64007, "bool_retr": 0,
        "type_equp": [[86009], [86009], [86008], [86010], [86010]], "onln_date": "2022年07月14日"
        },
    "2280030006": {
        "vari_ksid": 2280030006, "zhcn_name": "路易九世", "zhtw_name": "路易九世", "jajp_name": "サン・ルイ",
        "engb_name": "Saint Louis", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2018年04月26日"
        },
    "2280030017": {
        "vari_ksid": 2280030017, "zhcn_name": "香槟", "zhtw_name": "香檳", "jajp_name": "シャンパーニュ",
        "engb_name": "Champagne", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2020年07月09日"
        },
    "2280030027": {
        "vari_ksid": 2280030027, "zhcn_name": "布雷斯特", "zhtw_name": "佈雷斯特*", "jajp_name": "ブレスト",
        "engb_name": "Brest", "vari_rari": 6, "vari_kstp": "250", "vari_natl": 64008, "bool_retr": 0,
        "type_equp": [[86003, 86011], [86001], [86006], [86010], [86010]], "onln_date": "2022年07月14日"
        },
    "2280030012": {
        "vari_ksid": 2280030012, "zhcn_name": "加斯科涅", "zhtw_name": "加斯科涅", "jajp_name": "ガスコーニュ",
        "engb_name": "Gascogne", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64009, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2019年04月18日"
        },
    "2280040003": {
        "vari_ksid": 2280040003, "zhcn_name": "海伦娜·META", "zhtw_name": "海倫娜·META",
        "jajp_name": "ヘレナ(META)",
        "engb_name": "Helena META", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64100, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年06月10日"
        },
    "2280040011": {
        "vari_ksid": 2280040011, "zhcn_name": "孟菲斯·META", "zhtw_name": "孟菲斯·META*",
        "jajp_name": "メンフィス(META)", "engb_name": "Memphis META", "vari_rari": 4, "vari_kstp": "210",
        "vari_natl": 64100, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2022年05月26日"
        },
    "2280040013": {
        "vari_ksid": 2280040013, "zhcn_name": "特伦托·META", "zhtw_name": "特倫托·META*",
        "jajp_name": "トレント(META)", "engb_name": "Trento META", "vari_rari": 4, "vari_kstp": "220",
        "vari_natl": 64100, "bool_retr": 0, "type_equp": [[86003], [86005], [86006], [86010], [86010]],
        "onln_date": "2022年07月28日"
        },
    "2280040007": {
        "vari_ksid": 2280040007, "zhcn_name": "格奈森瑙·META", "zhtw_name": "格奈森瑙·META*",
        "jajp_name": "グナイゼナウ(META)", "engb_name": "Gneisenau META", "vari_rari": 5, "vari_kstp": "302",
        "vari_natl": 64100, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2021年12月09日"
        },
    "2280040009": {
        "vari_ksid": 2280040009, "zhcn_name": "沙恩霍斯特·META", "zhtw_name": "沙恩霍斯特·META*",
        "jajp_name": "シャルンホルスト(META)", "engb_name": "Scharnhorst META", "vari_rari": 5, "vari_kstp": "302",
        "vari_natl": 64100, "bool_retr": 0, "type_equp": [[86004], [86005], [86006], [86010], [86010]],
        "onln_date": "2022年03月10日"
        },
    "2280040012": {
        "vari_ksid": 2280040012, "zhcn_name": "反击·META", "zhtw_name": "反擊·META*",
        "jajp_name": "レパルス(META)",
        "engb_name": "Repulse META", "vari_rari": 5, "vari_kstp": "302", "vari_natl": 64100, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2022年06月09日"
        },
    "2280040005": {
        "vari_ksid": 2280040005, "zhcn_name": "扶桑·META", "zhtw_name": "扶桑·META",
        "jajp_name": "扶桑(META)",
        "engb_name": "Fusou META", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64100, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2021年10月01日"
        },
    "2280040010": {
        "vari_ksid": 2280040010, "zhcn_name": "山城·META", "zhtw_name": "山城·META",
        "jajp_name": "山城(META)",
        "engb_name": "Yamashiro META", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64100,
        "bool_retr": 0, "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]],
        "onln_date": "2022年04月01日"
        },
    "2280040006": {
        "vari_ksid": 2280040006, "zhcn_name": "飞鹰·META", "zhtw_name": "飛鷹·META",
        "jajp_name": "飛鷹(META)",
        "engb_name": "Hiyou META", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64100, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010, 86015], [86010, 86015]],
        "onln_date": "2021年12月01日"
        },
    "2280040008": {
        "vari_ksid": 2280040008, "zhcn_name": "隼鹰·META", "zhtw_name": "隼鷹·META",
        "jajp_name": "隼鷹(META)",
        "engb_name": "Junyou META", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64100, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010, 86015], [86010, 86015]],
        "onln_date": "2022年02月01日"
        },
    "2280040001": {
        "vari_ksid": 2280040001, "zhcn_name": "飞龙·META", "zhtw_name": "飛龍·META",
        "jajp_name": "飛龍(META)",
        "engb_name": "Hiryuu META", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64100, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2020年12月22日"
        },
    "2280040002": {
        "vari_ksid": 2280040002, "zhcn_name": "皇家方舟·META", "zhtw_name": "皇家方舟·META",
        "jajp_name": "アーク・ロイヤル(META)", "engb_name": "Ark Royal META", "vari_rari": 5, "vari_kstp": "702",
        "vari_natl": 64100, "bool_retr": 0, "type_equp": [[86008], [86008], [86009], [86010], [86010]],
        "onln_date": "2021年03月18日"
        },
    "2280040004": {
        "vari_ksid": 2280040004, "zhcn_name": "苍龙·META", "zhtw_name": "蒼龍·META",
        "jajp_name": "蒼龍(META)",
        "engb_name": "Souryuu META", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64100, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2021年09月09日"
        },
    "2280050001": {
        "vari_ksid": 2280050001, "zhcn_name": "涅普顿", "zhtw_name": "涅普頓*", "jajp_name": "ネプテューヌ",
        "engb_name": "Neptune", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64901, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月06日"
        },
    "2280050002": {
        "vari_ksid": 2280050002, "zhcn_name": "诺瓦露", "zhtw_name": "諾瓦露*", "jajp_name": "ノワール",
        "engb_name": "Noire", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64901, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2018年02月06日"
        },
    "2280050003": {
        "vari_ksid": 2280050003, "zhcn_name": "布兰", "zhtw_name": "布蘭*", "jajp_name": "ブラン",
        "engb_name": "Blanc", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64901, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月06日"
        },
    "2280050004": {
        "vari_ksid": 2280050004, "zhcn_name": "贝露", "zhtw_name": "貝露*", "jajp_name": "ベール",
        "engb_name": "Vert", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64901, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86009], [86010], [86010]], "onln_date": "2018年02月06日"
        },
    "2280050005": {
        "vari_ksid": 2280050005, "zhcn_name": "绀紫之心", "zhtw_name": "紺紫之心*", "jajp_name": "パープルハート",
        "engb_name": "Purple Heart", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64901, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月06日"
        },
    "2280050006": {
        "vari_ksid": 2280050006, "zhcn_name": "圣黑之心", "zhtw_name": "聖黑之心*", "jajp_name": "ブラックハート",
        "engb_name": "Black Heart", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64901, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2018年02月06日"
        },
    "2280050007": {
        "vari_ksid": 2280050007, "zhcn_name": "群白之心", "zhtw_name": "群白之心*", "jajp_name": "ホワイトハート",
        "engb_name": "White Heart", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64901, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年02月06日"
        },
    "2280050008": {
        "vari_ksid": 2280050008, "zhcn_name": "翡绿之心", "zhtw_name": "翡綠之心*", "jajp_name": "グリーンハート",
        "engb_name": "Green Heart", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64901, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86009], [86010], [86010]], "onln_date": "2018年02月06日"
        },
    "2280050031": {
        "vari_ksid": 2280050031, "zhcn_name": "久远", "zhtw_name": "久遠*", "jajp_name": "クオン",
        "engb_name": "Kuon*", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64903, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2018年11月29日"
        },
    "2280050032": {
        "vari_ksid": 2280050032, "zhcn_name": "猫音", "zhtw_name": "貓音*", "jajp_name": "ネコネ",
        "engb_name": "Nekone*", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64903, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年11月29日"
        },
    "2280050033": {
        "vari_ksid": 2280050033, "zhcn_name": "露露缇耶", "zhtw_name": "露露緹耶*", "jajp_name": "ルルティエ",
        "engb_name": "Rurutie*", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64903, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2018年11月29日"
        },
    "2280050034": {
        "vari_ksid": 2280050034, "zhcn_name": "乌璐露", "zhtw_name": "烏璐露*", "jajp_name": "ウルゥル",
        "engb_name": "Uruuru*", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64903, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2018年11月29日"
        },
    "2280050035": {
        "vari_ksid": 2280050035, "zhcn_name": "萨拉娜", "zhtw_name": "薩拉娜*", "jajp_name": "サラァナ",
        "engb_name": "Saraana*", "vari_rari": 4, "vari_kstp": "701", "vari_natl": 64903, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86006], [86010, 86015], [86010, 86015]],
        "onln_date": "2018年11月29日"
        },
    "2280050036": {
        "vari_ksid": 2280050036, "zhcn_name": "芙米露露", "zhtw_name": "芙米露露*", "jajp_name": "フミルィル",
        "engb_name": "Fumiruiru*", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64903, "bool_retr": 0,
        "type_equp": [[86007], [86008], [86008], [86010], [86010]], "onln_date": "2018年11月22日"
        },
    "2280050041": {
        "vari_ksid": 2280050041, "zhcn_name": "绊爱", "zhtw_name": "絆愛*", "jajp_name": "キズナアイ",
        "engb_name": "Kizuna AI", "vari_rari": 4, "vari_kstp": "100", "vari_natl": 64904, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2019年04月26日"
        },
    "2280050042": {
        "vari_ksid": 2280050042, "zhcn_name": "绊爱·Elegant", "zhtw_name": "絆愛·Elegant*",
        "jajp_name": "キズナアイ・エレガント", "engb_name": "Elegant Kizuna AI", "vari_rari": 5, "vari_kstp": "220",
        "vari_natl": 64904, "bool_retr": 0, "type_equp": [[86003], [86001], [86006], [86010], [86010]],
        "onln_date": "2019年04月26日"
        },
    "2280050043": {
        "vari_ksid": 2280050043, "zhcn_name": "绊爱·Anniversary", "zhtw_name": "絆愛·Anniversary*",
        "jajp_name": "キズナアイ・アニバーサリー", "engb_name": "Anniversary Kizuna AI", "vari_rari": 5,
        "vari_kstp": "702", "vari_natl": 64904, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2019年04月26日"
        },
    "2280050044": {
        "vari_ksid": 2280050044, "zhcn_name": "绊爱·SuperGamer", "zhtw_name": "絆愛·SuperGamer*",
        "jajp_name": "キズナアイ・スーパーゲーマー", "engb_name": "Super Gamer Kizuna AI", "vari_rari": 5,
        "vari_kstp": "300", "vari_natl": 64904, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2019年04月26日"
        },
    "2280050061": {
        "vari_ksid": 2280050061, "zhcn_name": "玛莉萝丝", "zhtw_name": "瑪莉蘿絲", "jajp_name": "マリー・ローズ",
        "engb_name": "Marie Rose", "vari_rari": 5, "vari_kstp": "100", "vari_natl": 64906, "bool_retr": 0,
        "type_equp": [[86001], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年11月26日"
        },
    "2280050062": {
        "vari_ksid": 2280050062, "zhcn_name": "穗香", "zhtw_name": "穗香", "jajp_name": "ほのか",
        "engb_name": "Honoka", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64906, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2020年11月26日"
        },
    "2280050063": {
        "vari_ksid": 2280050063, "zhcn_name": "霞", "zhtw_name": "霞", "jajp_name": "かすみ",
        "engb_name": "Kasumi", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64906, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2020年11月26日"
        },
    "2280050064": {
        "vari_ksid": 2280050064, "zhcn_name": "海咲", "zhtw_name": "海咲", "jajp_name": "みさき",
        "engb_name": "Misaki", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64906, "bool_retr": 0,
        "type_equp": [[86002], [86001], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年11月26日"
        },
    "2280050065": {
        "vari_ksid": 2280050065, "zhcn_name": "凪咲", "zhtw_name": "凪咲", "jajp_name": "なぎさ",
        "engb_name": "Nagisa", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64906, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2020年11月26日"
        },
    "2280050066": {
        "vari_ksid": 2280050066, "zhcn_name": "女天狗", "zhtw_name": "女天狗", "jajp_name": "女天狗",
        "engb_name": "Nyotengu", "vari_rari": 4, "vari_kstp": "702", "vari_natl": 64906, "bool_retr": 0,
        "type_equp": [[86007], [86009], [86008], [86010], [86010]], "onln_date": "2020年11月26日"
        },
    "2280050067": {
        "vari_ksid": 2280050067, "zhcn_name": "莫妮卡", "zhtw_name": "莫妮卡", "jajp_name": "モニカ",
        "engb_name": "Monica", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64906, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2020年11月26日"
        },
    "2280050071": {
        "vari_ksid": 2280050071, "zhcn_name": "天海春香", "zhtw_name": "天海春香", "jajp_name": "天海春香",
        "engb_name": "Haruka Amami", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64907, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年07月22日"
        },
    "2280050072": {
        "vari_ksid": 2280050072, "zhcn_name": "如月千早", "zhtw_name": "如月千早", "jajp_name": "如月千早",
        "engb_name": "Chihaya Kisaragi", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64907,
        "bool_retr": 0, "type_equp": [[86007], [86009], [86008], [86010], [86010]],
        "onln_date": "2021年07月22日"
        },
    "2280050073": {
        "vari_ksid": 2280050073, "zhcn_name": "水濑伊织", "zhtw_name": "水瀨伊織", "jajp_name": "水瀬伊織",
        "engb_name": "Iori Minase", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64907, "bool_retr": 0,
        "type_equp": [[86004], [86001], [86006], [86010], [86010]], "onln_date": "2021年07月22日"
        },
    "2280050074": {
        "vari_ksid": 2280050074, "zhcn_name": "三浦 梓", "zhtw_name": "三浦梓", "jajp_name": "三浦あずさ",
        "engb_name": "Azusa Miura", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64907, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2021年07月22日"
        },
    "2280050075": {
        "vari_ksid": 2280050075, "zhcn_name": "秋月律子", "zhtw_name": "秋月律子", "jajp_name": "秋月律子",
        "engb_name": "Ritsuko Akizuki", "vari_rari": 4, "vari_kstp": "540", "vari_natl": 64907,
        "bool_retr": 0, "type_equp": [[86001], [86006], [86010, 86018], [86010, 86018], [86010, 86018]],
        "onln_date": "2021年07月22日"
        },
    "2280050076": {
        "vari_ksid": 2280050076, "zhcn_name": "双海亚美", "zhtw_name": "雙海亞美", "jajp_name": "双海亜美",
        "engb_name": "Ami Futami", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64907, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2021年07月22日"
        },
    "2280050077": {
        "vari_ksid": 2280050077, "zhcn_name": "双海真美", "zhtw_name": "雙海真美", "jajp_name": "双海真美",
        "engb_name": "Mami Futami", "vari_rari": 4, "vari_kstp": "801", "vari_natl": 64907, "bool_retr": 0,
        "type_equp": [[86013], [86013], [86001], [86010], [86010]], "onln_date": "2021年07月22日"
        },
    "2280050081": {
        "vari_ksid": 2280050081, "zhcn_name": "宝多六花", "zhtw_name": "寶多六花", "jajp_name": "宝多六花",
        "engb_name": "Rikka Takarada", "vari_rari": 5, "vari_kstp": "210", "vari_natl": 64908,
        "bool_retr": 0,
        "type_equp": [[86002, 86010], [86005, 86010], [86006, 86010], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年11月25日"
        },
    "2280050082": {
        "vari_ksid": 2280050082, "zhcn_name": "新条茜", "zhtw_name": "新條茜", "jajp_name": "新条アカネ",
        "engb_name": "Akane Shinjo", "vari_rari": 5, "vari_kstp": "300", "vari_natl": 64908, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2021年11月25日"
        },
    "2280050083": {
        "vari_ksid": 2280050083, "zhcn_name": "莲", "zhtw_name": "哈絲", "jajp_name": "はっす",
        "engb_name": "Hass", "vari_rari": 4, "vari_kstp": "210", "vari_natl": 64908, "bool_retr": 0,
        "type_equp": [[86002], [86005], [86006], [86010, 86014], [86010, 86014]],
        "onln_date": "2021年11月25日"
        },
    "2280050084": {
        "vari_ksid": 2280050084, "zhcn_name": "奈美子", "zhtw_name": "奈美子", "jajp_name": "なみこ",
        "engb_name": "Namiko", "vari_rari": 4, "vari_kstp": "220", "vari_natl": 64908, "bool_retr": 0,
        "type_equp": [[86003], [86005], [86006], [86010], [86010]], "onln_date": "2021年11月25日"
        },
    "2280050085": {
        "vari_ksid": 2280050085, "zhcn_name": "南梦芽", "zhtw_name": "南夢芽", "jajp_name": "南夢芽",
        "engb_name": "Yume Minami", "vari_rari": 5, "vari_kstp": "220", "vari_natl": 64908, "bool_retr": 0,
        "type_equp": [[86003], [86001], [86006], [86010], [86010]], "onln_date": "2021年11月25日"
        },
    "2280050086": {
        "vari_ksid": 2280050086, "zhcn_name": "飞鸟川千濑", "zhtw_name": "飛鳥川千瀨",
        "jajp_name": "飛鳥川ちせ",
        "engb_name": "Chise Asukagawa", "vari_rari": 5, "vari_kstp": "702", "vari_natl": 64908,
        "bool_retr": 0, "type_equp": [[86007], [86009], [86008], [86010], [86010]],
        "onln_date": "2021年11月25日"
        },
    "2280050087": {
        "vari_ksid": 2280050087, "zhcn_name": "貉", "zhtw_name": "貉", "jajp_name": "ムジナ",
        "engb_name": "Mujina", "vari_rari": 4, "vari_kstp": "300", "vari_natl": 64908, "bool_retr": 0,
        "type_equp": [[86004], [86001, 86002], [86006], [86010], [86010]], "onln_date": "2021年11月25日"
        }
    }
