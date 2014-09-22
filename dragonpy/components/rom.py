# coding: utf-8

"""
    DragonPy - Dragon 32 emulator in Python
    =======================================

    :created: 2014 by Jens Diemer - www.jensdiemer.de
    :copyleft: 2014 by the DragonPy team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from __future__ import absolute_import, division, print_function
import os
import logging

log = logging.getLogger(__name__)


class ROMFile(object):
    def __init__(self, filepath, address, max_size=None):
        self.filepath = filepath
        self.address = address
        self.max_size = max_size

        if not os.path.isfile(self.filepath):
            log.log(99, "Error ROM file not found: '%s'", self.filepath)