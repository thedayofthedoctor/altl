#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF AZUR LANE TOOL LIB BY MATT BELFAST BROWN
setup.py — Package build and distribution configuration for setuptools.

Author: Matt Belfast Brown
E-mail: thedayofthedo@gmail.com
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

# Import the setuptools packaging utilities for building and distributing the package.
from setuptools import find_packages, setup

# Open the long description markdown file for inclusion in the package metadata.
with open("Descriptiption.md", "r", encoding="utf-8") as description_file:
    # Read the full content of the description file into a string variable.
    long_description = description_file.read()

# Invoke the setuptools setup function with the complete package configuration.
setup(
        # Specify the distribution name for the PyPI package index.
        name="AzurLaneToolLib",
        # Specify the current semantic version string for this release.
        version="0.8.0",

        # Specify the author's full display name for package metadata.
        author="Matt Belfast Brown",
        # Specify the author's contact email address for package inquiries.
        author_email="thedayofthedo@gmail.com",
        # Specify the SPDX license identifier string for the package.
        license="GPL-3.0 LICENSE",

        # Provide a short one-line summary of the package purpose for PyPI display.
        description="Tools lib for Azur Lane which game powered by ManJiu Shanghai",
        # Assign the pre-read long description content from the markdown file.
        long_description=long_description,
        # Declare the content type of the long description as GitHub-flavored markdown.
        long_description_content_type="text/markdown",
        # List search keywords to help users discover the package on the index.
        keywords=["pip", "azur_lane", "tool"],

        # Set the project homepage URL pointing to the GitHub repository.
        url="https://github.com/thedayofthedoctor/altl",
        # Map additional project-related URLs for documentation and issue tracking.
        project_urls={
            # URL pointing to the hosted package documentation site.
            "Documentation": "http://belfast.web3v.work/program/doc/altl/",
            # URL pointing to the GitHub issue tracker for bug reports.
            "Bug Tracker": "https://github.com/thedayofthedoctor/altl/issues",
            # End of the project URLs dictionary mapping.
            },

        # Automatically discover all packages in the source tree using setuptools.
        packages=find_packages(),
        # Include non-Python data files listed in package_data during installation.
        include_package_data=True,
        # Declare JSON detail files inside the details package as package data.
        package_data={
            # Map the details subpackage to include all JSON files at that level.
            "AzurLaneToolLib.details": ["*.json"],
        # End of the package data dictionary mapping.
        },
        # Indicate that the package can be safely installed as a zip archive.
        zip_safe=True,

        # List the trove classifiers for the Python package index categorisation.
        classifiers=[
            # Declare compatibility with Python version 3.9.
            "Programming Language :: Python :: 3.9",
            # Declare compatibility with Python version 3.10.
            "Programming Language :: Python :: 3.10",
            # Declare compatibility with Python version 3.11.
            "Programming Language :: Python :: 3.11",
            # Declare compatibility with Python version 3.12.
            "Programming Language :: Python :: 3.12",
            # Declare compatibility with Python version 3.13.
            "Programming Language :: Python :: 3.13",
            # Declare compatibility with Python version 3.14.
            "Programming Language :: Python :: 3.14",
            # Declare the Open Source license classification for the package.
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        # End of the classifiers list definition.
            ],
        # Declare that the package runs on any operating system platform.
        platforms="any",
        # List the mandatory runtime dependencies required by the package.
        install_requires=["lzstring"],
        # Restrict installation to Python versions 3.9 through 3.14 inclusive.
        python_requires=">=3.9,<=3.14"
    # End of the setup function call arguments.
        )
