#!/usr/bin/env python2
"""
This file is part of UrliZr.

UrliZr is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

UrliZr is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with UrliZr.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.core.management import execute_manager
import imp
try:
    imp.find_module('urlizr.settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import urlizr.settings

if __name__ == "__main__":
    execute_manager(urlizr.settings)
