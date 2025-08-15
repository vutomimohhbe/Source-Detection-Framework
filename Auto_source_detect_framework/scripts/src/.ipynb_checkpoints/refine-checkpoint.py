import pandas as pd
from astropy.io import fits
from astropy.wcs import WCS
import os

def convert_catalog_to_yolo(catalog_path, fits_path, label_dir, img_size=1024):
    catalog = pd.read_csv(catalog_path)
    hdu = fits.open(fits_path)[0]
    wcs = WCS(hdu.header)
    os.makedirs(label_dir, exist_ok=True)

    for index, row in catalog.iterrows():
        ra, dec = row['RA'], row['DEC']
        pix_coords = wcs.all_world2pix([[ra, dec]], 0)[0]
        x_center = pix_coords[0] / img_size
        y_center = 1 - (pix_coords[1] / img_size)
        width, height = 0.01, 0.01  # Adjust based on source size
        label = f"0 {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"
        with open(os.path.join(label_dir, f'patch_{index}.txt'), 'w') as f:
            f.write(label)
    print(f"Converted {len(catalog)} labels to {label_dir}")

if __name__ == "__main__":
    convert_catalog_to_yolo('/users/vutomi/Source_Detection/YOLOs/Data/catalogs/Abell_209_pybdsf_refined.cat',
                           '/users/vutomi/Source_Detection/YOLOs/Data/images/Abell_209_aFix_pol_I_15arcsec_fcube_cor_2d.fits',
                           '/users/vutomi/Source_Detection/YOLOs/Data/labels/abell_209_refined')
