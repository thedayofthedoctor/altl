#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL LIB BY MATT BELFAST BROWN
modules.module_Experience_Calculator — Ship level-up experience calculation.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2026-06-21
Version: 0.8.0
Mode Create Date: 2020-09-25
Mode Date: 2026-06-21
Mode Version: 1.0.4

THIS PROGRAM IS LICENSED UNDER GPL-3.0 YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2026 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not,
see <https://www.gnu.org/licenses/>.
"""


def calculate_level_experience(plan_type: str, ship_level: int) -> int:
    """
    Calculate the experience points required to advance a ship to the next level.

    Uses a piecewise linear formula with slope and intercept coefficients that
    vary by level bracket and plan type. The formula is: int(1000 * slope *
    level - 100 * intercept). Top Solution and Decisive Plan types each have
    their own coefficient tables.

    :param plan_type: The ship research plan type string, either Top Solution or Decisive Plan.
    :type plan_type: str
    :param ship_level: The current level of the ship for which to compute the experience requirement.
    :type ship_level: int
    :return: The experience value required to advance from the current level to the next.
    :rtype: int
    """
    # Check if the plan type is Top Solution with its own coefficient bracket table.
    if plan_type == "Top Solution":
        # Check if the ship is at level zero which requires no experience to advance.
        if ship_level == 0:
            # Assign zero coefficients for the edge case of level zero.
            slope_coefficient, intercept_coefficient = 0, 0
        # Check if the ship level falls in the early game bracket from 1 through 40.
        elif 0 < ship_level <= 40:
            # Assign the gentle slope coefficient for early-game level brackets.
            slope_coefficient, intercept_coefficient = 0.1, 0
        # Check if the ship level falls in the mid-early bracket from 41 through 60.
        elif 40 < ship_level <= 60:
            # Assign a moderately increased slope for this level bracket.
            slope_coefficient, intercept_coefficient = 0.2, 40
        # Check if the ship level falls in the mid-game bracket from 61 through 70.
        elif 60 < ship_level <= 70:
            # Assign an increased slope for the mid-game bracket range.
            slope_coefficient, intercept_coefficient = 0.3, 100
        # Check if the ship level falls in the mid-late bracket from 71 through 80.
        elif 70 < ship_level <= 80:
            # Assign a higher slope for the mid-late game bracket.
            slope_coefficient, intercept_coefficient = 0.4, 170
        # Check if the ship level falls in the late-game bracket from 81 through 90.
        elif 80 < ship_level <= 90:
            # Assign the top regular slope coefficient for this bracket.
            slope_coefficient, intercept_coefficient = 0.5, 250
        # Check if the ship level falls in the awakening bracket from 91 through 92.
        elif 90 < ship_level <= 92:
            # Assign a steeply increased slope for the awakening phase.
            slope_coefficient, intercept_coefficient = 1, 700
        # Check if the ship level falls in the second awakening bracket at 93 or 94.
        elif 92 < ship_level <= 94:
            # Assign a doubled awakening slope for this bracket.
            slope_coefficient, intercept_coefficient = 2, 1620
        # Check if the ship is exactly at the milestone level 95.
        elif ship_level == 95:
            # Assign a quadrupled slope for the level 95 milestone.
            slope_coefficient, intercept_coefficient = 4, 3500
        # Check if the ship level falls in the post-milestone bracket at 96 or 97.
        elif 95 < ship_level <= 97:
            # Assign a quintupled slope for the post-95 bracket.
            slope_coefficient, intercept_coefficient = 5, 4450
        # Check if the ship is exactly at the milestone level 98.
        elif ship_level == 98:
            # Assign a 20x slope for the level 98 milestone.
            slope_coefficient, intercept_coefficient = 20, 19000
        # Check if the ship is exactly at the milestone level 99.
        elif ship_level == 99:
            # Assign a 72x slope for the penultimate milestone level.
            slope_coefficient, intercept_coefficient = 72, 69960
        # Check if the ship is exactly at the max level 100 milestone.
        elif ship_level == 100:
            # Assign negative coefficients for the level 100 boundary condition.
            slope_coefficient, intercept_coefficient = -82, -82500
        # Check if the ship level falls in the cognitive awakening bracket from 101 through 105.
        elif 100 < ship_level <= 105:
            # Assign a post-100 moderate slope for cognitive awakening.
            slope_coefficient, intercept_coefficient = 3, 2500
        # Check if the ship level falls in the cognitive bracket from 106 through 110.
        elif 105 < ship_level <= 110:
            # Assign a doubled cognitive awakening slope.
            slope_coefficient, intercept_coefficient = 6, 5650
        # Check if the ship level falls in the cognitive bracket from 111 through 115.
        elif 110 < ship_level <= 115:
            # Assign a 10x slope for this cognitive bracket.
            slope_coefficient, intercept_coefficient = 10, 10050
        # Check if the ship level falls in the cognitive bracket from 116 through 120.
        elif 115 < ship_level <= 120:
            # Assign a 15x slope for this cognitive bracket.
            slope_coefficient, intercept_coefficient = 15, 15800
        # Check if the ship level falls in the final cognitive bracket from 121 through 124.
        elif 120 < ship_level < 125:
            # Assign a 21x slope for the penultimate cognitive bracket.
            slope_coefficient, intercept_coefficient = 21, 23000
        # Check if the ship is exactly at the ultimate max level 125.
        elif ship_level == 125:
            # Assign the maximum coefficients for the final level milestone.
            slope_coefficient, intercept_coefficient = 2696, 3340000
        # The ship level falls outside all defined brackets for Top Solution.
        else:
            # Assign zero coefficients as a safe fallback for unrecognized levels.
            slope_coefficient, intercept_coefficient = 0, 0
    # Otherwise check if the plan type is Decisive Plan with its own coefficient table.
    elif plan_type == "Decisive Plan":
        # Check if the ship is at level zero which requires no experience to advance.
        if ship_level == 0:
            # Assign zero coefficients for the edge case of level zero.
            slope_coefficient, intercept_coefficient = 0, 0
        # Check if the ship level falls in the early game bracket from 1 through 40.
        elif 0 < ship_level <= 40:
            # Assign the Decisive Plan early-game slope 1.2x higher than Top Solution.
            slope_coefficient, intercept_coefficient = 0.12, 0
        # Check if the ship level falls in the mid-early bracket from 41 through 60.
        elif 40 < ship_level <= 60:
            # Assign the Decisive Plan mid-early slope.
            slope_coefficient, intercept_coefficient = 0.24, 48
        # Check if the ship level falls in the mid-game bracket from 61 through 70.
        elif 60 < ship_level <= 70:
            # Assign the Decisive Plan mid-game slope.
            slope_coefficient, intercept_coefficient = 0.36, 120
        # Check if the ship level falls in the mid-late bracket from 71 through 80.
        elif 70 < ship_level <= 80:
            # Assign the Decisive Plan mid-late slope.
            slope_coefficient, intercept_coefficient = 0.48, 204
        # Check if the ship level falls in the late-game bracket from 81 through 89.
        elif 80 < ship_level < 90:
            # Assign the Decisive Plan late-game slope.
            slope_coefficient, intercept_coefficient = 0.6, 300
        # Check if the ship is exactly at the milestone level 90.
        elif ship_level == 90:
            # Assign the Decisive Plan level 90 milestone slope.
            slope_coefficient, intercept_coefficient = 0.65, 325
        # Check if the ship level falls in the awakening bracket from 91 through 92.
        elif 90 < ship_level <= 92:
            # Assign the Decisive Plan awakening phase slope.
            slope_coefficient, intercept_coefficient = 1.3, 910
        # Check if the ship level falls in the second awakening bracket at 93 or 94.
        elif 92 < ship_level <= 94:
            # Assign the Decisive Plan doubled awakening slope.
            slope_coefficient, intercept_coefficient = 2.6, 2106
        # Check if the ship is exactly at the milestone level 95.
        elif ship_level == 95:
            # Assign the Decisive Plan level 95 milestone slope.
            slope_coefficient, intercept_coefficient = 5.2, 4550
        # Check if the ship level falls in the post-milestone bracket at 96 or 97.
        elif 95 < ship_level <= 97:
            # Assign the Decisive Plan post-95 bracket slope.
            slope_coefficient, intercept_coefficient = 6.5, 5785
        # Check if the ship is exactly at the milestone level 98.
        elif ship_level == 98:
            # Assign the Decisive Plan level 98 milestone slope.
            slope_coefficient, intercept_coefficient = 26, 24700
        # Check if the ship is exactly at the milestone level 99.
        elif ship_level == 99:
            # Assign the Decisive Plan penultimate milestone slope.
            slope_coefficient, intercept_coefficient = 93.6, 90948
        # Check if the ship is exactly at the max level 100 milestone.
        elif ship_level == 100:
            # Assign negative coefficients for the level 100 boundary condition.
            slope_coefficient, intercept_coefficient = -111.6, -112200
        # Check if the ship level falls in the cognitive awakening bracket from 101 through 105.
        elif 100 < ship_level <= 105:
            # Assign the Decisive Plan post-100 cognitive awakening slope.
            slope_coefficient, intercept_coefficient = 3.6, 3000
        # Check if the ship level falls in the cognitive bracket from 106 through 110.
        elif 105 < ship_level <= 110:
            # Assign the Decisive Plan doubled cognitive slope.
            slope_coefficient, intercept_coefficient = 7.2, 6780
        # Check if the ship level falls in the cognitive bracket from 111 through 115.
        elif 110 < ship_level <= 115:
            # Assign the Decisive Plan 12x cognitive slope.
            slope_coefficient, intercept_coefficient = 12, 12060
        # Check if the ship level falls in the cognitive bracket from 116 through 120.
        elif 115 < ship_level <= 120:
            # Assign the Decisive Plan 18x cognitive slope.
            slope_coefficient, intercept_coefficient = 18, 18960
        # Check if the ship level falls in the final cognitive bracket from 121 through 124.
        elif 120 < ship_level < 125:
            # Assign the Decisive Plan penultimate cognitive slope.
            slope_coefficient, intercept_coefficient = 25.2, 27600
        # Check if the ship is exactly at the ultimate max level 125.
        elif ship_level == 125:
            # Assign the maximum Decisive Plan coefficients for the final level milestone.
            slope_coefficient, intercept_coefficient = 2635.2, 3264000
        # The ship level falls outside all defined brackets for Decisive Plan.
        else:
            # Assign zero coefficients as a safe fallback for unrecognized levels.
            slope_coefficient, intercept_coefficient = 0, 0
    # The plan type is unrecognized; assign zero coefficients as a safe fallback.
    else:
        # Assign zero coefficients for unknown or invalid plan type inputs.
        slope_coefficient, intercept_coefficient = 0, 0
    # Define the fixed slope multiplier constant used in the experience formula.
    slope_constant = 1000
    # Define the fixed intercept multiplier constant used in the experience formula.
    intercept_constant = -100
    # Compute the intercept contribution term from the constant and coefficient.
    intercept_part = intercept_constant * intercept_coefficient
    # Compute the slope contribution term from the constant and coefficient.
    slope_part = slope_constant * slope_coefficient
    # Apply the linear formula to produce the final integer experience requirement.
    level_experience = int(slope_part * ship_level + intercept_part)
    # Return the computed per-level experience value to the caller.
    return level_experience


def calculate_ship_total(plan_type: str, target_level: int, current_level: int, current_experience: int) -> tuple[int, int]:
    """
    Calculate the total experience required and already accumulated for a ship.

    Sums the per-level experience requirements for all levels from zero up to
    the target and current levels using calculate_level_experience at each step.
    The difference between the two totals, minus current experience, yields the
    amount still needed to reach the target level.

    :param plan_type: The ship research plan type string, either Top Solution or Decisive Plan.
    :type plan_type: str
    :param target_level: The desired level the ship should reach.
    :type target_level: int
    :param current_level: The level the ship has already attained.
    :type current_level: int
    :param current_experience: The experience points already earned toward the current level.
    :type current_experience: int
    :return: A tuple of the still-needed experience and the total experience accumulated.
    :rtype: tuple[int, int]
    """
    # Initialize the accumulator for total experience required to reach the target level.
    total_target = 0
    # Initialize the accumulator for total experience already earned up to the current level.
    total_current = 0
    # Sum the per-level experience requirements from zero up to the target level.
    for level_index in range(target_level):
        # Accumulate the per-level requirement for each level in the target range.
        total_target += calculate_level_experience(plan_type, level_index)
    # Sum the per-level experience requirements from zero up to the current level.
    for level_iterator in range(current_level):
        # Accumulate the per-level requirement for each already-completed level.
        total_current += calculate_level_experience(plan_type, level_iterator)
    # Add the partial experience already earned within the current level.
    total_target += current_experience
    # Compute the remaining experience still needed to bridge the gap.
    still_needed = total_current - total_target
    # Return the pair of still-needed experience and total accumulated experience.
    return still_needed, total_current
