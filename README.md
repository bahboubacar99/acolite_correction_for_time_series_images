# Automatic Processing of Sentinel-2 Images with ACOLITE and Study Shapefiles
In this project, we will implement a programme that allows us to browse a series of Sentinel-2 L1C images in order to correct each one using the Acolite atmospheric correction model adapted to aquatic themes.
## About ACOLITE
ACOLITE is an open-source software designed for atmospheric correction and the removal of sun glint from satellite images, converting top-of-atmosphere reflectance into surface reflectance. It was initially developed for processing aquatic scenes, particularly in turbid waters, and is now widely used for various water quality analyses, including plastic debris detection. ACOLITE offers two main correction methods: EXP (Exponential Extrapolation) and DSF (Dark Spectrum Fitting). The EXP method estimates aerosol reflectance using Rayleigh-corrected SWIR bands and extrapolates this to visible and NIR bands via an exponential function, but its accuracy is limited in blue bands and turbid waters due to the assumption of zero water reflectance. The DSF method is more robust, identifying the darkest pixels in the scene to estimate atmospheric path reflectance and aerosol optical depth, and it can be applied globally, in tiles, or even per pixel. DSF also includes sun glint correction using SWIR bands or alternative approaches, reducing the impact of specular reflection on the retrieved surface reflectance. Overall, DSF is generally preferred over EXP for complex aquatic environments, while EXP can be used for faster, simpler corrections in clear water conditions. for more detail about acolite visit [here](https://odnature.naturalsciences.be/downloads/remsem/acolite/acolite_manual_20210802.0.pdf)
## Objectives
- Link Sentinel-2 images to shapefiles representing areas of interest.
- Automatically transform shapefile coordinates to the WGS 84 system.
- Define ACOLITE processing parameters for each scene.
- Run acolite_run() from Python to generate corrected products in structured folders.

## Prerequisites
- Python 3.8 or higher
- ACOLITE cloned locally from GitHub and it dependaces libraries; which can find [here](https://github.com/acolite/acolite)
- Sentinel-2 data (L1C level, .SAFE format)
- Shapefile (.shp or .gpkg) associated with each image or set of images

## Installations:
**Clone ACOLITE from its official GitHub repository and it dependaces libraries [here](https://github.com/acolite/acolite):**
``` bash
 git clone https://github.com/acolite/acolite.git
```
``` bash
 pip install numpy matplotlib scipy gdal libgdal-jp2openjpeg libgdal-netcdf pyproj scikit-image pyhdf pyresample netcdf4 h5py requests pygrib cartopy zarr
```
**Install the required libraries:**
``` bash
 pip install geopandas pyproj
```
**Update the clone path in the script:**
``` bash
acolite_path = 'chemin/vers/acolite'
sys.path.append(acolite_path)
```

