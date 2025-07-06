# Plastic-Detection
The training code for plastic detection

## Project Structure
The project structure is
```
Plastic-Detection
├── README.md
├── data
│   ├── train
│   └── val
├── data.yaml
├── detect.py
├── label
│   ├── train
│   └── val
├── total_data.zip
├── total_val.zip
├── train.py
├── train_config.yaml
└── utils
    └── labelme2yolo.py
```

## Dependecies
- Before training, please use `pip install ultralytics` to install the available YOLO model.

## Training data & Evaluation data
- Training data: Data from Fuzhou(福州) are used for training.
- Evaluation data: Data from Qingdao(青岛) are used for evaluation.