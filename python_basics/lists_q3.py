# q.3 We are given the following list of energy sources.

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

# Write som code to remove 'fossil' from the list and, then add 'geothermal' to the end of the lst.

del energy[0]
energy.append('geothermal')
print(energy)