#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL BY MATT BELFAST BROWN
AzurLaneToolLib.modules.__init__ — Subpackage exposing all calculation module names.

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

# Expose the subpackage title string for introspection and distribution metadata.
__title__ = "AzurLaneToolLib.modules"
# Expose the subpackage version string for introspection and distribution metadata.
__version__ = "0.8.0"
# Expose the author name string for introspection and distribution metadata.
__author__ = "Matt Belfast Brown"
# Expose the license identifier string for introspection and distribution metadata.
__license__ = "GPL-3.0"
# Expose the copyright string for introspection and distribution metadata.
__copyright__ = "Copyright (c) 2019-2026 Matt Belfast Brown"
# Declare the set of public module names this subpackage exposes for wildcard imports.
__all__ = ["module_Blueprint_Calculator", "module_Bonus_Calculator",
           # Continue the public API list with the remaining module identifiers.
           "module_Commander_Calculator", "module_Experience_Calculator",
           # Continue the public API list with the final pair of module identifier strings.
           "module_Fuel_Calculator", "module_Kansen_Compare"]
