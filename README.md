
# Total thermal energy estimation for NGC 7538

## Description

This Python script calculates the electron density (`n_e`) and total thermal energy (`E_thermal`) of an H II region using Hα observations. The script processes FITS files to extract Hα surface brightness and uses empirical formulas to derive the desired physical properties.

## Prerequisites

- Python 3.x
- The following Python packages:
  - `astropy`
  - `numpy`

You can install the required packages using pip:
```bash
pip install astropy numpy
```

## Usage

### Step-by-Step Guide

1. **Import Required Libraries**: Start by importing necessary libraries.

   ```python
   from astropy.io import fits
   import numpy as np
   ```

2. **Load the FITS File**: Load the Hα surface brightness data from the FITS file.

   ```python
   # Load the FITS file
   file_path = 'path_to_your_fits_file.fits'  # Update with your file path
   hdul = fits.open(file_path)
   data = hdul[0].data
   hdul.close()
   ```

3. **Inspect the Data**: Optionally, inspect the data to understand its structure.

   ```python
   # Inspect the data
   print(data.shape)
   ```

4. **Measure Hα Surface Brightness**: Calculate the mean or total surface brightness of the Hα emission.

   ```python
   # Calculate the mean Hα surface brightness
   I_Halpha = np.mean(data)
   ```

5. **Estimate Electron Density**: Use the empirical relationship between Hα surface brightness and electron density.

   ```python
   # Estimate electron density
   n_e = np.sqrt(I_Halpha / 1.36e-12)
   ```

6. **Assume Electron Temperature**: Assume a typical electron temperature for H II regions.

   ```python
   # Assume electron temperature
   T_e = 10000  # in Kelvin
   ```

7. **Calculate Thermal Energy Density**: Use the formula for thermal energy density.

   ```python
   # Boltzmann constant
   k_B = 1.38e-16  # in erg K^-1

   # Calculate thermal energy density
   E_density = (3 / 2) * n_e * k_B * T_e
   ```

8. **Calculate Total Thermal Energy**: Calculate the total thermal energy using the volume of the H II region.

   ```python
   # Assuming a volume in cubic centimeters (example volume)
   volume = 1e60  # in cm^3

   # Calculate total thermal energy
   E_total = E_density * volume

   # Print the results
   print(f"Electron Density (n_e): {n_e} cm^-3")
   print(f"Thermal Energy Density: {E_density} erg cm^-3")
   print(f"Total Thermal Energy: {E_total} erg")
   ```

### Full Code Example

Here is the complete code as described above:

```python
from astropy.io import fits
import numpy as np

# Load the FITS file
file_path = 'path_to_your_fits_file.fits'  # Update with your file path
hdul = fits.open(file_path)
data = hdul[0].data
hdul.close()

# Inspect the data
print(data.shape)

# Calculate the mean Hα surface brightness
I_Halpha = np.mean(data)

# Estimate electron density
n_e = np.sqrt(I_Halpha / 1.36e-12)

# Assume electron temperature
T_e = 10000  # in Kelvin

# Boltzmann constant
k_B = 1.38e-16  # in erg K^-1

# Calculate thermal energy density
E_density = (3 / 2) * n_e * k_B * T_e

#Volume estimation of a half sphere
r = 2.45447 * 3.086e18 # pc to cm 
volume = (4 * np.pi * r**3)/3

# Calculate total thermal energy for a half sphere as NGC 7538
# half sphere morphology.
E_total = E_density * (volume/2)

# Print the results
print(f"Electron Density (n_e): {n_e} cm^-3")
print(f"Thermal Energy Density: {E_density} erg cm^-3")
print(f"Total Thermal Energy: {E_total} erg")
```

## Results for NGC 7538

Electron Density (n_e): 55.91 cm^-3

Electron Temperature (T_e): 10000 K

Thermal Energy Density: 1.16e-10 erg cm^-3

Total Thermal Energy: 1.05e+47 erg

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the astropy and numpy communities for providing the tools used in this script.
- Special thanks to the authors and researchers whose empirical relationships and formulas were utilized.
