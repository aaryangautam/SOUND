"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=None,
            out_sig=None
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.message_port_register_out(pmt.intern("freq"))
        self.channel = 0

    def work(self, input_items, output_items):
        """Useless function"""
        return len(output_items[0])

    def change_channel(self, center_freq):
        self.channel = (self.channel + 3)%8
        freq = center_freq + (self.channel * -100e3)
        P_freq_cmd = pmt.cons(pmt.string_to_symbol("freq"), pmt.from_double(freq))
        self.message_port_pub(pmt.intern("freq"), P_freq_cmd)
        return 1
