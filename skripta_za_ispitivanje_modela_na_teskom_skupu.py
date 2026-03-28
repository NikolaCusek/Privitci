from ultralytics import YOLO
import os
import pandas as pd

#Odabir modela
modeltype = "yolov5"
modelweight = "x" #n s m l x
ogdataset = "JPEG" #PNG JPEG

datasetweretestingon = ogdataset

testdataset = "ZavrsniDatasets/extra_dataset/" + datasetweretestingon + "/data.yaml"

model = YOLO("runs/detect/" + modeltype + modelweight + ".pt_" + ogdataset + "/weights/best.pt") 

metrics = model.val(data=testdataset, split="test")

map50 = metrics.box.map50
map5095 = metrics.box.map
recall = metrics.box.mr
precision = metrics.box.mp

csv_path = "rezultati_test_teski.csv"

#CSV
new_row = {
    "Model": modeltype + modelweight,
    "Skup podataka": ogdataset,
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