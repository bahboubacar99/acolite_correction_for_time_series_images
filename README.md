# Automatic Processing of Sentinel-2 Images with ACOLITE and Study Shapefiles
In this project, we will implement a programme that allows us to browse a series of Sentinel-2 L1C images in order to correct each one using the Acolite atmospheric correction model adapted to aquatic themes.
## Objectives
- Link Sentinel-2 images to shapefiles representing areas of interest.
- Automatically transform shapefile coordinates to the WGS 84 system.
- Define ACOLITE processing parameters for each scene.
- Run acolite_run() from Python to generate corrected products in structured folders.

## Prerequisites
- Python 3.8 or higher
- ACOLITE cloned locally from GitHub; which can find [here](https://github.com/acolite/acolite)
- Sentinel-2 data (L1C level, .SAFE format)
- Shapefile (.shp or .gpkg) associated with each image or set of images

## Installations:
**Clone ACOLITE from its official GitHub repository [here](https://github.com/acolite/acolite):**
``` bash
 git clone https://github.com/acolite/acolite.git
**Install the required libraries:**
``` bash
 pip install geopandas pyproj ```
**Update the clone path in the script:**
``` bash
acolite_path = 'chemin/vers/acolite'
sys.path.append(acolite_path)
