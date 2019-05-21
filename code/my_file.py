from thinkdsp import *

cos_sig = CosSignal(freq=440, amp = 1.0, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset = 0)
mix = sin_sig + cos_sig
wave = mix.make_wave(duration=2.0, start=0, framerate=11025)
#wave.plot()
#pyplot.show()
period = mix.period
segment = wave.segment(start=0, duration=period*3)
segment.plot()
pyplot.show()

violin_wave = thinkdsp.read_wave('input.wav')
wave.write(filename='output.wav')

