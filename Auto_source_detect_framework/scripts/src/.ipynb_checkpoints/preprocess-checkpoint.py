from astropy.io import fits
import numpy as np
import os
import matplotlib.pyplot as plt
import sys

def preprocess_fits(fits_path, output_dir, label_path, patch_size=1024, overlap=256):  # Updated patch_size to 1024, overlap to 256 (25%)
    # Load FITS data
    try:
        hdu = fits.open(fits_path)[0]
        data = hdu.data
        img_shape = (hdu.header['NAXIS2'], hdu.header['NAXIS1'])  # (3617, 3617)
    except Exception as e:
        print(f"Error loading FITS file: {e}")
        return

    # Patch parameters
    step_size = patch_size - overlap
    label_dir = os.path.join(output_dir, 'labels')
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(label_dir, exist_ok=True)

    # Read original labels
    try:
        with open(label_path, 'r') as f:
            lines = [line.strip().split() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Label file {label_path} not found. No labels will be generated.")
        lines = []

    # Generate patches and adjust labels
    count = 0
    print("Slicing Images ...")
    for i in range(0, img_shape[1] - patch_size + 1, step_size):
        for j in range(0, img_shape[0] - patch_size + 1, step_size):
            patch = data[j:j+patch_size, i:i+patch_size]
            # Normalize with min-max scaling
            patch_normalized = (patch - np.min(patch)) / (np.max(patch) - np.min(patch) + 1e-10)  # Avoid division by zero
            patch_filename = f'patch_{i//step_size}_{j//step_size}.png'
            try:
                plt.imsave(os.path.join(output_dir, patch_filename), patch_normalized, cmap='gray', origin='lower', vmin=0, vmax=1)
                count += 1
            except Exception as e:
                print(f"Error saving {patch_filename}: {e}")
                continue

            # Adjust labels for this patch
            patch_labels = []
            for line in lines:
                try:
                    class_id, x_center_norm, y_center_norm, width_norm, height_norm = map(float, line)
                    x_center = x_center_norm * img_shape[1]
                    y_center = (1 - y_center_norm) * img_shape[0]  # Reverse YOLO flip

                    # Check if center is within patch
                    if i <= x_center < i + patch_size and j <= y_center < j + patch_size:
                        x_patch = (x_center - i) / patch_size
                        y_patch = (y_center - j) / patch_size
                        width_patch = width_norm * (img_shape[1] / patch_size)
                        height_patch = height_norm * (img_shape[0] / patch_size)
                        if 0 <= x_patch <= 1 and 0 <= y_patch <= 1 and width_patch > 0 and height_patch > 0:
                            patch_labels.append(f"0 {x_patch:.6f} {y_patch:.6f} {width_patch:.6f} {height_patch:.6f}")
                except ValueError:
                    print(f"Skipping invalid label line: {line}")
                    continue

            if patch_labels:
                with open(os.path.join(label_dir, f'patch_{i//step_size}_{j//step_size}.txt'), 'w') as f:
                    f.write('\n'.join(patch_labels))

    print(f"Generated {count} patches and corresponding labels in {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python preprocess.py <fits_path> <output_dir> <label_path>")
        sys.exit(1)
    preprocess_fits(sys.argv[1], sys.argv[2], sys.argv[3])
