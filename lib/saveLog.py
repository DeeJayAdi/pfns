from datetime import datetime
import os

def saveLog(data,path="./logs"):
    if os.path.exists('./logs')==False:
        os.mkdir(path)
    filename = datetime.now().strftime("%H-%M-%S-%d-%m-%Y")+"-log.json"
    file=open(path+"/"+filename,'w')
    file.write(str(data))
    file.close()