def get_sidebands(carrier_freq, mod_freq, mod_index):
	sidebandFrequencies = []
	for i in range(-10, 10):
		sidebandFrequencies.insert(carrier_freq + i * mod_index * mod_freq)
	return sidebandFrequencies
