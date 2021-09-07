# (c) Copyright 2021 by Coinkite Inc. This file is covered by license found in COPYING-CC.
#
# mk4.py - Mk4 specific code, not needed on earlier devices.
#
#
import sys, uos, pyb, glob

def make_flash_fs():
    print("Would rebuild /flash")


def init0():
    # called very, very early

    # (fake) NFC interface
    import sim_nfc
    sys.modules['nfc'] = sim_nfc
    n = sim_nfc.SimulatedNFCHandler()
    n.setup()
    glob.NFC = n
    


# EOF