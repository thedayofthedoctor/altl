# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL BY MATT BELFAST BROWN
mode_KSN_Com.py - The core mode of the Azur Lane Tool.

Author: Matt Belfast Brown
Create Date: 2021-07-10
Version Date: 2022-03-26
Version: 0.5.2
Mode Create Date: 2020-10-07
Mode Date: 2022-02-15
Mode Version: 1.0.0

THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2021-2022 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


# define function
def fun_ksen_nmco(vari_ksip: str) -> str:
    """
    此函数用于查询和谐的舰船名称包括日本及美国舰船.
    This function is used to query harmonious ship names including Japanese and American ships.
    :param vari_ksip: 查询内容. Query content.
    :return vari_knrs: 查询结果. Search result.
    """
    if vari_ksip not in list_ksnc + list_ksnm:
        vari_knrs = '查找内容无效，请检验输入内容，或检查更新！'
    else:
        vari_knrs = ''
        for para_lsor in range(len(list_ksnm)):
            if vari_ksip == list_ksnm[para_lsor]:
                vari_knrs = '舰船名：' + vari_ksip + '，对应代号:' + list_ksnc[para_lsor]
            elif vari_ksip == list_ksnc[para_lsor]:
                vari_knrs = '舰船名：' + list_ksnm[para_lsor] + '，对应代号:' + vari_ksip
            else:
                vari_knrs = '查找内容无效，请检验输入内容，或检查更新！'
    return vari_knrs


# define list
list_ksnm = ['峰风', '神风', '朝风', '春风', '松风', '旗风', '追风', '夕凪', '睦月', '如月', '卯月', '水无月', '文月', '长月', '三日月', '吹雪', '白雪',
             '初雪', '深雪', '浦波', '绫波', '敷波', '曙', '涟', '潮', '晓', '响', '雷', '电', '初春', '若叶', '初霜', '有明', '夕暮', '白露', '时雨',
             '夕立', '海风', '山风', '江风', '凉风', '朝潮', '大潮', '满潮', '荒潮', '霞', '阳炎', '不知火', '黑潮', '亲潮', '初风', '雪风', '天津风',
             '浦风', '矶风', '滨风', '谷风', '野分', '岚', '萩风', '舞风', '夕云', '卷云', '风云', '长波', '卷波', '清波', '秋月', '初月', '凉月',
             '新月JP', '冬月', '春月', '宵月', '满月', '花月', '岛风', '樫野', '天龙', '龙田', '球磨', '北上', '大井', '长良', '五十铃', '由良', '鬼怒',
             '阿武隈', '夕张', '川内', '神通', '那珂', '阿贺野', '能代', '矢矧', '大淀', '古鹰', '加古', '青叶', '衣笠', '最上', '三隈', '铃谷', '熊野',
             '利根', '筑摩', '妙高', '那智', '足柄', '羽黑', '高雄', '爱宕', '摩耶', '鸟海', '金刚', '比叡', '榛名', '雾岛', '天城', '敷岛', '三笠', '扶桑',
             '山城', '伊势', '日向', '长门', '陆奥', '土佐', '纪伊', '骏河', '大和', '武藏', '凤翔', '龙骧', '祥凤', '瑞凤', '千岁', '千代田', '大鲸',
             '龙凤', '飞鹰', '隼鹰', '赤城', '加贺', '苍龙', '飞龙', '翔鹤', '瑞鹤', '大凤', '云龙', '葛城', '信浓', '白龙', '明石', '伊吹', '出云', '北风',
             '吾妻', '伊9', '伊13', '伊16', '伊19', '伊25', '伊26', '伊54', '伊56', '伊58', '伊60', '伊168', '伊490', '新泽西', '提康德罗加',
             '博伊西', '旧金山', '射水鱼', '莫里森']
list_ksnc = ['樱', '榊', '櫂', '橪', '棡', '樋', '椎', '枳', '松', '樟', '楙', '杌', '橗', '枨', '檧', '桐', '杉', '杨', '梧', '朴', '柚',
             '柿', '棪', '槿', '槟', '枫', '栀', '梓', '柏', '梅', '楉', '檨', '榎', '棭', '梿', '栴', '椿', '菪', '杣', '茳', '莨', '棹',
             '荙', '樠', '栘', '蕸', '萩', '蒲', '蓉', '藮', '菙', '莲', '菡', '槆', '柉', '樇', '栭', '苓', '萍', '莵', '蒠', '茭', '荨',
             '枟', '苌', '棬', '棈', '椛', '檚', '栎', '枥', '㮔', '桸', '楛', '槾', '榵', '芒', '㭴', '豺', '豹', '熊', '狸', '獾', '貊',
             '貉', '㹨', '猤', '貃', '狐', '貆', '貎', '豻', '豼', '貅', '貁', '淀', '狼', '狌', '犹', '猅', '猨', '狻', '狺', '猁', '猑',
             '狘', '獌', '狏', '狳', '犰', '獒', '犬', '犮', '猋', '鲤', '鲟', '鲑', '鳗', '鳐', '鲙', '鲐', '魟', '鲼', '鳌', '螯', '鲨',
             '鲛', '䲠', '鲣', '鲪', '鲸', '鳄', '凤', '枭', '鹞', '鹳', '鹂', '鹃', '迖', '鸗', '鸱', '鸢', '凰', '鸾', '蛟', '龙', '鹬',
             '鹤', '鹩', '靇', '鹖', '鵗', '鹫', '茗', '峦', '侌', '苝', '猉', '玖', '十纱', '伊知梦', '衣玖', '双叶檎', '双叶梦', '冴诗', '冴梦',
             '冴矢', '六重', '伊吕波', '诗玖玲', '花园', '卡莉永', '树城', '雾城', '喷水鱼', '赛普拉斯']
