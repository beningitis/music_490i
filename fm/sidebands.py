def get_sidebands(carrierFreq, modulationRatio, modulationIndex):
	modulationFreq = carrierFreq * modulationRatio
	sideband_frequencies = []
	for i in range(0, 20):
		freq = carrierFreq + i * modulationIndex * modulationFreq
		if freq > 0: 
			sideband_frequencies.insert(0, freq)
	return sideband_frequencies