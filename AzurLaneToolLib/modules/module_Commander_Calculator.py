#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL LIB BY MATT BELFAST BROWN
modules.module_Commander_Calculator — Commander level-up experience calculation.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2026-06-21
Version: 0.8.0
Mode Create Date: 2019-08-10
Mode Date: 2026-06-22
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


def calculate_level_multiplier(commander_level: int) -> int:
    """
    Compute the experience parameter multiplier for a given commander level.

    The multiplier follows piecewise rules that vary by level bracket,
    applying integer division, linear scaling, or fixed values depending
    on the level range. Levels outside the defined brackets yield zero.

    :param commander_level: The current commander level for which to compute the multiplier.
    :type commander_level: int
    :return: The experience parameter multiplier for this commander level.
    :rtype: int
    """
    # Check if the commander is at the initial level one with a fixed multiplier.
    if commander_level == 1:
        # Assign the fixed multiplier value for level one.
        level_multiplier = 1
    # Check if the commander is in the low-level bracket from 2 through 50.
    elif 2 <= commander_level <= 50:
        # Apply integer division by three for this bracket range.
        level_multiplier = (commander_level + 1) // 3
    # Check if the commander is in the mid-low bracket from 51 through 70.
    elif 51 <= commander_level <= 70:
        # Apply integer division by two for this bracket range.
        level_multiplier = (commander_level + 1) // 2
    # Check if the commander is in the mid bracket from 71 through 90.
    elif 71 <= commander_level <= 90:
        # Return the level plus one directly for this bracket range.
        level_multiplier = commander_level + 1
    # Check if the commander is in the mid-high bracket from 91 through 110.
    elif 91 <= commander_level <= 110:
        # Apply a doubling multiplier for this bracket range.
        level_multiplier = (commander_level + 1) * 2
    # Check if the commander is in the high bracket from 111 through 120.
    elif 111 <= commander_level <= 120:
        # Apply a tripling multiplier for this bracket range.
        level_multiplier = (commander_level + 1) * 3
    # Check if the commander is in the very-high bracket from 121 through 130.
    elif 121 <= commander_level <= 130:
        # Apply triple the level directly for this bracket range.
        level_multiplier = 3 * commander_level
    # Check if the commander is in the ultra-high bracket from 131 through 150.
    elif 131 <= commander_level <= 150:
        # Apply quadruple the level directly for this bracket range.
        level_multiplier = 4 * commander_level
    # Check if the commander is in the extreme bracket from 151 through 170.
    elif 151 <= commander_level <= 170:
        # Apply quintuple the level directly for this bracket range.
        level_multiplier = 5 * commander_level
    # Check if the commander is in the top bracket from 171 through 190.
    elif 171 <= commander_level <= 190:
        # Apply sextuple the level directly for this bracket range.
        level_multiplier = 6 * commander_level
    # Check if the commander is in the penultimate bracket from 191 up to 200.
    elif 191 <= commander_level < 200:
        # Apply septuple the level directly for this bracket range.
        level_multiplier = 7 * commander_level
    # The level falls outside all defined brackets; produce a zero multiplier.
    else:
        # Assign zero for unrecognized or out-of-range commander levels.
        level_multiplier = 0
    # Cast the computed floating-point value to an integer before returning.
    level_multiplier = int(level_multiplier)
    # Return the final integer multiplier to the caller.
    return level_multiplier


def calculate_required_experience(commander_level: int) -> int:
    """
    Calculate the total cumulative experience required to reach a given commander level.

    Iterates from level one upward, accumulating the per-level experience
    requirement using the multiplier from calculate_level_multiplier at each
    step. The accumulation starts with a base seed of 40 experience points.

    :param commander_level: The target commander level to compute cumulative experience for.
    :type commander_level: int
    :return: The total cumulative experience points required to reach this level.
    :rtype: int
    """
    # Initialize the base experience requirement with a seed value of 40.
    current_requirement = 40
    # Initialize the accumulator for total cumulative experience points.
    total_experience = 0
    # Iterate through each level from 1 up to and including the target commander level.
    for level_index in range(1, commander_level + 1):
        # Compute the experience multiplier for the current iteration level.
        step_multiplier = calculate_level_multiplier(level_index)
        # Increment the per-level requirement by ten times the computed multiplier.
        current_requirement = current_requirement + 10 * step_multiplier
        # Accumulate the updated per-level requirement into the running total.
        total_experience = total_experience + current_requirement
    # Return the fully accumulated total experience points for the target level.
    return total_experience
