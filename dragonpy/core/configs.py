# coding: utf-8

"""
    DragonPy - Dragon 32 emulator in Python
    =======================================

    :created: 2013 by Jens Diemer - www.jensdiemer.de
    :copyleft: 2013-2014 by the DragonPy team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

import inspect
import struct
import multiprocessing


from dragonlib.utils.logging_utils import log


DRAGON32 = "Dragon32"
DRAGON64 = "Dragon64"
COCO2B = "COCO2B"
SBC09 = "sbc09"
SIMPLE6809 = "Simple6809"
MULTICOMP6809 = "Multicomp6809"
VECTREX = "Vectrex"


class MachineDict(dict):
    DEFAULT = None
    def register(self, name, cls, default=False):
        dict.__setitem__(self, name, cls)
        if default:
            assert self.DEFAULT is None
            self.DEFAULT = name

machine_dict = MachineDict()


class DummyMemInfo(object):
    def get_shortest(self, *args):
        return ">>mem info not active<<"
    def __call__(self, *args):
        return ">>mem info not active<<"


class AddressAreas(dict):
    """
    Hold information about memory address areas which accessed via bus.
    e.g.:
        Interrupt vectors
        Text screen
        Serial/parallel devices
    """
    def __init__(self, areas):
        super(AddressAreas, self).__init__()
        for start_addr, end_addr, txt in areas:
            self.add_area(start_addr, end_addr, txt)

    def add_area(self, start_addr, end_addr, txt):
        for addr in xrange(start_addr, end_addr + 1):
            dict.__setitem__(self, addr, txt)


class BaseConfig(object):
#     # http address/port number for the CPU control server
#     CPU_CONTROL_ADDR = "127.0.0.1"
#     CPU_CONTROL_PORT = 6809

    # How many ops should be execute before make a control server update cycle?
    BURST_COUNT = 10000

    DEFAULT_ROMS = {}

    def __init__(self, cfg_dict):
        self.cfg_dict = cfg_dict
        self.cfg_dict["cfg_module"] = self.__module__ # FIXME: !

        assert self.RAM_SIZE == (self.RAM_END - self.RAM_START) + 1
        assert self.ROM_SIZE == (self.ROM_END - self.ROM_START) + 1

        log.debug("cfg_dict: %s", repr(cfg_dict))

#         # socket address for internal bus I/O:
#         if cfg_dict["bus_socket_host"] and cfg_dict["bus_socket_port"]:
#             self.bus = True
#             self.bus_socket_host = cfg_dict["bus_socket_host"]
#             self.bus_socket_port = cfg_dict["bus_socket_port"]
#         else:
#             self.bus = None # Will be set in cpu6809.start_CPU()

        self.ram = cfg_dict.get("ram", None)

#         if cfg_dict["rom"]:
#             raw_rom_cfg = cfg_dict["rom"]
#             raise NotImplementedError("TODO: create rom cfg!")
#         else:
        self.rom_cfg = self.DEFAULT_ROMS

        if cfg_dict["trace"]:
            self.trace = True
        else:
            self.trace = False

        self.verbosity = cfg_dict["verbosity"]

        self.mem_info = DummyMemInfo()
        self.memory_byte_middlewares = {}
        self.memory_word_middlewares = {}

    def _get_initial_Memory(self, size):
        return [0x00] * size

    def get_initial_RAM(self):
        return self._get_initial_Memory(self.RAM_SIZE)

    def get_initial_ROM(self):
        return self._get_initial_Memory(self.ROM_SIZE)

#     def get_initial_ROM(self):
#         start=cfg.ROM_START, size=cfg.ROM_SIZE
#         self.start = start
#         self.end = start + size
#         self._mem = [0x00] * size

    def print_debug_info(self):
        print "Config: '%s'" % self.__class__.__name__

        for name, value in inspect.getmembers(self): # , inspect.isdatadescriptor):
            if name.startswith("_"):
                continue
#             print name, type(value)
            if not isinstance(value, (int, basestring, list, tuple, dict)):
                continue
            if isinstance(value, (int,)):
                print "%20s = %-6s in hex: %7s" % (
                    name, value, hex(value)
                )
            else:
                print "%20s = %s" % (name, value)


def test_run():
    import os, sys, subprocess
    cmd_args = [sys.executable,
        os.path.join("..", "..", "DragonPy_CLI.py"),

#         "--verbosity=5",
        "--verbosity=10", # DEBUG
#         "--verbosity=20", # INFO
#         "--verbosity=30", # WARNING
#         "--verbosity=40", # ERROR
#         "--verbosity=50", # CRITICAL/FATAL

#         "--machine=Simple6809",
        "--machine=sbc09",
    ]
    print "Startup CLI with: %s" % " ".join(cmd_args[1:])
    subprocess.Popen(cmd_args, cwd=".").wait()

if __name__ == "__main__":
    test_run()
