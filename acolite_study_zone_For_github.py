# add acolite clone to Python path and import acolite
import sys, os
import shutil
import sys, os
import geopandas as gpd
from pyproj import Transformer
import glob
# add acolite clone to Python path and import acolite
user_home = os.path.expanduser("~")
acolite_path =  'path where acolite github where clone'
sys.path.append(acolite_path)
import acolite as ac

# Fonction pour transformer les limites de projection vers WGS 84
def transform_to_wgs84(bounds, crs):
    # Transformer pour la projection WGS 84 (EPSG:4326)
    transformer = Transformer.from_crs(crs, 'EPSG:4326', always_xy=True)
    minx, miny = transformer.transform(bounds[0], bounds[1])
    maxx, maxy = transformer.transform(bounds[2], bounds[3])
    return [minx, miny, maxx, maxy]

## path to S2 image folder .SAFE
sentinel_2_dir = './IMAGES_FOR_STUDY_DATASET'

# Recherche de tous les répertoires correspondant aux critères
scene_dirs = glob.glob(os.path.join(sentinel_2_dir, '**/*MSIL1C*.SAFE'), recursive=True)

bundles = scene_dirs

# output directory
output_dir_base  = './STUDY_DATASET_PROCESSEDS/ACOLITE_results_study'

# optional file with processing settings
# if set to None defaults will be used
settings_file = None

# run through bundles
for bundle in bundles:
    
   # Create a folder for each bundle
    parent_dir_name = os.path.basename(os.path.dirname(bundle))
    output_dir_bundle = os.path.join( output_dir_base, "ACOLITE_study_results_" + parent_dir_name)
    os.makedirs(output_dir_bundle, exist_ok=True)

     # Find the shapefile in the parent directory of the current bundle directory
    parent_dir = os.path.dirname(bundle)
    #shapefile_paths = glob.glob(os.path.join(parent_dir, '*.shp'))+ glob.glob(os.path.join(parent_dir, '*.gpkg'))
    shapefile_parent_dir = os.path.dirname(parent_dir)
    shapefile_paths = glob.glob(os.path.join(shapefile_parent_dir, '*.shp')) + glob.glob(os.path.join(shapefile_parent_dir, '*.gpkg'))

                      
    if shapefile_paths:
        shapefile_paths = shapefile_paths[0]  # Take the first shapefile found
        # Read the shapefile and get its bounds 
        gdf = gpd.read_file(shapefile_paths)
        bounds = gdf.total_bounds
        crs = gdf.crs

        print("les limites avant projection")

        print(bounds)
        print (crs)

        # Transform the bounds to WGS 84 coordinates
        limit = transform_to_wgs84(bounds, crs)
        # Adjust the order of coordinates
        limit_ajusted = [limit[1], limit[0], limit[3], limit[2]]
        print(limit_ajusted)

        # import settings 
        settings = ac.acolite.settings.parse(settings_file)
        # set settings provided above
        settings['limit'] = limit_ajusted
        settings['inputfile'] = bundle
        settings['output'] = output_dir_bundle
        # other settings can also be provided here, e.g.
        settings['l2w_parameters'] = ['rhos_*']
        settings['geometry_type']= 'grids_footprint'
        settings['output_xy'] = 'True'
        # other settings can also be provided see documentation
        
        try:
          ac.acolite.acolite_run(settings=settings)
        except Exception as e:
          print(f"Error processing {bundle}: {e}")
    
    
    else:
        print(f"No shapefile found in {bundle}. Skipping.")
                


