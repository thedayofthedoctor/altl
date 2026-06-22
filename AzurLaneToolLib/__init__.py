#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL BY MATT BELFAST BROWN
AzurLaneToolLib.__init__ — Package root exposing all public calculation functions.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2026-06-21
Version: 0.8.0

THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2026 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not,
see <https://www.gnu.org/licenses/>.
"""

# Import all calculation modules from the modules package tree.
import AzurLaneToolLib.modules.module_Blueprint_Calculator as module_Blueprint_Calculator
# Import the bonus calculator module that handles backyard and utility experience calculations.
import AzurLaneToolLib.modules.module_Bonus_Calculator as module_Bonus_Calculator
# Import the commander calculator module that computes commander-level experience.
import AzurLaneToolLib.modules.module_Commander_Calculator as module_Commander_Calculator
# Import the experience calculator module that computes ship-level experience.
import AzurLaneToolLib.modules.module_Experience_Calculator as module_Experience_Calculator
# Import the fuel calculator module that computes ship fuel consumption values.
import AzurLaneToolLib.modules.module_Fuel_Calculator as module_Fuel_Calculator
# Import the Kansen compare module that performs harmonized ship name lookups.
import AzurLaneToolLib.modules.module_Kansen_Compare as module_Kansen_Compare

# Expose the package title string for introspection and distribution metadata.
__title__ = "AzurLaneToolLib"
# Expose the package version string for introspection and distribution metadata.
__version__ = "0.8.0"
# Expose the author name string for introspection and distribution metadata.
__author__ = "Matt Belfast Brown"
# Expose the license identifier string for introspection and distribution metadata.
__license__ = "GPL-3.0"
# Expose the copyright string for introspection and distribution metadata.
__copyright__ = "Copyright (c) 2019-2026 Matt Belfast Brown"
# Declare the set of public names this package exposes for wildcard imports.
__all__ = ["modules", "details", "module_Blueprint_Calculator", "module_Bonus_Calculator",
           # Continue the public API list with the remaining public identifier strings.
           "module_Commander_Calculator", "module_Experience_Calculator",
           # Continue the public API list with the final group of module identifier strings.
           "module_Fuel_Calculator", "module_Kansen_Compare"]

# Expose public functions from the Blueprint Calculator module as convenience aliases.
fun_cnbp_rbpt = module_Blueprint_Calculator.calculate_blueprint_summary
# Expose the base blueprint calculation function as a convenience alias.
fun_cnbp_rqub = module_Blueprint_Calculator.calculate_base_blueprints
# Expose the plan-type blueprint calculation function as a convenience alias.
fun_cnbp_rqup = module_Blueprint_Calculator.calculate_plan_blueprints
# Expose the blueprint total calculation function as a convenience alias.
fun_cnbp_rrcl = module_Blueprint_Calculator.calculate_blueprint_total
# Expose the fortune fitting calculation function as a convenience alias.
fun_cnbp_tyfi = module_Blueprint_Calculator.calculate_fortune_fitting
# Expose public functions from the Commander Calculator module as convenience aliases.
fun_berf_cmug = module_Commander_Calculator.calculate_required_experience
# Expose the level multiplier calculation function as a convenience alias.
fun_evdb_cmul = module_Commander_Calculator.calculate_level_multiplier
# Expose public functions from the Experience Calculator module as convenience aliases.
fun_cexp_vrfu = module_Experience_Calculator.calculate_level_experience
# Expose the ship experience total calculation function as a convenience alias.
fun_crex_cele = module_Experience_Calculator.calculate_ship_total
# Expose public functions from the Fuel Calculator module as convenience aliases.
fun_bsdg_fuca = module_Fuel_Calculator.calculate_base_consumption
# Expose the special correction lookup function as a convenience alias.
fun_kstp_scco = module_Fuel_Calculator.lookup_special_correction
# Expose the surface consumption calculation function as a convenience alias.
fun_sfks_fuca = module_Fuel_Calculator.calculate_surface_consumption
# Expose the submarine fuel calculation function as a convenience alias.
fun_subd_fuco = module_Fuel_Calculator.calculate_submarine_fuel
# Expose public functions from the Kansen Compare module as convenience aliases.
fun_ksen_nmco = module_Kansen_Compare.lookup_harmonized_name
