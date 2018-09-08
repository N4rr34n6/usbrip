#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@file config.py
@author Sam Freeside <scr.im/emsnovvcrash>
@date 2018-06

@brief Config file containing cross-module vars.

@license
Copyright (C) 2018 Sam Freeside

This file is part of usbrip.

usbrip is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

usbrip is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with usbrip.  If not, see <http://www.gnu.org/licenses/>.
@endlicense
"""

import sys

DEBUG = False

QUIET = False

# Enable colored text when terminal output (True), else (| or > for example) no color (False)
ISATTY = True if sys.stdout.isatty() else False
