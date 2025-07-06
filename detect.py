from ultralytics import YOLO

def detect(img_path):
    model = YOLO("runs/train/last.pt")
    results = model(img_path)
    results[0].show()
    results[0].save("result.jpg")
    
if __name__ == "__main__":
    detect("test.jpg")