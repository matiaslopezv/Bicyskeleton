import json
try:
    with open("bicycle.json" , "r", encoding = "utf-8") as f:
        data = json.load(f)
    print(data)
except:
    print("El archivo JSON no se puede leer")