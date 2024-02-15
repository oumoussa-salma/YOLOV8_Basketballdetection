from ultralytics import YOLO

model =YOLO("finalModelTrainned.pt")

results = model.track(source='C:\\Users\salma\Pycharm\Projects\YOLOv8Detection\\finalTest\\videos\\vid2.mp4', show=True, tracker="bytetrack.yaml")