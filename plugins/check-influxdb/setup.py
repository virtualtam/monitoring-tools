#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Copyright (C) 2014, Savoir-faire Linux, Inc.
#
# Authors:
#   Matthieu Caneill <matthieu.caneill@savoirfairelinux.com>
#   Grégory Starck <gregory.starck@savoirfairelinux.com>
#
#############################################################################

from __future__ import with_statement

from setuptools import setup, find_packages


description = 'check if an influxDB instance is launch and some other metrics ( memory allocated, number of shard, number of point write and number of point per shard)'
long_description = ('''check if an influxDB instance is launch and some other metrics ( memory allocated, number of shard, number of point write and number of point per shard)''')

#############################################################################

setup(
    name='shinkenplugins.plugins.influxdb',
    version="1.0",
    packages=find_packages(),
    author="Flavien Peyre",
    author_email="flavien.peyre@savoirfairelinux.com",
    long_description=long_description,
    description=description,
    license="GPL3+",
    url="https://github.com/savoirfairelinux/sfl-shinken-plugins",
    platforms=['any'],
    install_requires=[
        'shinkenplugins>0.2',
    ],
    extras_require={
        'test': [
            'nose',
            'psutil',
            'influxdb',
            'requests',
            
        ],
    },
    namespace_packages=[
        'shinkenplugins',
        'shinkenplugins.plugins',
    ],
    entry_points="""
    [console_scripts]
    check_influxdb = shinkenplugins.plugins.influxdb:main
    """
)
