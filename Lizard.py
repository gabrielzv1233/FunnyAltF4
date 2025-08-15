# pyinstaller Lizard.py --onefile --noconsole --add-data "lizard.gif;." --add-data "lizard.mp3;."
from pystray import Icon, MenuItem, Menu
from win11toast import toast_async
from PIL import Image
import win32com.client
import threading
import keyboard
import argparse
import asyncio
import psutil
import pygame
import os
import sys

parser = argparse.ArgumentParser()
current_process = psutil.Process(os.getpid())
parser.add_argument("--isstartup", type=bool, help="adds a delay before initializing, allows windows to be fully ready before starting, causing keybind not to work", required=False)
args = parser.parse_args()

def resource_path(name: str) -> str:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, name)
    return os.path.join(os.path.dirname(__file__), name)

MuteSound = False

if args.isstartup is True:
    import time
    print("Program running as startup task, waiting 15 seconds to initialize")
    time.sleep(15)

async def starttoast():
    asyncio.create_task(toast_async('Lizard is running!', 'Find app in tray to quit'))
    
async def startuptoast(enabledstartup: bool):
    if enabledstartup == True:
        asyncio.create_task(toast_async('Lizard', 'Lizard will now start automatically at login'))
    else:
        asyncio.create_task(toast_async('Lizard', 'Lizard will no longer start automatically at login'))

startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
script_path = sys.argv[0]
shortcut_name = "Lizard.lnk"
shortcut_path = os.path.join(startup_folder, shortcut_name)

def create_startup_shortcut():
    print("Creating startup shortcut")
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = script_path
    shortcut.Arguments = '--isstartup=True'
    shortcut.WorkingDirectory = os.path.dirname(script_path)
    shortcut.IconLocation = script_path
    shortcut.save()

def toggle_startup(icon, item):
    if os.path.exists(shortcut_path):
        print("removing startup shortcut")
        asyncio.run(startuptoast(False))
        os.remove(shortcut_path)
    else:
        asyncio.run(startuptoast(True))
        create_startup_shortcut()
    icon.update_menu()

def create_image():
    img_path = resource_path("lizard.gif")
    image = Image.open(img_path)
    return image

def play_sound():
    global MuteSound
    if not MuteSound:
        pygame.mixer.music.play()
        
def toggle_mute(icon, item):
    global MuteSound
    MuteSound = not MuteSound
    icon.update_menu()

def quit_app():
    print("Exiting task")
    pygame.mixer.music.stop()
    pygame.quit()
    current_process.kill()

def setup_tray():
    print("Setting up windows tray icon")
    menu = Menu(
        MenuItem('Play Sound (Space)', action=lambda icon, item: play_sound()),    
        MenuItem('Toggle Startup', toggle_startup, checked=lambda item: os.path.exists(shortcut_path)),
        MenuItem('Mute Sound', toggle_mute, checked=lambda item: MuteSound),
        MenuItem('Quit', action=quit_app)
    )
    icon = Icon("tray_icon", create_image(), "Lizard", menu)
    icon.run()

print("initializing pygame audio")
pygame.mixer.init()

pygame.mixer.music.load(resource_path("lizard.mp3"))

print("Creating hotkey")
keyboard.add_hotkey('Space', play_sound)

if (__name__ == "__main__"):
    asyncio.run(starttoast())
    tray_thread = threading.Thread(target=setup_tray)
    tray_thread.start()
    print("Lizard is ready! Press Alt+f4 to play sound.")