#!/bin/bash
set -e  # Exit on any error

# Configuration
FITS_PATH="/users/vutomi/abell_133.fits"
WEIGHTS_PATH="/users/vutomi/Source_Detection/YOLOs/training_models/yolov5/runs/train/exp5/weights/best.pt"
DATA_CONFIG="/users/vutomi/Auto_source_detect_framework/configs/data.yaml"
OUTPUT_DIR="/users/vutomi/Auto_source_detect_framework/outputs"
LABEL_PATH="/users/vutomi/Source_Detection/YOLOs/Data/labels/abell_133.txt"
PATCH_SIZE=640
CONF_THRESHOLD=0.07
BATCH_SIZE=1
EPOCHS=10

# Steps
# echo "Step 1: Preprocessing FITS to patches"
# echo "Slicing Images ..."
#python src/preprocess.py "$FITS_PATH" "$OUTPUT_DIR/processed/abell_133_patches" $PATCH_SIZE
#python src/preprocess.py "$FITS_PATH" "$OUTPUT_DIR/processed/abell_133_patches" "$LABEL_PATH"


# echo "Step 2: Running inference on unlabelled patches"
#python src/detect.py "$WEIGHTS_PATH" $PATCH_SIZE "$OUTPUT_DIR/processed/abell_133_patches" "$OUTPUT_DIR/runs" $CONF_THRESHOLD "$DATA_CONFIG"

#echo "Step 3: Loding and Refining catalog"
# Manual CARTA refinement here, then run:
#python src/refine.py "/users/vutomi/Source_Detection/YOLOs/Data/catalogs/Abell_209_pybdsf_refined.cat" "$FITS_PATH" "$OUTPUT_DIR/labels/abell_209_refined"

#echo "Step 4: Training YOLO plus CBAM"
#python src/train.py "$DATA_CONFIG" $PATCH_SIZE $BATCH_SIZE $EPOCHS "$WEIGHTS_PATH" "$OUTPUT_DIR/runs"

echo "Running inference on unlabelled patches"
python src/detect.py "$WEIGHTS_PATH" $PATCH_SIZE "/users/vutomi/Source_Detection/YOLOs/Data/images/patches" "$OUTPUT_DIR/runs" $CONF_THRESHOLD "$DATA_CONFIG"


echo "Pipeline completed!"
