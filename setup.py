#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Stephane Caron <stephane.caron@lirmm.fr>
#
# This file is part of pypoman.
#
# pypoman is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# pypoman is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pypoman. If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(
    name='pypoman',
    version='0.1.0',
    description="Python Polyhedron Manipulation",
    url="https://github.com/stephane-caron/pypoman",
    author="Stéphane Caron",
    author_email="stephane.caron@lirmm.fr",
    license="LGPL",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License (LGPL)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Mathematics'],
    packages=['pypoman']
)
