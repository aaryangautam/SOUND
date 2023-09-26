#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Frequency Hopping Spread Spectrum Lab
# Author: Solomon
# Copyright: Solomon
# GNU Radio version: 3.9.5.0-rc1

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import learning_fhss_epy_block_0 as epy_block_0  # embedded python block
import math
import numpy as np
import osmosdr
import time
import pmt
import threading




class learning_fhss(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Frequency Hopping Spread Spectrum Lab", catch_exceptions=True)
        readList = []
        with open("guiVariables.txt") as f:
            [readList.append(line.strip()) for line in f.readlines()]
        centerF = float(readList[0])
        ##################################################
        # Variables
        ##################################################
        self.vol_lvl = vol_lvl = 1
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.samp_rate = samp_rate = 4.8e6
        self.center_freq = center_freq = centerF

        ##################################################
        # Blocks
        ##################################################
        self.epy_block_0 = epy_block_0.blk()
        def _variable_function_probe_0_probe():
          while True:

            val = self.epy_block_0.change_channel(center_freq)
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_variable_function_probe_0,val))
              except AttributeError:
                self.set_variable_function_probe_0(val)
            except AttributeError:
              pass
            time.sleep(1.0 / (5))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=100,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_sink_0.set_time_source('gpsdo', 0)
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(32000)
        self.osmosdr_sink_0.set_center_freq(center_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(20, 0)
        self.osmosdr_sink_0.set_if_gain(30, 0)
        self.osmosdr_sink_0.set_bb_gain(30, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(2000000, 0)
        self.freq_xlating_fir_filter_xxx_1 = filter.freq_xlating_fir_filter_ccc(1, [1], 0, samp_rate)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/pi/Documents/TE/SDRtransmittest.wav', True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(vol_lvl)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(2*math.pi*(5e3)/samp_rate)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.epy_block_0, 'freq'), (self.freq_xlating_fir_filter_xxx_1, 'freq'))
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.freq_xlating_fir_filter_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_frequency_modulator_fc_0, 0))


    def get_vol_lvl(self):
        return self.vol_lvl

    def set_vol_lvl(self, vol_lvl):
        self.vol_lvl = vol_lvl
        self.blocks_multiply_const_vxx_0.set_k(self.vol_lvl)

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_frequency_modulator_fc_0.set_sensitivity(2*math.pi*(5e3)/self.samp_rate)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_sink_0.set_center_freq(self.center_freq, 0)




def main(top_block_cls=learning_fhss, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
