# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL LIB BY MATT BELFAST BROWN
details.__init__ — Data access layer that loads reference data from bundled JSON detail files.

Author: Matt Belfast Brown
Create Date: 2019-07-11
Version Date: 2026-06-21
Version: 0.8.0

THIS PROGRAM IS LICENSED UNDER GPL-3.0 YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2019-2026 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not,
see <https://www.gnu.org/licenses/>.
"""

# Import the JSON module for deserializing bundled detail files.
import json
# Access package resources via the modern importlib API available since Python 3.9.
import importlib.resources


class DetailLoader:
    """
    Lazy-loads Azur Lane reference data from bundled JSON detail files.

    Each public method loads a specific data category on first access and caches
    the result as an instance attribute, eliminating redundant file I/O on
    subsequent calls. All JSON keys follow the PascalCase convention required by
    CLASP-3.1.

    Public methods:
        load_nations — Loads and returns the nation codes lookup dictionary.
        load_equipmenttypes — Loads and returns the equipment types lookup dictionary.
        load_shiptypes — Loads and returns the ship types lookup dictionary.
        load_rarities — Loads and returns the rarity codes lookup dictionary.
        load_ships — Loads and returns the ship data dictionary.

    Private methods:
        _init_load_json_file_function_ — Opens and parses a bundled JSON detail file.
    """

    def __init__(self):
        """
        Initialize the DetailLoader with empty caches for all five data categories.

        Each cache attribute starts as None and is populated lazily when the
        corresponding public method is first called. This avoids loading all JSON
        files at import time and defers I/O until the data is actually needed.
        """
        # Initialize the nation codes cache to None for lazy loading on first access.
        self.cache_nations = None
        # Initialize the equipment types cache to None for lazy loading on first access.
        self.cache_equipmenttypes = None
        # Initialize the ship types cache to None for lazy loading on first access.
        self.cache_shiptypes = None
        # Initialize the rarity codes cache to None for lazy loading on first access.
        self.cache_rarities = None
        # Initialize the ship data cache to None for lazy loading on first access.
        self.cache_ships = None

    def _init_load_json_file_function_(self, resource_name):
        """
        Open and parse a bundled JSON detail file from the details package.

        Reads a JSON resource using the importlib.resources API introduced in
        Python 3.9, decodes it with UTF-8 encoding, and returns the resulting
        dictionary. This private method is called once per data category when
        the corresponding cache is empty.

        :param resource_name: The filename of the JSON resource within the details package.
        :type resource_name: str
        :return: Parsed JSON data as a dictionary of PascalCase key-value pairs.
        :rtype: dict
        """
        # Open the JSON file bundled with the package and parse it into a dictionary.
        with importlib.resources.files(__package__).joinpath(resource_name).open("r", encoding="utf-8") as file_resource:
            # Parse and return the JSON content from the opened file resource.
            return json.load(file_resource)

    def load_nations(self):
        """
        Lazy-load and return the nation codes lookup dictionary.

        Reads the detail_Nation_Codes.json file on first call and caches the
        result as an instance attribute. Subsequent calls return the cached
        dictionary without performing additional I/O.

        :return: Dictionary mapping nation ID strings to metadata such as
            Chinese, English, and Japanese names.
        :rtype: dict
        """
        # Populate the cache only if it has not been loaded yet.
        if self.cache_nations is None:
            # Call the private loader method to parse the bundled JSON detail file.
            self.cache_nations = self._init_load_json_file_function_("detail_Nation_Codes.json")
        # Return the cached nation codes dictionary to the caller.
        return self.cache_nations

    def load_equipmenttypes(self):
        """
        Lazy-load and return the equipment types lookup dictionary.

        Reads the detail_Equipment_Types.json file on first call and caches the
        result as an instance attribute. Subsequent calls return the cached
        dictionary without performing additional I/O.

        :return: Dictionary mapping equipment type ID strings to multilingual
            type name metadata.
        :rtype: dict
        """
        # Populate the cache only if it has not been loaded yet.
        if self.cache_equipmenttypes is None:
            # Call the private loader method to parse the bundled JSON detail file.
            self.cache_equipmenttypes = self._init_load_json_file_function_("detail_Equipment_Types.json")
        # Return the cached equipment types dictionary to the caller.
        return self.cache_equipmenttypes

    def load_shiptypes(self):
        """
        Lazy-load and return the ship types lookup dictionary.

        Reads the detail_Ship_Types.json file on first call and caches the
        result as an instance attribute. Subsequent calls return the cached
        dictionary without performing additional I/O.

        :return: Dictionary mapping ship type ID strings to multilingual type
            name and position metadata.
        :rtype: dict
        """
        # Populate the cache only if it has not been loaded yet.
        if self.cache_shiptypes is None:
            # Call the private loader method to parse the bundled JSON detail file.
            self.cache_shiptypes = self._init_load_json_file_function_("detail_Ship_Types.json")
        # Return the cached ship types dictionary to the caller.
        return self.cache_shiptypes

    def load_rarities(self):
        """
        Lazy-load and return the rarity codes lookup dictionary.

        Reads the detail_Rarity_Codes.json file on first call and caches the
        result as an instance attribute. Subsequent calls return the cached
        dictionary without performing additional I/O.

        :return: Dictionary mapping rarity ID strings to multilingual rarity
            level display names.
        :rtype: dict
        """
        # Populate the cache only if it has not been loaded yet.
        if self.cache_rarities is None:
            # Call the private loader method to parse the bundled JSON detail file.
            self.cache_rarities = self._init_load_json_file_function_("detail_Rarity_Codes.json")
        # Return the cached rarity codes dictionary to the caller.
        return self.cache_rarities

    def load_ships(self):
        """
        Lazy-load and return the ship data dictionary.

        Reads the detail_Ship_Data.json file on first call and caches the
        result as an instance attribute. This is the largest data file in the
        package, containing attributes for over 500 Kansen entries. Subsequent
        calls return the cached dictionary without performing additional I/O.

        :return: Dictionary mapping ship ID strings to full ship attribute
            records including names, rarity, type, and equipment slots.
        :rtype: dict
        """
        # Populate the cache only if it has not been loaded yet.
        if self.cache_ships is None:
            # Call the private loader method to parse the bundled JSON detail file.
            self.cache_ships = self._init_load_json_file_function_("detail_Ship_Data.json")
        # Return the cached ship data dictionary to the caller.
        return self.cache_ships


# Instantiate a singleton DetailLoader for package-wide lazy-loaded data access.
detail_loader = DetailLoader()

# Expose each public method as a module-level convenience function.
# The public API names are preserved for backward compatibility with existing callers.
load_nations = detail_loader.load_nations
# Expose equipment types loader as a module-level convenience function.
load_equipmenttypes = detail_loader.load_equipmenttypes
# Expose ship types loader as a module-level convenience function.
load_shiptypes = detail_loader.load_shiptypes
# Expose rarity codes loader as a module-level convenience function.
load_rarities = detail_loader.load_rarities
# Expose ship data loader as a module-level convenience function.
load_ships = detail_loader.load_ships

# Expose the package title string for introspection and distribution metadata.
__title__ = "AzurLaneToolLib.details"
# Expose the package version string for introspection and distribution metadata.
__version__ = "0.8.0"
# Expose the author name string for introspection and distribution metadata.
__author__ = "Matt Belfast Brown"
# Expose the license identifier string for introspection and distribution metadata.
__license__ = "GPL-3.0"
# Expose the copyright string for introspection and distribution metadata.
__copyright__ = "Copyright (c) 2019-2026 Matt Belfast Brown"
# Declare the set of public API names this package exposes for wildcard imports.
__all__ = ["DetailLoader", "load_nations", "load_equipmenttypes", "load_shiptypes",
           # Continue the public API list with the remaining loader functions.
           "load_rarities", "load_ships"]
