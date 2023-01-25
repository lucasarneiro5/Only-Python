import os, shutil
import glob
import time
import datetime
from datetime import timedelta
from datetime import datetime as dt

class delete_oldFiles():
    def __init__(self):
        self.path = r"C:\Users\lavieira\Documents\Projects\ScriptsPython"
        self.hoje = dt.now()
        self.today = self.hoje.strftime("%Y-%m")
        self.all_folders = glob.glob("*")

    def get_folder(self, diretorio, file):
        self.folders = os.path.join(diretorio, file)
        if os.path.isdir(self.folders): # Se for uma pasta, ele retorna o caminho dela
            return self.folders      

    def start(self):
        # Get each file inside the folder = self.path
        for file in os.listdir(self.path):
            self.folder = self.get_folder(self.path, file)
            # Para cada item dentro de cada pasta encontrada no self.path
            for item in os.listdir(self.folder):
                if item.endswith(".json"): 
                    # Se for .json, delete o item            
                    os.remove(os.path.join(self.folders, item))
                elif item == 'SnapshotError':
                    # Se for uma pasta com esse nome, acessa ela e deleta arquivos
                    snap_shot = os.path.join(self.folder, item)
                    shutil.rmtree(snap_shot)

file = delete_oldFiles()
file.start()