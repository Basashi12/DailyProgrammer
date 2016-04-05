# Challenge #20 Difficult

import ctypes, time

def reminder():
    while True:
        time.sleep(7200)
        ctypes.windll.user32.MessageBoxW(0, 'Stop procrastinating!', 'Be Productive!', 0)
        # Python 2 would have used MessageBoxA
