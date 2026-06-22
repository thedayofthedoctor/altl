#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL LIB BY MATT BELFAST BROWN
modules.module_Fuel_Calculator — Ship fuel consumption calculation.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2026-06-21
Version: 0.8.0
Mode Create Date: 2020-05-27
Mode Date: 2026-06-21
Mode Version: 1.1.0

THIS PROGRAM IS LICENSED UNDER GPL-3.0 YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2026 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not,
see <https://www.gnu.org/licenses/>.
"""

# Define the base fuel consumption values indexed by ship type tier.
type_bases = [1, 2, 3, 4, 5, 6]
# Define the rarity fuel consumption offset values indexed by rarity tier.
rarity_bases = [0, 1, 2, 3, 4]
# Define the breakthrough fuel consumption penalty values indexed by breakthrough stage.
breakthrough_bases = [0, 2, 4, 6]
# Define the special fuel consumption values for specific outlier ship cases.
special_bases = [7, 9]
# Define the special correction offset values for named ships with adjusted consumption.
special_corrections = [-2, -1, 1]
# Define the list of ship names that receive a special consumption correction.
special_ships = ["夕张", "神风", "多塞特郡", "最上", "三隈", "三笠", "飞鹰", "隼鹰", "半人马", "金刚", "比叡", "天城"]


def lookup_special_correction(ship_name: str) -> int:
    """
    Look up the special fuel consumption correction for a named ship.

    Certain ships in Azur Lane deviate from the standard consumption formula
    and receive a fixed offset. This function returns that offset if the ship
    is on the known special list, or zero otherwise.

    :param ship_name: The name of the ship to check for a special correction.
    :type ship_name: str
    :return: The special correction offset value for the named ship, or zero.
    :rtype: int
    """
    # Check if the given ship name belongs to the first special group receiving a correction of -2.
    if ship_name in ["夕张"]:
        # Return the correction offset for the largest consumption reduction.
        special_offset = special_corrections[0]
    # Check if the given ship name belongs to the second group receiving a correction of -1.
    elif ship_name in ["神风", "多塞特郡", "最上", "三隈", "三笠"]:
        # Return the correction offset for a moderate consumption reduction.
        special_offset = special_corrections[1]
    # Check if the given ship name belongs to the third group receiving a correction of +1.
    elif ship_name in ["飞鹰", "隼鹰", "半人马", "金刚", "比叡", "天城"]:
        # Return the correction offset for a mild consumption increase.
        special_offset = special_corrections[2]
    # The ship name does not appear on any special correction list.
    else:
        # Return zero indicating no special correction applies.
        special_offset = 0
    # Return the computed special correction value to the caller.
    return special_offset


def calculate_base_consumption(ship_type: str, ship_rarity: str, ship_name: str) -> int:
    """
    Calculate the base level-one-zero-breakthrough fuel consumption for a Kansen.

    Derives the fuel consumption by combining the ship type base value, rarity
    offset, and an optional special correction for named ships. This represents
    the consumption at level 100 with zero breakthroughs.

    :param ship_type: The hull type code string such as DD, CL, CA, CV, BC, or BB.
    :type ship_type: str
    :param ship_rarity: The rarity label string in Chinese such as 普通, 稀有, 精锐, 超稀有, or 海上传奇.
    :type ship_rarity: str
    :param ship_name: The name of the ship to check for a special consumption correction.
    :type ship_name: str
    :return: The base fuel consumption value for the given ship at level 100 without breakthroughs.
    :rtype: int
    """
    # Determine the ship type tier index based on the hull classification code.
    if ship_type == "DD":
        # Destroyers have the lowest type tier index.
        type_index = 0
    # Check for light cruiser, monitor, and repair ship types sharing the same tier.
    elif ship_type in ["CL", "MN", "MT"]:
        # Light cruisers and related auxiliaries share the second tier index.
        type_index = 1
    # Check for heavy cruiser and light carrier types sharing the same tier.
    elif ship_type in ["CA", "CVL"]:
        # Heavy cruisers and light carriers share the third tier index.
        type_index = 2
    # Check for the standard fleet carrier type.
    elif ship_type == "CV":
        # Fleet carriers occupy the fourth tier index.
        type_index = 3
    # Check for the battlecruiser type.
    elif ship_type == "BC":
        # Battlecruisers occupy the fifth tier index.
        type_index = 4
    # Check for the battleship type.
    elif ship_type == "BB":
        # Battleships occupy the sixth and highest tier index.
        type_index = 5
    # The ship type code is unrecognized; default to the lowest tier.
    else:
        # Assign zero as a safe fallback for unknown hull classifications.
        type_index = 0
    # Determine the rarity tier index based on the Chinese rarity label string.
    if ship_rarity == "普通":
        # Normal rarity occupies the lowest tier index.
        rarity_index = 0
    # Check for the rare rarity label.
    elif ship_rarity == "稀有":
        # Rare occupies the second tier index.
        rarity_index = 1
    # Check for the elite rarity label.
    elif ship_rarity == "精锐":
        # Elite occupies the third tier index.
        rarity_index = 2
    # Check for super rare or Top Solution plan rarity labels.
    elif ship_rarity in ["超稀有", "最高方案"]:
        # Super rare and Top Solution share the fourth tier index.
        rarity_index = 3
    # Check for Ultra Rare or Decisive Plan rarity labels.
    elif ship_rarity in ["海上传奇", "决战方案"]:
        # Ultrarare and Decisive Plan share the fifth and highest tier index.
        rarity_index = 4
    # The rarity label is unrecognized; default to the lowest tier.
    else:
        # Assign zero as a safe fallback for unknown rarity labels.
        rarity_index = 0
    # Check whether the ship qualifies for a special consumption correction.
    if ship_name in special_ships:
        # Look up the correction value for the specially listed ship name.
        special_offset = lookup_special_correction(ship_name)
    # The ship does not appear on the special correction list.
    else:
        # Assign zero correction for ships with standard consumption profiles.
        special_offset = 0
    # Look up the base fuel value for the determined ship type tier.
    type_base = type_bases[type_index]
    # Look up the fuel offset value for the determined rarity tier.
    rarity_base = rarity_bases[rarity_index]
    # Sum type base, rarity offset, and special correction, then cast to integer.
    base_consumption = int(type_base + rarity_base + special_offset)
    # Return the computed base consumption value for the caller.
    return base_consumption


def calculate_surface_consumption(is_plan: bool, breakthrough_stage: int, ship_kind: str, ship_type: str, ship_rarity: str, ship_name: str, ship_level: int) -> int:
    """
    Calculate the final fuel consumption for a surface Kansen at its current state.

    Combines the base consumption with breakthrough penalties, level scaling,
    and a surface or submarine type factor. Plan ships receive a fixed
    breakthrough penalty regardless of their actual breakthrough level.

    :param is_plan: Whether the ship is a research plan ship receiving a fixed breakthrough penalty.
    :type is_plan: bool
    :param breakthrough_stage: The current breakthrough stage of the ship, ranging from 0 to 3.
    :type breakthrough_stage: int
    :param ship_kind: The operational domain string, either Surface or Submarine.
    :type ship_kind: str
    :param ship_type: The hull type code string such as DD, CL, or BB.
    :type ship_type: str
    :param ship_rarity: The rarity label string in Chinese.
    :type ship_rarity: str
    :param ship_name: The name of the ship for special correction lookup.
    :type ship_name: str
    :param ship_level: The current level of the ship capped internally at 99.
    :type ship_level: int
    :return: The final fuel consumption value for the ship in its current state.
    :rtype: int
    """
    # Determine the breakthrough penalty tier based on the breakthrough stage.
    if breakthrough_stage == 0:
        # No breakthroughs yield the lowest penalty tier index.
        breakthrough_index = 0
    # Check if the ship has exactly one breakthrough stage.
    elif breakthrough_stage == 1:
        # One breakthrough yields the second penalty tier index.
        breakthrough_index = 1
    # Check if the ship has exactly two breakthrough stages.
    elif breakthrough_stage == 2:
        # Two breakthroughs yield the third penalty tier index.
        breakthrough_index = 2
    # Check if the ship has three or more breakthrough stages.
    elif breakthrough_stage == 3:
        # Three breakthroughs yield the highest penalty tier index.
        breakthrough_index = 3
    # The breakthrough stage is unrecognized; default to the lowest tier.
    else:
        # Assign zero index as a safe fallback for invalid breakthrough values.
        breakthrough_index = 0
    # Override the breakthrough index for plan ships regardless of actual breakthrough stage.
    if is_plan:
        # Plan ships always receive the maximum breakthrough fuel penalty.
        breakthrough_index = 3
    # Plan ship flag is not set; retain the computed breakthrough index.
    else:
        # The breakthrough index remains unchanged for non-plan ships.
        breakthrough_index += 0
    # Look up the breakthrough fuel penalty value from the penalty table.
    breakthrough_penalty = breakthrough_bases[breakthrough_index]
    # Compute the base fuel consumption for the ship without breakthrough modifiers.
    base_consumption = calculate_base_consumption(ship_type, ship_rarity, ship_name)
    # Determine the operational domain factor based on surface or submarine classification.
    if ship_kind == "Surface":
        # Surface ships receive a unit domain factor for the consumption formula.
        domain_factor = 1
    # The ship is a submarine or has an unrecognized domain classification.
    else:
        # Non-surface ships receive a zero domain factor in this context.
        domain_factor = 0
    # Compute the final consumption using the level-scaled formula with all modifiers.
    final_consumption = int(int(domain_factor + (base_consumption * (0.5 + min(ship_level, 99)) * 0.05)) + breakthrough_penalty)
    # Return the computed final fuel consumption to the caller.
    return final_consumption


def calculate_submarine_fuel(submarine_count: int, move_count: int) -> int:
    """
    Calculate the fuel consumption for deploying submarines across a given number of map cells.

    Applies a linear formula with a small floor correction to determine the
    fuel cost based on the number of submarines in the formation and the
    distance traveled in grid cells.

    :param submarine_count: The number of submarines in the deployed formation.
    :type submarine_count: int
    :param move_count: The number of map grid cells the submarine fleet moves across.
    :type move_count: int
    :return: The fuel consumption value for the submarine movement operation.
    :rtype: int
    """
    # Compute the submarine fuel cost using the game formula with a micro-adjustment for floor behavior.
    submarine_fuel = int(1.1 * submarine_count * move_count - 0.00001) + 1
    # Return the computed submarine fuel consumption to the caller.
    return submarine_fuel
