import pandas as pd

df = pd.DataFrame(columns= ("Podloga", "Osigurac","Crta", "Tocka", "Tocka pozicija", "Gotovo", "Skip"))
g = 0
dicPodloga = {0:"Crna", 1:"Bijela"}
dicOsigurac = {0:"Svi", 1:"Bez Ljevog", 2:"Bez desnog"}
dicCrta = {0:'_', 1:'|', 2:'/', 3:'\\', 4:" "}
dicTocka = {0:'.', 1:':', 2:'⁂', 3:" "}
dicPozicija = {0:"Gore", 1:"Sredina", 2:"Dolje"}


for l in range(0,2):
    for k in range(0,3):
        for j in range(0,5):
            for h in range(0,4):
                if h != 3:    
                    for i in range(0,3):
                        df.loc[g, "Podloga"] = dicPodloga[l]
                        df.loc[g, "Osigurac"] = dicOsigurac[k]
                        df.loc[g, "Crta"] = dicCrta[j]
                        df.loc[g, "Tocka"] = dicTocka[h]
                        df.loc[g, "Tocka pozicija"] = dicPozicija[i]
                        df.loc[g, "Gotovo"] = 0
                        df.loc[g, "Skip"] = 0
                        g = g + 1
                else:
                    df.loc[g, "Podloga"] = dicPodloga[l]
                    df.loc[g, "Osigurac"] = dicOsigurac[k]
                    df.loc[g, "Crta"] = dicCrta[j]
                    df.loc[g, "Tocka"] = dicTocka[h]
                    df.loc[g, "Tocka pozicija"] = "Nema tocke"
                    df.loc[g, "Gotovo"] = 0
                    df.loc[g, "Skip"] = 0
                    g = g + 1
                    
df.to_csv("Plan_eksperimenta.csv")