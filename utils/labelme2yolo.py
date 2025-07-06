import json
import os

# hyperparameters
data_mode = 'val' # ['train', 'val', 'test']
img_w, img_h = [1227, 1227]
labels = ['UW', 'CW', 'DW', 'AW']

# The dictionary between label and id
label2id = {label: i for i, label in enumerate(labels)}
id2label = {i : label for label, i in label2id.items()}

# Get the path of the current dir
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)

def labelme_to_yolo(json_path, output_dir):
    with open(json_path, "r", encoding='utf-8') as f:
        data = json.load(f)

    label_lines = []

    for shape in data['shapes']:
        label_unparsed = shape['label']
        label_parsed = label_unparsed[-2:]
        points = shape['points']

        xmin = max(min(p[0] for p in points), 0)
        xmax = min(max(p[0] for p in points), img_w)
        ymin = max(min(p[1] for p in points), 0)
        ymax = min(max(p[1] for p in points), img_h)

        x_center = (xmin + xmax) / 2.0 / img_w
        y_center = (ymin + ymax) / 2.0 / img_h
        width = (xmax - xmin) / img_w
        height = (ymax - ymin) / img_h

        if label_parsed not in label2id: 
            raise ValueError(f"A undefined label occurred '{label_parsed}', only labels in {labels} are allowed!!!")
        else:
            class_id = label2id[label_parsed]
        label_lines.append(f"{class_id} {x_center} {y_center} {width} {height}")

    base = os.path.splitext(os.path.basename(json_path))[0]
    txt_path = os.path.join(output_dir, base + ".txt")
    with open(txt_path, 'w') as f:
        f.write('\n'.join(label_lines))

# All three modes
if data_mode == 'train':
    json_dir = current_dir + "/../data/train"
    output_dir = current_dir + "/../label/train"
elif data_mode == 'val':
    json_dir = current_dir + "/../data/val"
    output_dir = current_dir + "/../label/val"
elif data_mode == 'test':
    json_dir = current_dir + "/../data/test"
    output_dir = current_dir + "/../label/test"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(json_dir):
    if file.endswith('.json'):
        labelme_to_yolo(os.path.join(json_dir, file), output_dir)
