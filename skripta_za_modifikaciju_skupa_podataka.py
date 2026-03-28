import os as os

def RoboToNormal(x): #Roboflow doda puno toga na originalno ime datoteke, ovime se dobi originalno ime datoteke
    y = ""
    for i in x:
        if i == '_':
            break
        y = y + i
    return y + ".png"
            
def JPGPNGconverter(x): #Uzme ime datoteke koja se zamjenjuje i promijeni ekstenziju u png
    y = ""
    x = x[::-1]
    k = 0
    for i in x:
        if k > 0:
            y = y + i
        if i == ".":
            k = k + 1
    y = y[::-1]
    return y + ".png"
        
        


OGDIr = "teski_skup/png"
RecivDir = "ZavrsniDatasets/extra_dataset/before_transplant/images"


OGDir_names = os.listdir(OGDIr)
RecivDir_names = os.listdir(RecivDir)

for i in RecivDir_names:
    OGfile = RoboToNormal(i)
    Cpfrom = OGDIr + "/" + OGfile
    Cptodel = RecivDir  + "/" +  i
    Cpto = RecivDir  + "/" +  JPGPNGconverter(i)
    com1 = f"cp {Cpfrom} {Cpto}"
    com2 = f"rm {Cptodel}"
    print(com1)
    print(com2)
    os.system(com1)
    os.system(com2)