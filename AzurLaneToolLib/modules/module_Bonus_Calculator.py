#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL LIB BY MATT BELFAST BROWN
modules.module_Bonus_Calculator — Backyard experience and bonus calculations.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2026-06-21
Version: 0.8.0
Mode Create Date: 2023-03-11
Mode Date: 2026-06-21
Mode Version: 1.0.0

THIS PROGRAM IS LICENSED UNDER GPL-3.0 YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2026 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not,
see <https://www.gnu.org/licenses/>.
"""

# Map each battle chapter identifier to its normal and hard mode level thresholds.
chapter_map = {
    # Define the level thresholds for chapter 1 stages 1 through 4.
    "1-1": [1, 2], "1-2": [3, 4], "1-3": [5, 6], "1-4": [8, 10],
    # Define the level thresholds for chapter 2 stages 1 through 4.
    "2-1": [11, 12], "2-2": [14, 15], "2-3": [17, 18], "2-4": [20, 21],
    # Define the level thresholds for chapter 3 stages 1 through 4.
    "3-1": [23, 24], "3-2": [26, 27], "3-3": [29, 30], "3-4": [32, 33],
    # Define the level thresholds for chapter 4 stages 1 through 4.
    "4-1": [35, 36], "4-2": [38, 39], "4-3": [41, 42], "4-4": [44, 45],
    # Define the level thresholds for chapter 5 stages 1 through 4.
    "5-1": [47, 48], "5-2": [50, 51], "5-3": [53, 54], "5-4": [56, 57],
    # Define the level thresholds for chapter 6 stages 1 through 4.
    "6-1": [59, 60], "6-2": [62, 63], "6-3": [65, 66], "6-4": [68, 69],
    # Define the level thresholds for chapter 7 stages 1 through 4.
    "7-1": [71, 72], "7-2": [73, 74], "7-3": [75, 76], "7-4": [77, 78],
    # Define the level thresholds for chapter 8 stages 1 through 4.
    "8-1": [79, 80], "8-2": [81, 82], "8-3": [83, 84], "8-4": [85, 86],
    # Define the level thresholds for chapter 9 stages 1 through 4.
    "9-1": [88, 89], "9-2": [90, 91], "9-3": [92, 93], "9-4": [94, 95],
    # Define the level thresholds for chapter 10 stages 1 through 4.
    "10-1": [95, 96], "10-2": [97, 98], "10-3": [99, 100], "10-4": [101, 102],
    # Define the level thresholds for chapter 11 stages 1 through 4.
    "11-1": [103, 104], "11-2": [104, 105], "11-3": [105, 106], "11-4": [106, 107],
    # Define the level thresholds for chapter 12 stages 1 through 4.
    "12-1": [107, 108], "12-2": [109, 110], "12-3": [111, 112], "12-4": [113, 114],
    # Define the level thresholds for chapter 13 stages 1 through 4.
    "13-1": [115, 116], "13-2": [117, 118], "13-3": [119, 120], "13-4": [121, 122]
    # End of the chapter level threshold mapping dictionary.
    }


def calculate_backyard_experience(commander_level: int, comfort_value: int, kansen_count: int, food_ratio: float) -> int:

    """
    Calculate the comprehensive experience value earned per Kansen per hour in the backyard.

    The formula multiplies a base rate that scales with commander level by factors
    for food supplement ratio, comfort value, and the number of Kansen stationed.
    The result is truncated to an integer after applying all multipliers.

    :param commander_level: The current level of the commander determining the base experience rate.
    :type commander_level: int
    :param comfort_value: The comfort value of the backyard affecting the experience multiplier.
    :type comfort_value: int
    :param kansen_count: The number of Kansen stationed in the backyard.
    :type kansen_count: int
    :param food_ratio: The food supplement ratio applied as an additional multiplier.
    :type food_ratio: float
    :return: The comprehensive experience value earned per Kansen per hour.
    :rtype: int
    """
    # Define the per-Kansen count rate multipliers indexed by the number of stationed ships.
    kansen_rates = [0, 1, 1.8, 2.4, 2.8, 3.2, 3.6]
    # Calculate the base experience from the commander level and a fixed offset.
    experience_gain = (240 + commander_level * 12)
    # Apply the food supplement ratio as the first multiplier.
    experience_gain *= (1 + food_ratio)
    # Apply the comfort value adjustment factor as the second multiplier.
    experience_gain *= (1 + (comfort_value / (comfort_value + 100)))
    # Apply the food supplement ratio again as a repeated multiplier per game mechanics.
    experience_gain *= (1 + food_ratio)
    # Apply the per-Kansen count rate normalized by the number of stationed ships.
    experience_gain *= (kansen_rates[kansen_count] / kansen_count)
    # Truncate the final floating-point result to an integer value.
    experience_gain = int(experience_gain)
    # Return the computed hourly experience value per Kansen.
    return experience_gain


def calculate_commander_gain(kansen_count: int, success_grade: str, commander_level: int, battle_chapter: str, difficulty_index: int) -> int:
    """
    Calculate the commander experience earned from a sortie battle result.

    Determines the base experience from the number of Kansen deployed, applies
    a success grade multiplier, and applies a level difference penalty if the
    commander significantly outlevels the battle chapter.

    :param kansen_count: The number of Kansen deployed in the sortie fleet.
    :type kansen_count: int
    :param success_grade: The battle success grade string such as S, A, or B.
    :type success_grade: str
    :param commander_level: The current level of the commander.
    :type commander_level: int
    :param battle_chapter: The battle chapter identifier string in the format X-Y.
    :type battle_chapter: str
    :param difficulty_index: The difficulty index selecting normal or hard mode within the chapter.
    :type difficulty_index: int
    :return: The commander experience value earned from the sortie.
    :rtype: int
    """
    # Define the base experience values indexed by fleet size minus two.
    base_experiences = [20, 27, 35, 42.5, 49.5, 57.5, 65, 72.5]
    # Define the success grade multipliers for S, A, and B battle results.
    success_levels = {"S": 1.2, "A": 1.0, "B": 0.8}
    # Retrieve the chapter level threshold for the given battle chapter and difficulty.
    chapter_level = chapter_map[battle_chapter][difficulty_index]
    # Determine the level difference penalty multiplier based on commander overleveling.
    if commander_level - chapter_level > 40:
        # Commander exceeds chapter level by more than 40; apply the maximum penalty.
        level_coefficient = 0.1
    # The commander exceeds the chapter level by a moderate margin between 20 and 40.
    elif 20 < commander_level - chapter_level <= 40:
        # Commander exceeds chapter level by between 20 and 40 levels; apply a half penalty.
        level_coefficient = 0.5
    # The commander is within 20 levels of the chapter; no level penalty is applied.
    else:
        # Commander is within 20 levels of the chapter; the full experience is awarded.
        level_coefficient = 1
    # Look up the base experience value for the current fleet size.
    base_experience = base_experiences[kansen_count - 2]
    # Look up the success grade multiplier for the given battle result.
    success_multiplier = success_levels[success_grade]
    # Compute the final commander experience as the product of all factors.
    commander_experience = int(base_experience * success_multiplier * level_coefficient)
    # Return the computed commander experience value.
    return commander_experience
