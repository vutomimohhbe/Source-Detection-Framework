from astropy.io import fits
from astropy.wcs import WCS
import logging

def pix_to_world(fits_path, x, y):
    hdu = fits.open(fits_path)[0]
    wcs = WCS(hdu.header)
    return wcs.wcs_pix2world([[x, y]], 0)[0]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
