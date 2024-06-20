from astropy.io import fits
import numpy as np

# Load the FITS file
file_path = 'NGC7538_Halpha.fits'
hdul = fits.open(file_path)
data = hdul[1].data
hdul.close()

# Measure Halpha surface brightness
I_Halpha = np.mean(data)  # Average Halpha surface brightness

# Estimate electron density
n_e = np.sqrt((I_Halpha * (1/4.25e10)) / 1.36e-12)

# Assume electron temperature
T_e = 10000  # in Kelvin

# Calculate thermal energy density
k_B = 1.38e-16  # Boltzmann constant in erg K^-1
E_density = (3 / 2) * n_e * k_B * T_e

#Volume estimation of a half sphere
r = 2.45447 * 3.086e18 # pc to cm 
volume = (4 * np.pi * r**3)/3

# Calculate total thermal energy (assuming a known volume)
#volume = 1e60  # Example volume in cubic centimeters
E_total = E_density * (volume/2)

print(f"Electron Density (n_e): {n_e} cm^-3")
print(f"Electron Temperature (T_e): {T_e} K")
print(f"Thermal Energy Density: {E_density} erg cm^-3")
print(f"Total Thermal Energy: {E_total} erg")
