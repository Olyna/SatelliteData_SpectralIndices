# SatelliteData_SpectralIndices
Spectral Indices for Landsat_5, Landsat_8 &amp; Sentinel_2.

## Usage
The bandsForIndices() function accepts as input parameters an abbreviation of the satellite name (satellite), and a list of fullpaths which relate to the bands of a single scene (bandsInOneTile). For Landsat satellites is possible to calculate spectral indices for which is required band SWIR. This is not possible for Sentinel 2, because Sentinel 2 SWIR band has a different resolution, thus needs to be resampled from 20 to 10 meters.

The function returns fullpaths of images that will be called later by functions calc_...().