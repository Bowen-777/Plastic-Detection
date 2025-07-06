from ultralytics import YOLO
import yaml
import argparse

# parse parameters
parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, default='data.yaml', help='Path to data config')
parser.add_argument('--params', type=str, default='train_config.yaml', help='Path to training params')
args = parser.parse_args()

with open(arg.data, 'r') as f:
    data_config = yaml.safe_load(f)

with open(arg.params, 'r') as f:
    train_config = yaml.safe_load(f)

# For simplicity 
cfg = train_config

model = YOLO(cfg['model'])


model.train(
    data=args.data,
    epochs=cfg['epochs'],
    imgsz=cfg['imgsz'],
    batch=cfg['batch'],
    optimizer=cfg['optimizer']['type'],
    lr0=cfg['optimizer']['lr0'],
    momentum=cfg['optimizer']['momentum'],
    weight_decay=cfg['optimizer']['weight_decay'],
    patience=cfg['patience'],
    project=cfg['project'],
    name=cfg['name'],
    exist_ok=cfg.get('exist_ok', False)
)