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


    
#Postavke
chosen_model = "yolov8n.pt"

model = YOLO(chosen_model)

train_epochs = 100 # 100    
image_size = 896 # 640
learning_rate  = 0.01 # 0.01
batch  = 16 # 16
dataset = "ZavrsniDatasets/PNG/data.yaml"
csv_path = "rezultati_val.csv"


starttraintime = time.time()
#Ucenje
results = model.train(data= dataset, epochs= train_epochs, lr0= learning_rate, imgsz= image_size, batch = batch, amp=False, half=False, degrees = 22.5)

training_time = time.time() - starttraintime

print(f"Training took {training_time:.2f}s")

#Zapis podataka
metrics = model.val(data=dataset)

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

#df.to_csv(csv_path, index=False)

print("Results saved.csv")