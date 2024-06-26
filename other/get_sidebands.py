def get_sidebands(carrierFreq, modulationFreq, modulationIndex):
	sideband_frequencies = []
	for i in range(-5, 5):
		freq = carrierFreq + i * modulationIndex * modulationFreq
		if freq > 0: 
			sideband_frequencies.insert(-1, freq)
	return sideband_frequencies.sort()