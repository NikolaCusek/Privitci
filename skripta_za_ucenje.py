import torch
from ultralytics.nn.tasks import DetectionModel
from torch.serialization import add_safe_globals, safe_globals
import time
import pandas as pd
from ultralytics import YOLO
import os

add_safe_globals([DetectionModel])

# with safe_globals([DetectionModel]):
#     model = YOLO("yolov8n.pt")

#n - 7.2, s - 13.4, m - 23.6, l 19.2, x 24.6
#n - 4.3, s - 13.9, m - 14.8, l 18.8, 

chooser = []
for i, h in zip(("yolo11s.pt","yolo11m.pt", "yolo11l.pt", "yolo11x.pt"), (32, 32, 32, 16, 16)):
    for g in ("PNG", "JPEG"):
        chooser.append((i, h, g))

iterat = 7 #Rusi se u slucaju ako pokusam staviti cijelu skriptu za ucenje u for petlju, zato se to radi rucno

#Postavke
chosen_model = chooser[iterat][0]

model = YOLO(chosen_model)


whichdataset = chooser[iterat][2]
train_epochs = 100 # 100    
image_size = 640 # 640
learning_rate  = 0.01 # 0.01
batch  = chooser[iterat][1] # 16
csv_path = "rezultati_test.csv"

if whichdataset == "PNG":
    dataset = "ZavrsniDatasets/PNG/data.yaml"
elif whichdataset == "JPEG":
    dataset = "ZavrsniDatasets/JPEG/data.yaml"
else:
    dataset = ""

starttraintime = time.time()
#Ucenje
model_name = chosen_model + "_" + whichdataset
results = model.train(data= dataset, epochs= train_epochs, lr0= learning_rate, imgsz= image_size, batch = batch, amp=False, half=False, degrees = 22.5, name= model_name)

training_time = time.time() - starttraintime

print(f"Training took {training_time:.2f}s")

#Zapis podataka
model = YOLO("runs/detect/" + model_name + "/weights/best.pt")
metrics = model.val(data=dataset, split="test")

map50 = metrics.box.map50
map5095 = metrics.box.map
recall = metrics.box.mr
precision = metrics.box.mp

print(f"mAP50: {map50:.4f}")
print(f"mAP50-95: {map5095:.4f}")
print(f"Recall: {recall:.4f}")


#CSV
new_row = {
    "Model": chosen_model,
    "Skup podataka": dataset,
    "Broj epoha": train_epochs,
    "Veličina slike": image_size,
    "Stopa Učenja": learning_rate,
    "Batch size": batch,
    "Vrijeme Učenja (s)": round(training_time, 2),
    "mAP:50": round(map50, 4),
    "mAP:95": round(map5095, 4),
    "Recall": round(recall, 4),
    "Precision": round(precision, 4)
}

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
else:
    df = pd.DataFrame([new_row])

df.to_csv(csv_path, index=False)

print("Results saved")