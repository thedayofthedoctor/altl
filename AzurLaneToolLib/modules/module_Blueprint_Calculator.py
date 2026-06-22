#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL LIB BY MATT BELFAST BROWN
modules.module_Blueprint_Calculator — Blueprint requirement calculation for ship research plans.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2026-06-21
Version: 0.8.0
Mode Create Date: 2020-05-02
Mode Date: 2026-06-21
Mode Version: 1.2.0

THIS PROGRAM IS LICENSED UNDER GPL-3.0 YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2026 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not,
see <https://www.gnu.org/licenses/>.
"""

# Fitting tier thresholds for Top Solution plan type, indexed by fortune fitting level.
fitting_top = [10, 20, 30, 40, 65]
# Fitting tier thresholds for Decisive Plan type, indexed by fortune fitting level.
fitting_decisive = [20, 30, 40, 50, 75]


def calculate_base_blueprints(plan_level: int) -> int:
    """
    Calculate the number of basic blueprints required to reach a given research level.

    Applies a piecewise formula that varies by level bracket: linear segments
    for regular ranges, fixed values for milestone levels, and a cubic
    polynomial for levels divisible by five beyond the first milestone.

    :param plan_level: The target research plan level for which to calculate the requirement.
    :type plan_level: int
    :return: The number of basic blueprints needed to advance from the previous level.
    :rtype: int
    """
    # Check if the level falls in the first regular bracket excluding milestone positions.
    if 1 <= plan_level <= 4 or 6 <= plan_level <= 9 or 11 <= plan_level <= 14:
        # Apply the linear formula for the first regular bracket range.
        base_blueprints = 0.4 * plan_level - 0.4 * (plan_level % 5) + 2
    # Check if the level falls in the second regular bracket excluding milestone positions.
    elif 16 <= plan_level <= 19 or 21 <= plan_level <= 24 or 26 <= plan_level <= 29:
        # Apply the linear formula for the second regular bracket range.
        base_blueprints = plan_level - (plan_level % 5) - 5
    # Check if the level is exactly the first milestone level five.
    elif plan_level == 5:
        # Assign the fixed blueprint requirement for the level-five milestone.
        base_blueprints = 5
    # Check if the level is any other milestone divisible by five.
    elif plan_level % 5 == 0:
        # Apply the cubic polynomial formula for higher milestone levels.
        base_blueprints = int(-(plan_level ** 3) / 375 + (plan_level ** 2) / 5 - 2.9333 * plan_level + 20)
    # The level is zero or unrecognized; produce no blueprint requirement.
    else:
        # Set the blueprint requirement to zero for invalid or edge-case input levels.
        base_blueprints = 0
    # Return the computed value cast to an integer type.
    return int(base_blueprints)


def calculate_plan_blueprints(plan_type: str, plan_level: int) -> int:
    """
    Calculate the number of blueprints needed to advance one research level for a given plan type.

    Multiplies the base blueprint requirement by 1.5 for Decisive Plan ships
    and returns the base value unchanged for Top Solution ships. Unknown plan
    types yield zero.

    :param plan_type: The ship research category string, either Top Solution or Decisive Plan.
    :type plan_type: str
    :param plan_level: The target research plan level for the calculation.
    :type plan_level: int
    :return: The number of blueprints required to advance from this level.
    :rtype: int
    """
    # Check if the plan type is Top Solution, which uses the base requirement directly.
    if plan_type == "Top Solution":
        # Calculate the base blueprint count without applying any multiplier.
        required_blueprints = calculate_base_blueprints(plan_level)
    # Otherwise check if the plan type is Decisive Plan, which applies a 1.5x multiplier.
    elif plan_type == "Decisive Plan":
        # Calculate the base count and apply the Decisive Plan multiplier.
        required_blueprints = int(calculate_base_blueprints(plan_level) * 1.5)
    # The plan type is unrecognized; produce zero as a safe fallback value.
    else:
        # Assign zero blueprints for unknown or invalid plan type strings.
        required_blueprints = 0
    # Return the computed blueprint requirement for the given level and type.
    return required_blueprints


def calculate_blueprint_total(
        plan_type: str,
        owned_blueprints: int,
        level_used: int,
        target_level: int,
        current_level: int
) -> tuple[int, int]:
    """
    Calculate the total blueprints required and used for non-fortune research progress.

    Sums the per-level requirements from the current level up to the target level,
    accounting for already-owned blueprints and those spent at the current level.

    :param plan_type: The ship research category string, either Top Solution or Decisive Plan.
    :type plan_type: str
    :param owned_blueprints: The number of unused blueprints already in possession.
    :type owned_blueprints: int
    :param level_used: The number of blueprints already spent toward the current level.
    :type level_used: int
    :param target_level: The desired research plan level to reach.
    :type target_level: int
    :param current_level: The current research plan level already attained.
    :type current_level: int
    :return: A tuple of the still-needed blueprints and the total blueprints used so far.
    :rtype: tuple[int, int]
    """
    # Initialize the accumulator for total blueprints required to reach the target level.
    total_needed = 0
    # Initialize the accumulator for total blueprints already used up to the current level.
    total_used = 0
    # Sum the per-level blueprint requirements from zero up to the target level.
    for level_index in range(target_level):
        # Accumulate the blueprint requirement for each level in the target range.
        total_needed += calculate_plan_blueprints(plan_type, level_index)
    # Sum the per-level blueprint requirements from zero up to the current level.
    for level_iterator in range(current_level):
        # Accumulate the blueprint requirement for each already-completed level.
        total_used += calculate_plan_blueprints(plan_type, level_iterator)
    # Add the blueprints already spent within the current level.
    total_used += level_used
    # Compute the remaining blueprints still needed after accounting for owned and used.
    still_needed = total_needed - owned_blueprints - total_used
    # Return the pair of still-needed blueprints and total blueprints consumed.
    return still_needed, total_used


def calculate_fortune_fitting(
        plan_type: str,
        fortune_level: int,
        fortune_blueprints: int,
        fortune_experience: int
) -> tuple[int, int]:
    """
    Calculate the total blueprints required and used for fortune (Tianyun) fitting.

    Applies per-tier thresholds that differ between Top Solution and Decisive Plan
    types, and prorates the current tier based on the fortune experience percentage.

    :param plan_type: The ship research category string, either Top Solution or Decisive Plan.
    :type plan_type: str
    :param fortune_level: The current fortune fitting tier level already completed.
    :type fortune_level: int
    :param fortune_blueprints: The number of unused fortune fitting blueprints in possession.
    :type fortune_blueprints: int
    :param fortune_experience: The current fortune fitting experience value as a percentage.
    :type fortune_experience: int
    :return: A tuple of the total fortune blueprints still needed and the total already used.
    :rtype: tuple[int, int]
    """
    # Initialize the accumulator for blueprints already consumed in fortune fitting.
    fitting_used = 0
    # Check if the plan type is Top Solution, which uses the top-tier threshold list.
    if plan_type == "Top Solution":
        # Sum the fitting tier thresholds for each completed fortune level.
        for level_position in range(fortune_level):
            # Accumulate the threshold value for each completed tier in the top list.
            fitting_used += fitting_top[level_position]
        # Prorate the current incomplete tier based on the fortune experience percentage.
        fitting_used += int((fortune_experience / 100) * fitting_top[fortune_level])
        # Compute the remaining fortune blueprints needed for Top Solution completion.
        fortune_needed = 165 - fortune_blueprints - fitting_used
    # Otherwise check if the plan type is Decisive Plan, which uses its own threshold list.
    elif plan_type == "Decisive Plan":
        # Sum the fitting tier thresholds for each completed fortune level.
        for level_position in range(fortune_level):
            # Accumulate the threshold value for each completed tier in the decisive list.
            fitting_used += fitting_decisive[level_position]
        # Prorate the current incomplete tier based on the fortune experience percentage.
        fitting_used += int((fortune_experience / 100) * fitting_top[fortune_level])
        # Compute the remaining fortune blueprints needed for Decisive Plan completion.
        fortune_needed = 215 - fortune_blueprints - fitting_used
    # The plan type is unrecognized; produce a zero result as a safe fallback.
    else:
        # Set the fortune needed value to zero for unknown plan type inputs.
        fortune_needed = 0
    # Return the pair of fortune blueprints still needed and those already used.
    return fortune_needed, fitting_used


def calculate_blueprint_summary(
        plan_type: str,
        has_fortune: str,
        target_level: int,
        current_level: int,
        owned_blueprints: int,
        level_used: int,
        fortune_level: int,
        fortune_blueprints: int,
        fortune_experience: int
) -> list:
    """
    Aggregate all blueprint calculations into a single summary list.

    Combines the non-fortune research progression calculation with the optional
    fortune fitting calculation when enabled, producing grand totals and per-category
    breakdowns in a six-element list.

    :param plan_type: The ship research category string, either Top Solution or Decisive Plan.
    :type plan_type: str
    :param has_fortune: A flag indicating whether fortune fitting should be included in the calculation.
    :type has_fortune: str
    :param target_level: The desired research plan level to reach.
    :type target_level: int
    :param current_level: The current research plan level already attained.
    :type current_level: int
    :param owned_blueprints: The number of unused blueprints already in possession.
    :type owned_blueprints: int
    :param level_used: The number of blueprints already spent toward the current level.
    :type level_used: int
    :param fortune_level: The current fortune fitting tier level already completed.
    :type fortune_level: int
    :param fortune_blueprints: The number of unused fortune fitting blueprints in possession.
    :type fortune_blueprints: int
    :param fortune_experience: The current fortune fitting experience value as a percentage.
    :type fortune_experience: int
    :return: A six-element list containing grand totals and category breakdowns for blueprint needs.
    :rtype: list
    """
    # Check whether fortune fitting should be included in the aggregate calculation.
    if has_fortune:
        # Compute fortune fitting requirements when the flag is enabled.
        fortune_needed, fitting_used = calculate_fortune_fitting(
            plan_type, fortune_level, fortune_blueprints, fortune_experience
        )
    # Fortune fitting is not requested; initialize the fortune values to zero.
    else:
        # Set both fortune counters to zero to exclude them from the total.
        fortune_needed, fitting_used = 0, 0
    # Compute the non-fortune blueprint requirements for the specified level range.
    still_needed, total_used = calculate_blueprint_total(plan_type, owned_blueprints, level_used, target_level, current_level)
    # Combine non-fortune needs with fortune needs for the overall total of required blueprints.
    overall_needed = still_needed + fortune_needed
    # Combine non-fortune usage with fortune usage for the overall total of consumed blueprints.
    overall_used = total_used + fitting_used
    # Return the complete summary as a list of six computed values.
    return [overall_needed, overall_used, still_needed, total_used, fortune_needed, fitting_used]
