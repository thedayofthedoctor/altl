#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL LIB BY MATT BELFAST BROWN
modules.module_Blueprint_Calculator — Blueprint plan requirement calculation.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2026-06-21
Version: 0.8.0
Mode Create Date: 2020-05-02
Mode Date: 2026-06-21
Mode Version: 1.2.0

THIS PROGRAM IS LICENSED UNDER GPL-3.0 YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2026 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this
program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Fitting tier thresholds for Top Solution type, indexed by fortune fitting level.
fitting_top = [10, 20, 30, 40, 65]
# Fitting tier thresholds for Decisive Plan type, indexed by fortune fitting level.
fitting_decisive = [20, 30, 40, 50, 75]


def calculate_base_blueprints(plan_level: int) -> int:
    """
    Calculate the number of basic blueprints required to reach a research level.

    Applies a piecewise formula that varies by level bracket: linear segments
    for regular ranges, fixed values for milestone levels, and a cubic
    polynomial for levels divisible by five beyond the first milestone.

    :param plan_level: The target research plan level for calculation.
    :type plan_level: int
    :return: The number of basic blueprints needed to advance from this level.
    :rtype: int
    """
    # Check if the level falls in the first regular bracket excluding milestones.
    if 1 <= plan_level <= 4 or 6 <= plan_level <= 9 or 11 <= plan_level <= 14:
        # Apply the linear formula for the first regular bracket range.
        base_blueprints = 0.4 * plan_level - 0.4 * (plan_level % 5) + 2
    # Check if the level falls in the second regular bracket excluding milestones.
    elif 16 <= plan_level <= 19 or 21 <= plan_level <= 24 or 26 <= plan_level <= 29:
        # Apply the linear formula for the second regular bracket range.
        base_blueprints = plan_level - (plan_level % 5) - 5
    # Check if the level is exactly the first milestone level five.
    elif plan_level == 5:
        # Assign the fixed blueprint requirement for the level-five milestone.
        base_blueprints = 5
    # Check if the level is any other milestone level divisible by five.
    elif plan_level % 5 == 0:
        # Compute the cubic term portion of the milestone polynomial formula.
        cubic_part = -(plan_level ** 3) / 375
        # Compute the quadratic term portion of the milestone polynomial formula.
        square_part = (plan_level ** 2) / 5
        # Compute the linear term portion of the milestone polynomial formula.
        linear_part = -2.9333 * plan_level
        # Combine all polynomial terms with the constant 20 and cast to integer.
        base_blueprints = int(cubic_part + square_part + linear_part + 20)
    # The level is zero or falls outside all defined brackets.
    else:
        # Set the blueprint requirement to zero for invalid input levels.
        base_blueprints = 0
    # Cast the computed value to an integer type before returning.
    return int(base_blueprints)


def calculate_plan_blueprints(plan_type: str, plan_level: int) -> int:
    """
    Calculate blueprints needed to advance one level for a given plan type.

    Multiplies the base requirement by 1.5 for Decisive Plan ships and
    returns the base value unchanged for Top Solution. Unknown types yield
    zero.

    :param plan_type: The research category, Top Solution or Decisive Plan.
    :type plan_type: str
    :param plan_level: The target research plan level for the calculation.
    :type plan_level: int
    :return: The number of blueprints required to advance from this level.
    :rtype: int
    """
    # Check if the plan type is Top Solution, using the base requirement directly.
    if plan_type == "Top Solution":
        # Calculate the base blueprint count without any multiplier.
        required_blueprints = calculate_base_blueprints(plan_level)
    # Otherwise check if the plan type is Decisive Plan with a 1.5x multiplier.
    elif plan_type == "Decisive Plan":
        # Calculate the base count and apply the Decisive Plan 1.5x multiplier.
        required_blueprints = int(calculate_base_blueprints(plan_level) * 1.5)
    # The plan type string is unrecognized; produce zero as a safe fallback.
    else:
        # Assign zero blueprints for unknown or invalid plan type inputs.
        required_blueprints = 0
    # Return the computed blueprint requirement to the caller.
    return required_blueprints


def calculate_blueprint_total(plan_type: str, owned_blueprints: int,
                              # Continue the function parameter list with level tracking arguments.
                              level_used: int, target_level: int,
                              # Conclude the function parameter list with the current level argument.
                              current_level: int) -> tuple[int, int]:
    """
    Calculate total blueprints required and used for non-fortune progression.

    Sums per-level requirements from the current level up to the target level,
    accounting for already-owned blueprints and those spent at the current
    level.

    :param plan_type: The research category, Top Solution or Decisive Plan.
    :type plan_type: str
    :param owned_blueprints: The number of unused blueprints in possession.
    :type owned_blueprints: int
    :param level_used: The number of blueprints already spent at this level.
    :type level_used: int
    :param target_level: The desired research plan level to reach.
    :type target_level: int
    :param current_level: The current research plan level already attained.
    :type current_level: int
    :return: A tuple of still-needed blueprints and total blueprints used.
    :rtype: tuple[int, int]
    """
    # Initialize the accumulator for total blueprints needed to reach the target.
    total_needed = 0
    # Initialize the accumulator for total blueprints already used so far.
    total_used = 0
    # Sum the per-level blueprint requirements up to the target level.
    for level_index in range(target_level):
        # Accumulate the requirement for each level in the target range.
        total_needed += calculate_plan_blueprints(plan_type, level_index)
    # Sum the per-level blueprint requirements up to the current level.
    for level_iterator in range(current_level):
        # Accumulate the requirement for each already-completed level.
        total_used += calculate_plan_blueprints(plan_type, level_iterator)
    # Add the blueprints already spent within the current level to the total.
    total_used += level_used
    # Compute the remaining blueprints after subtracting owned and used amounts.
    still_needed = total_needed - owned_blueprints - total_used
    # Return the pair of still-needed blueprints and total blueprints consumed.
    return still_needed, total_used


def calculate_fortune_fitting(plan_type: str, fortune_level: int,
                              # Continue the function parameter list with fortune blueprint arguments.
                              fortune_blueprints: int,
                              # Conclude the function parameter list with the fortune experience argument.
                              fortune_experience: int) -> tuple[int, int]:
    """
    Calculate blueprints required and used for fortune (Tianyun) fitting.

    Applies per-tier thresholds that differ between Top Solution and Decisive
    Plan types, prorating the current tier based on the fortune experience
    percentage.

    :param plan_type: The research category, Top Solution or Decisive Plan.
    :type plan_type: str
    :param fortune_level: The current fortune fitting tier level completed.
    :type fortune_level: int
    :param fortune_blueprints: The number of unused fortune blueprints owned.
    :type fortune_blueprints: int
    :param fortune_experience: The fortune fitting experience as a percentage.
    :type fortune_experience: int
    :return: A tuple of still-needed fortune blueprints and total used.
    :rtype: tuple[int, int]
    """
    # Initialize the accumulator for blueprints already consumed in fitting.
    fitting_used = 0
    # Check if the plan type is Top Solution with its own fitting thresholds.
    if plan_type == "Top Solution":
        # Sum the fitting tier thresholds for each completed fortune level.
        for level_position in range(fortune_level):
            # Accumulate the threshold value for each completed top-solution tier.
            fitting_used += fitting_top[level_position]
        # Prorate the current tier based on the fortune experience percentage.
        fitting_used += int((fortune_experience / 100)
                            # Multiply by the threshold value for the current fortune tier index.
                            * fitting_top[fortune_level])
        # Compute the remaining fortune blueprints for Top Solution completion.
        fortune_needed = 165 - fortune_blueprints - fitting_used
    # Otherwise check if the plan type is Decisive Plan with its own thresholds.
    elif plan_type == "Decisive Plan":
        # Sum the fitting tier thresholds for each completed fortune level.
        for level_position in range(fortune_level):
            # Accumulate the threshold value for each completed decisive tier.
            fitting_used += fitting_decisive[level_position]
        # Prorate the current tier based on the fortune experience percentage.
        fitting_used += int((fortune_experience / 100)
                            # Multiply by the threshold value for the current fortune tier index.
                            * fitting_top[fortune_level])
        # Compute the remaining fortune blueprints for Decisive Plan completion.
        fortune_needed = 215 - fortune_blueprints - fitting_used
    # The plan type string is unrecognized; produce zero as a safe fallback.
    else:
        # Set the fortune needed value to zero for unknown plan type inputs.
        fortune_needed = 0
    # Return the pair of fortune blueprints still needed and those already used.
    return fortune_needed, fitting_used


def calculate_blueprint_summary(
        # Accept the research plan type string as the first parameter.
        plan_type: str,
        # Accept the fortune fitting inclusion flag as the second parameter.
        has_fortune: str,
        # Accept the target research plan level as the third parameter.
        target_level: int,
        # Accept the current research plan level as the fourth parameter.
        current_level: int,
        # Accept the number of owned unused blueprints as the fifth parameter.
        owned_blueprints: int,
        # Accept the number of blueprints spent at this level as the sixth parameter.
        level_used: int,
        # Accept the completed fortune fitting tier level as the seventh parameter.
        fortune_level: int,
        # Accept the number of owned fortune blueprints as the eighth parameter.
        fortune_blueprints: int,
        # Accept the fortune fitting experience percentage as the ninth parameter.
        fortune_experience: int
        # The function return type is a six-element list of integer values.
        ) -> list:
    """
    Aggregate all blueprint calculations into a single summary list.

    Combines the non-fortune research progression calculation with the
    optional fortune fitting calculation, producing grand totals and
    per-category breakdowns in a six-element list.

    :param plan_type: The research category, Top Solution or Decisive Plan.
    :type plan_type: str
    :param has_fortune: Whether fortune fitting should be included.
    :type has_fortune: str
    :param target_level: The desired research plan level to reach.
    :type target_level: int
    :param current_level: The current research plan level already attained.
    :type current_level: int
    :param owned_blueprints: The number of unused blueprints in possession.
    :type owned_blueprints: int
    :param level_used: The number of blueprints spent at the current level.
    :type level_used: int
    :param fortune_level: The completed fortune fitting tier level.
    :type fortune_level: int
    :param fortune_blueprints: The number of owned fortune blueprints.
    :type fortune_blueprints: int
    :param fortune_experience: The fortune fitting experience as a percentage.
    :type fortune_experience: int
    :return: A six-element list of grand totals and category breakdowns.
    :rtype: list
    """
    # Check whether fortune fitting should be included in the calculation.
    if has_fortune:
        # Compute fortune fitting requirements when the inclusion flag is set.
        fortune_needed, fitting_used = calculate_fortune_fitting(
            # Pass the plan type for threshold table selection.
            plan_type,
            # Pass the completed fortune tier level for threshold lookup.
            fortune_level,
            # Pass the number of owned but unspent fortune blueprints.
            fortune_blueprints,
            # Pass the current fortune fitting experience as a percentage value.
            fortune_experience)
    # Fortune fitting is not requested; skip the fortune calculation entirely.
    else:
        # Set both fortune counters to zero to exclude them from the total.
        fortune_needed, fitting_used = 0, 0
    # Compute the non-fortune blueprint requirements for the given level range.
    still_needed, total_used = calculate_blueprint_total(
        # Pass the plan type for multiplier selection.
        plan_type,
        # Pass the number of owned but unspent regular blueprints.
        owned_blueprints,
        # Pass the number of blueprints already committed at the current level.
        level_used,
        # Pass the target level to compute blueprints required to reach it.
        target_level,
        # Pass the current level as the baseline for accumulated experience.
        current_level)
    # Combine non-fortune needs with fortune needs for the grand total required.
    overall_needed = still_needed + fortune_needed
    # Combine non-fortune usage with fortune usage for the grand total consumed.
    overall_used = total_used + fitting_used
    # Return the complete summary as a six-element list of computed integers.
    return [overall_needed, overall_used,
            # Continue the summary list with the per-category breakdown values.
            still_needed, total_used, fortune_needed, fitting_used]
