import subprocess
import os
from pathlib import Path

def run_inference(weights_path, img_size, source_dir, output_dir, conf_threshold=0.07, data_config="configs/data.yaml"):
    run_name = 'preds with CBAM'
    label_dir = Path(output_dir) / run_name / 'labels'

    # Run YOLOv5 inference
    cmd = [
        'python', '-m', 'yolov5.detect',
        '--weights', weights_path,
        '--img', str(img_size),
        '--conf', str(conf_threshold),
        '--source', source_dir,
        '--data', data_config,
        '--project', output_dir,
        '--name', run_name,
        '--exist-ok',
        '--save-txt',
        '--save-conf'
    ]
    subprocess.run(cmd, check=True)
    print(f"\n✅ Inference results saved to {output_dir}/{run_name}")

    # Count detections per image
    total_sources = 0
    print("\n📊 Detection Summary:")
    for img_file in sorted(Path(source_dir).glob("*.png")):
        label_file = label_dir / f"{img_file.stem}.txt"
        if label_file.exists():
            with open(label_file, "r") as f:
                detections = f.readlines()
            count = len(detections)
        else:
            count = 0
        total_sources += count
        print(f" - {img_file.name}: {count} sources detected")

    print(f"\n✅ Total sources detected across all images: {total_sources}")

if __name__ == "__main__":
    run_inference(
        '/users/vutomi/Source_Detection/YOLOs/training_models/yolov5/runs/train/exp5/weights/best.pt',
        640,
        '/users/vutomi/Source_Detection/YOLOs/Data/images/patches',
        '/users/vutomi/Auto_source_detect_framework/outputs/runs',
        0.07,
        '/users/vutomi/Auto_source_detection_framework/configs/data.yaml'
    )