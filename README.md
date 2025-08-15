

# Source Detection Framework 🌌

![Logo](logo.png)

![GitHub repo size](https://img.shields.io/github/repo-size/vutomimohhbe/Source-Detection-Framework)
![GitHub last commit](https://img.shields.io/github/last-commit/vutomimohhbe/Source-Detection-Framework)
![License](https://img.shields.io/github/license/vutomimohhbe/Source-Detection-Framework)

A robust framework for automated astronomical source detection using deep learning techniques, leveraging YOLOv8 for high-precision identification of celestial objects in astronomical images.

## 📖 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Results](#project-results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🌟 About the Project
The **Source Detection Framework** is designed to automate the detection of astronomical sources (e.g., stars, galaxies) in telescope-captured images. Built with YOLOv8, this project provides a scalable and efficient pipeline for processing astronomical data, suitable for researchers and astronomers.

### Built With
- [Python](https://www.python.org/) 🐍
- [YOLOv8](https://github.com/ultralytics/ultralytics) 🔍
- [Jupyter Notebook](https://jupyter.org/) 📓

## ✨ Features
- **Automated Source Detection**: Uses YOLOv8 for real-time object detection in astronomical images.
- **Modular Framework**: Easily extendable for different datasets and detection tasks.
- **Comprehensive Results**: Includes visualization and analysis tools in `Project-Results`.

## 🛠️ Installation
Follow these steps to set up the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/vutomimohhbe/Source-Detection-Framework.git
   cd Source-Detection-Framework
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *Note*: Ensure you have a `requirements.txt` file. If not, install key dependencies:
   ```bash
   pip install ultralytics jupyter numpy matplotlib
   ```

4. **Download Pre-trained YOLOv8 Model** (if applicable)
   Follow the instructions in `YOLOv8_training.ipynb` to download or train the model.

## 🚀 Usage
1. **Prepare Your Data**
   - Place your astronomical images in the `Auto_source_detect_framework/data` directory.
   - Ensure images are in a supported format (e.g., FITS, PNG, JPEG).

2. **Run the Detection Pipeline**
   ```bash
   python Auto_source_detect_framework/main.py
   ```
   *Note*: Adjust the script name based on your actual file structure.

3. **Train or Fine-tune YOLOv8**
   Open `YOLOv8_training.ipynb` in Jupyter Notebook to train the model:
   ```bash
   jupyter notebook YOLOv8_training.ipynb
   ```

4. **View Results**
   Check the `Project-Results` directory for detection outputs, visualizations, and metrics.

## 📊 Project Results
The `Project-Results` directory contains:
- **Visualizations**: Plots and annotated images of detected sources.
- **Metrics**: Precision, recall, and mAP scores for model performance.
- **Sample Outputs**: Examples of detected astronomical sources.

Example visualization:
![Sample Detection](Project-Results/sample_output.png)
*Note*: Replace with actual image paths if available.

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add YourFeature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please ensure your code follows the project's coding standards and includes relevant documentation.

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## 📬 Contact
Vutomi - [vutomimohhbe](https://github.com/vutomimohhbe)  
Project Link: [https://github.com/vutomimohhbe/Source-Detection-Framework](https://github.com/vutomimohhbe/Source-Detection-Framework)

