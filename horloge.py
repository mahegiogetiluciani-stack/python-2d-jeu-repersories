from datetime import datetime
import time

running = True

def horloge():
    while running:
        a = datetime.now().strftime("%H:%M:%S")
        print("Heure actuelle :", a)
        time.sleep(1.0)
        horloge()

horloge()
            
