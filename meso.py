import winsound as ws
import time

def beepsound():
    freq = 700
    dur = 1000
    ws.Beep(freq, dur)

while True:
    time.sleep(110)
    beepsound()

