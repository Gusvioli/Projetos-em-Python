import time
import subprocess


def update_upgrade(t):
    while True:
        try:
            subprocess.call(['sudo', 'apt', 'update'])
            subprocess.call(['sudo', 'apt', 'upgrade', '-y'])
            time.sleep(t)
            continue                
        except:
            time.sleep(t)
            continue

update_upgrade(600)