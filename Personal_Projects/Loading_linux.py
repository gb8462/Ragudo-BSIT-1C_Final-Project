import os
import time

def clean():
    os.system('clear')

def load():
    for i in range(2):
        print("Loading", end='', flush=True)
        time.sleep(0.3)
        
        clean()

        print("Loading .", end='', flush=True)
        time.sleep(0.3)
        
        clean()

        print("Loading ..", end='', flush=True)
        time.sleep(0.3)
        
        clean()

        print("Loading ...", end='', flush=True)
        time.sleep(0.3)
        
        clean()

    print("Loading ...", end='', flush=True)
    time.sleep(0.3)
    clean()

def exiting():
    for i in range(2):
        print("Exiting", end='', flush=True)
        time.sleep(0.3)
        
        clean()

        print("Exiting .", end='', flush=True)
        time.sleep(0.3)
        
        clean()

        print("Exiting ..", end='', flush=True)
        time.sleep(0.3)
        
        clean()

        print("Exiting ...", end='', flush=True)
        time.sleep(0.3)
        
        clean()

    print("Exiting ...", end='', flush=True)
    time.sleep(0.3)
    clean()