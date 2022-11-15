import pygetwindow as gw
import os
import time
import subprocess


class Checking_Robot:
    def __init__(self):
        self.elements = gw.getAllTitles()

    #Check on list
    def check_process(self):
        for i in self.elements:
            if i == 'Calculadora':
                return True
            else:
                pass

    def kill_process(self):
        self.killthis = 'Calculator.exe'
        #os.system("taskkill /im Calculator.exe")
        subprocess.call("TASKKILL /F /IM Calculator.exe", shell=True)

    def start_process(self):
        subprocess.check_call(r"C:\Users\lucas\Downloads\calc.exe", stdin=None, stdout=None, stderr=None, shell=False)

    def start(self):
        self.kill_process()
        time.sleep(5)
        ini = time.time()
        while True:
            self.elements = gw.getAllTitles()
            #print(self.elements)
            time.sleep(1)
            self.check_process()            
            print('\n')

             # Parar loop em caso de detectar a janela ou após 10 min avisar que nao iniciou.
            fim = time.time()
            if self.check_process() == True:
                print('Processo Iniciado!\n')
                break
            elif fim - ini > 11:
                print('Processo nao iniciado, iniciando automaticamente...\n')
                self.start_process()
                break          
            else:
                print('\nTempo Gasto: ', fim - ini)
                pass

check = Checking_Robot()
check.start()






