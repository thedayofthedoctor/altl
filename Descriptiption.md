<h1 align="center"> Azur Lane Tool Lib </h1>
<h4 align="center">Tools lib for Azur Lane which game powered by ManJiu Shanghai.
Accelerating library iteration.</h4>
<p  align="center">
<a href="https://pypi.org/manage/project/AzurLaneToolLib/release/0.8.0/"><img src="https://img.shields.io/pypi/v/azurlanetoollib"></a>
<a href="https://www.gnu.org/licenses/quick-guide-gplv3.zh-cn.html"><img src="https://img.shields.io/pypi/l/azurlanetoollib?color=green"></a>
<img src="https://img.shields.io/pypi/dd/azurlanetoollib?color=yellow">
</p>
<hr />

# AzurLaneToolLib

Tools lib for Azur Lane which game powered by ManJiu Shanghai.
Accelerating library iteration.  
***Due to changes in the game itself, this tool library will also modify the original update content.***

## Copyright Information

### LICENSE

> Copyright (C) 2019 - 2026 Matt Belfast Brown
>
> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
> License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
> version.
>
> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
> warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
>
> You should have received a copy of the GNU General Public License along with this program. If not,
> see <https://www.gnu.org/licenses/> .

### Author

#### Author Information

> Author: ***Matt Belfast Brown*** or *Matt Brown* or *M.B.B.*（ **Name in English** ）
>> Also be called ***The Day of The Doctor*** ( **Network Nickname** )  
> > ***鈴木夢美*** or ***伊藤京介*** ( **Name in Japanese** )  
> > ***沈永基***，***皓月***，***飞瀑山人***，***衍枫阁主人*** ( **Name in Chinese, Style Name, Pseudonym, Alias** )

#### Contact Details

> E-mail: ***thedayofthedo@gmail.com*** or ***thedayofthedoctor@foxmail.com***   
> TEL:\+86-15841486187
>
> Address: **Room 313, Apartment No. 14, South District, South Campus, Northwest A&F University, No. 22, Xinong Road,
Litai Street, Yangling District, Shaanxi Province, China**  
> Address: ***中国陕西省杨凌区李台街道西农路22号西北农林科技大学南校区南区14号公寓313宿舍***

# What will add next

> * 各类型武器CD
> * 零散经验相关
> * 部分战斗用计算
> * 属性计算

# Version Log

## Version Information

> First Edition Time: 2019-07-11  
> Last Revision Time: 2026-06-21  
> Version Number: 0.8.0

## Update Log

| Release Version |    Status     |  Release Date  | Update Info                                   | 
|----------------:|:-------------:|:--------------:|:----------------------------------------------|
|       **0.8.0** | ***working*** | ***2026-06-21*** | ***Restructured project, JSON data, pyproject.toml, CLASP-3.1 preparation.*** |
|           0.7.0 |    working    |     future     | Adapt to changes in the current game version. |
|       **0.6.4** | **available** | **2023-03-08** | **Write documents and improve information.**  |
|           0.6.3 |   available   |   2023-03-08   | Write documents and improve information.      |
|           0.6.2 |   available   |   2023-03-05   | Fixed some errors.                            |
|           0.6.1 |   available   |   2023-03-05   | Add mode ` mode_ SRS_ Ptl.py`.                |
|           0.6.0 |   available   |   2022-10-20   | Re planned version number                     |                                     |
|         0.5.3.1 |   available   |   2022-09-13   | Update new kansen name.                       |
|           0.5.3 |   available   |   2022-03-27   | Add and correct all comments.                 |
|           0.5.2 |   available   |   2022-03-26   | Full mode for FCS_Cal.                        |
|           0.5.1 |   available   |   2022-02-22   | New mode and new algorithm.                   |
|         0.5.1a2 |   available   |   2022-02-18   | Test for 0.5.1 and new md.                    |
|          before |   available   |     before     | before                                        |

## Version Update Information

### 0.8.0

+ Renamed `mode/` directory to `modules/`.
+ Renamed all `mode_*.py` to `module_*.py` with descriptive Pascal_Snake naming.
+ Replaced `data/data_AZR_Lan.py` with `details/detail_*.json` (5 JSON files, PascalCase keys).
+ Removed deprecated modules: `mode_SRS_Ptl.py`, `module_Fleet_Tool.py`.
+ Added `pyproject.toml` with modern build configuration.
+ Raised Python requirement to `>=3.9,<=3.14`.
+ Switched to `importlib.resources.files()` for package data access.
+ CLASP-3.1 compliance: all modules renamed, abbreviated names replaced, line-by-line comments added.
+ Renamed `module_Commander_Calculate` → `module_Commander_Calculator`.
+ Renamed `module_Experience_Calculate` → `module_Experience_Calculator`.
+ Renamed `module_Fuel_Consumption_Calculate` → `module_Fuel_Calculator`.
+ Renamed `module_Blueprint_Calculate` → `module_Blueprint_Calculator`.
+ Renamed `module_Miscellaneous_Calculate` → `module_Bonus_Calculator`.
+ Created `DetailLoader` class with lazy-loading JSON data access.

### 0.7.0

+ Adapt to changes in the current game version.

### 0.6.4

+ Add "HeXie" Kansen Name

### 0.6.3

+ Write documents
+ Improve information

### 0.6.2

+ Fixed some errors

### 0.6.1

+ Complete data verification
+ Complete Module ` mode_SRS_Ptl.py`
+ Fixed some errors

### 0.6.0

+ Re-planned version number
+ Revised ship data
+ New Data File ` data_AZR_Lan.py`
+ Delete Original Data ` data_FLE_Shi.py`
+ New Incomplete Module ` mode_SRS_Ptl.py` (**original author:tianqianzhiyang**)

### 0.5.3.1

- Add new Kansen name.

### 0.5.3

+ Add and correct all comments.
+ Fixed some errors.

### 0.5.2

- Complete the full mode of `mode_FCS_Cal.py`.
- Some comments have been modified.

### 0.5.1

+ Edit `mode_FCS_Cal.py` for complete the most basic functions.
+ function `fun_bsdg_fuca`, `fun_kstp_scco`, `fun_sfks_fuca` is available.
+ It can calculate the fuel consumption of surface kansens.

### 0.5.1a2

+ Add new mode from Azur Lane Fleet  (**author: x94fujo6rpg**).
+ Rewrite file `setup.py`.
+ Try adding a document.
