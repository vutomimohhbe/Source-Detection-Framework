import subprocess

def train_model(data_config, img_size, batch_size, epochs, weights_path, project_dir, custom_yaml="/users/vutomi/Auto_source_detect_framework/scripts/yolov5/models/custom_yolov5s.yaml"):
    cmd = [
        'python', '-m', 'yolov5.train',
        '--img', str(img_size),
        '--batch', str(batch_size),
        '--epochs', str(epochs),
        '--data', data_config,
        '--cfg', custom_yaml,  # Use custom config with CBAM
        '--weights', weights_path,
        '--project', project_dir,
        '--name', 'last YOLO cbam',  # Updated name to reflect CBAM
        '--exist-ok'
    ]
    subprocess.run(cmd, check=True)
    print(f"Training completed, results in {project_dir}/active_learning_cycle_with_cbam")

if __name__ == "__main__":
    train_model('/users/vutomi/Auto_source_detect_framework/configs/data.yaml',
                1024, 1, 10,
                '/users/vutomi/Source_Detection/YOLOs/training_models/yolov5/runs/train/exp5/weights/best.pt',
                '/users/vutomi/Source_Detection/YOLOs/outputs/runs')