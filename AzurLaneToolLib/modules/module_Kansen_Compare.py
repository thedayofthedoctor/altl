#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL LIB BY MATT BELFAST BROWN
modules.module_Kansen_Compare — Harmonized ship name lookup and comparison.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2026-06-21
Version: 0.8.0
Mode Create Date: 2020-10-07
Mode Date: 2026-06-21
Mode Version: 2.0.0

THIS PROGRAM IS LICENSED UNDER GPL-3.0 YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2026 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not,
see <https://www.gnu.org/licenses/>.
"""

# Define the list of original Japanese, American, and other ship names before harmonization.
original_names = [
    # Begin the list of original Japanese ship names with the first group of entries.
    "电", "岚", "响", "晓", "涟", "雷", "潮", "霞", "曙", "三笠", "三隈", "土佐", "大山", "大井",
    # Continue the list entries on the following line.
    "大凤", "大和", "大淀", "大潮", "大鲸", "山风", "山城", "千岁", "川内", "夕云", "夕立", "夕凪",
    # Continue the list entries on the following line.
    "夕张", "夕暮", "飞龙", "飞鹰", "天龙", "天城", "云龙", "云仙", "木津", "比叡", "日向", "长门",
    # Continue the list entries on the following line.
    "长月", "长良", "长波", "风云", "凤翔", "文月", "古鹰", "龙凤", "龙田", "龙骧", "北上", "北风",
    # Continue the list entries on the following line.
    "由良", "矢矧", "白凤", "白龙", "白雪", "白露", "卯月", "冬月", "鸟海", "出云", "加古", "加贺",
    # Continue the list entries on the following line.
    "有明", "伊吹", "伊势", "名取", "名寄", "衣笠", "江风", "那珂", "那智", "阳炎", "如月", "羽黑",
    # Continue the list entries on the following line.
    "纪伊", "扶桑", "赤城", "花月", "苍龙", "吾妻", "矶风", "时雨", "足柄", "吹雪", "利根", "近江",
    # Continue the list entries on the following line.
    "谷风", "岛风", "初月", "初风", "初春", "初雪", "初霜", "尾张", "陆奥", "妙风", "妙高", "武藏",
    # Continue the list entries on the following line.
    "青叶", "若月", "若叶", "松风", "明石", "金刚", "卷云", "卷波", "浅间", "春月", "春风", "荒潮",
    # Continue the list entries on the following line.
    "秋月", "信浓", "鬼怒", "追风", "亲潮", "神风", "神通", "峰风", "铃谷", "隼鹰", "爱宕", "高雄",
    # Continue the list entries on the following line.
    "凉月", "凉风", "凉波", "浦风", "浦波", "酒匂", "海风", "宵月", "祥凤", "能代", "骏河", "球磨",
    # Continue the list entries on the following line.
    "雪风", "野分", "清波", "深雪", "绫波", "绫濑", "葛城", "萩风", "朝风", "朝凪", "朝潮", "最上",
    # Continue the list entries on the following line.
    "黑潮", "筑摩", "翔鹤", "瑞凤", "瑞鹤", "雾岛", "睦月", "新月", "满月", "满潮", "滨风", "榛名",
    # Continue the list entries on the following line.
    "舞风", "旗风", "熊野", "樫野", "敷岛", "敷波", "摩耶", "藤波", "三日月", "千代田", "天津风", "五十铃",
    # Continue the list entries on the following line.
    "不知火", "水无月", "水无濑", "四万十", "阿武隈", "阿贺野", "渡良濑", "扎拉", "皮劳", "亚德", "约克",
    # Continue the list entries on the following line.
    "易北", "罗恩", "威悉", "科隆", "奥丁", "巴劳鱵", "旧金山", "吕佐夫", "衣阿华", "兴登堡", "纽伦堡",
    # Continue the list entries on the following line.
    "图林根", "哈尔滨", "美因茨", "埃尔宾", "埃吉尔", "埃姆登", "莱比锡", "莫里森", "俾斯麦", "射水鱼",
    # Continue the list entries on the following line.
    "博伊西", "新泽西", "德意志", "马格德堡", "布吕歇尔", "让·巴尔", "圣地亚哥", "杜伊斯堡", "英格拉罕",
    # Continue the list entries on the following line.
    "欧根亲王", "柯尼斯堡", "格奈森瑙", "梅克伦堡", "提尔比茨", "雷根斯堡", "塞德利茨", "赫尔戈兰", "德累斯顿",
    # Continue the list entries on the following line.
    "乌尔里希·冯·胡滕", "布伦希尔德", "卡尔斯鲁厄", "弗里茨·鲁梅", "齐柏林伯爵", "希佩尔海军上将", "沙恩霍斯特",
    # Continue the list entries on the following line.
    "阿达尔伯特亲王", "彼得·史特拉塞", "舍尔海军上将", "莫里茨亲王", "海因里希亲王", "菲利克斯·舒尔茨", "提康德罗加",
    # Continue the list entries on the following line.
    "斯佩伯爵海军上将", "葛兹·冯·伯利欣根", "奥古斯特·冯·帕塞瓦尔", "奥托·冯·阿尔文斯莱本", "腓特烈·卡尔", "腓特烈大帝",
    # Continue the list entries on the following line.
    "鲁普雷希特亲王", "曾克海军上将", "德弗林格尔", "伊9", "伊13", "伊16", "伊19", "伊25", "伊26",
    # Continue the list entries on the following line.
    "伊54", "伊56", "伊58", "伊60", "伊168", "伊404", "伊490", "Z1", "Z2", "Z5", "Z9",
    # Continue the list entries on the following line.
    "Z11", "Z12", "Z13", "Z14", "Z15", "Z16", "Z17", "Z18", "Z19", "Z20",
    # Continue the list entries on the following line.
    "Z21", "Z22", "Z23", "Z24", "Z25", "Z26", "Z28", "Z35", "Z36", "Z43",
    # Continue the list entries on the following line.
    "Z46", "Z47", "Z52", "U-31", "U-37", "U-47", "U-73", "U-81", "U-96",
    # Continue the list entries on the following line.
    "U-101", "U-110", "U-410", "U-522", "U-552", "U-556", "U-557", "U-1206",
    # Continue the list entries on the following line.
    "U-2501"
    # End of the list.
]

# Define the list of harmonized replacement names corresponding positionally to original_names.
harmonized_names = [
    # Begin the list of harmonized replacement names with the first group of entries.
    "柏", "萍", "栀", "枫", "槿", "梓", "槟", "蕸", "棪", "鲐", "狻", "䲠", "鳝", "獾", "鹩",
    # Continue the list entries on the following line.
    "鲸", "淀", "荙", "迖", "杣", "鲼", "鹂", "貆", "茭", "椿", "枳", "狐", "棭", "龙", "鸱",
    # Continue the list entries on the following line.
    "豺", "鳐", "靇", "猃", "貘", "鲟", "螯", "鲨", "枨", "貊", "苌", "枟", "凤", "橗", "狼",
    # Continue the list entries on the following line.
    "鸗", "豹", "枭", "狸", "苝", "㹨", "貁", "䳆", "鹫", "杉", "梿", "楙", "㮔", "猋", "侌",
    # Continue the list entries on the following line.
    "狌", "鸾", "榎", "峦", "鳌", "猽", "貀", "猅", "茳", "豻", "狏", "萩", "樟", "犰", "鲣",
    # Continue the list entries on the following line.
    "魟", "凰", "榵", "蛟", "猉", "柉", "栴", "狳", "桐", "猑", "鳉", "栭", "芒", "檚", "菙",
    # Continue the list entries on the following line.
    "梅", "杨", "檨", "鳂", "鲛", "杪", "獌", "鳄", "犹", "若", "楉", "棡", "茗", "鲤", "荨",
    # Continue the list entries on the following line.
    "棬", "猏", "桸", "橪", "栘", "椛", "鵗", "猤", "椎", "藮", "榊", "貎", "樱", "狺", "鸢",
    # Continue the list entries on the following line.
    "犬", "獒", "栎", "莨", "椋", "槆", "朴", "貄", "菪", "楛", "鹞", "貅", "鲪", "熊", "莲",
    # Continue the list entries on the following line.
    "苓", "棈", "梧", "柚", "狑", "鹖", "莵", "櫂", "桎", "棹", "猨", "蓉", "狘", "鹬", "鹳",
    # Continue the list entries on the following line.
    "鹤", "鳗", "松", "枥", "槾", "樠", "樇", "鲑", "蒠", "樋", "猁", "㭴", "鲙", "柿", "犮",
    # Continue the list entries on the following line.
    "藤", "檧", "鹃", "菡", "貉", "蒲", "杌", "鼯", "虒", "貃", "豼", "獭", "扎达尔", "宝拉",
    # Continue the list entries on the following line.
    "阿黛尔", "伊冯娜", "埃尔斯贝特", "艾伯塔", "威尔玛", "克劳迪亚", "沃登", "鱵", "雾城", "露西", "霍克艾",
    # Continue the list entries on the following line.
    "希尔德加德", "诺菈", "特鲁德", "滨江", "米兹", "埃尔薇菈", "埃格妮丝", "埃玛", "莉普莎", "塞普拉斯",
    # Continue the list entries on the following line.
    "奥德莉亚", "喷水鱼", "树城", "花园", "亚勒玛妮亚", "马格达莱娜", "布丽吉特", "简·布罗伊", "圣戴安娜",
    # Continue the list entries on the following line.
    "多琳妮娅", "格拉哈姆", "萨沃伊亲王", "阿尔伯缇娜", "奥古斯塔", "梅克琳达", "阿尔芙莉达", "瑞吉娜", "桑德菈",
    # Continue the list entries on the following line.
    "赫娜洛蕾", "迪特林德", "乌尔里克·冯·胡贝尔", "贝尔莎", "夏璐尔", "菲莉西娅·鲁梅", "海拉伯爵", "芙兰希卡",
    # Continue the list entries on the following line.
    "格尔林德", "阿德莉娅亲王", "佩特菈·斯坦贝瑟", "席勒", "莫琳亲王", "赫莉米娜亲王", "弗郎西斯卡·舒伯特", "卡莉永",
    # Continue the list entries on the following line.
    "休贝塔伯爵", "戈达·冯·贝格海姆", "奥斯特雷德·冯·帕赫贝尔", "奥莉薇娅·冯·阿诺德", "腓德雷卡·卡尔", "腓德雷卡大帝",
    # Continue the list entries on the following line.
    "蕾贝卡亲王", "泽特", "多萝泰娅", "玖", "十纱", "伊知梦", "衣玖", "双叶檎", "双叶梦", "冴诗", "冴梦",
    # Continue the list entries on the following line.
    "冴矢", "六重", "伊吕波", "诗玲寺", "诗玖玲", "莉泽洛特", "格尔达", "保拉", "沃尔普加", "伯莎", "埃丽卡",
    # Continue the list entries on the following line.
    "埃丝特", "弗蕾娜", "埃丽莎", "弗蕾德贡", "迪特琳德", "汉娜", "赫尔米娜", "卡洛琳", "威尔赫米娜", "安妮特",
    # Continue the list entries on the following line.
    "妮米", "妮丝", "妮可", "妮露", "妮娅", "咪菓", "咪露", "希咪", "希露", "希娜", "柯妮", "优咪伊",
    # Continue the list entries on the following line.
    "优米娜", "优希娜", "优娜米", "优哈依", "优玖露", "优伊欧伊", "优伊伊丽", "优斯伊丽", "优柯妮妮", "优可可妮",
    # Continue the list entries on the following line.
    "优可可洛", "优可可娜", "优伊妮欧露", "优妮可欧伊"
    # End of the list.
]


def lookup_harmonized_name(query_text: str) -> str:
    """
    Look up the harmonized or original name for a given ship name query.

    Searches both the original and harmonized name lists and returns a
    formatted result string showing the original name paired with its
    harmonized counterpart, or an error message if the query is not found.

    :param query_text: The ship name string to search for in either name list.
    :type query_text: str
    :return: A formatted result string with the original and harmonized names, or an error message.
    :rtype: str
    """
    # Check if the query text appears in the union of original and harmonized name lists.
    if query_text not in original_names + harmonized_names:
        # The query was not found in either list; return the localized error message.
        search_result = "查找内容无效，请检验输入内容，或检查更新！"
    # The query exists in at least one of the two name lists.
    else:
        # Initialize the result string to empty before scanning the lists.
        search_result = ""
        # Scan the original names list to find a matching entry by index.
        for list_position in range(len(original_names)):
            # Check if the query matches the original name at the current list position.
            if query_text == original_names[list_position]:
                # Format the result with the original name and its harmonized counterpart.
                search_result = "舰船原名：" + query_text + "，修正名称:" + harmonized_names[list_position]
                # Stop scanning immediately since a match was found.
                break
            # Otherwise check if the query matches the harmonized name at the current list position.
            elif query_text == harmonized_names[list_position]:
                # Format the result with the original name and the queried harmonized name.
                search_result = "舰船原名：" + original_names[list_position] + "，修正名称:" + query_text
                # Stop scanning immediately since a match was found.
                break
            # The current position does not match either list; continue scanning or fall through.
            else:
                # Set the result to the error message for the fallback case in the loop.
                search_result = "查找内容无效，请检验输入内容，或检查更新！"
    # Return the lookup result entered to the caller.
    return search_result
