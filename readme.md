## Intro to FunnyAltF4

FunnyAltF4 is simple, it makes Alt F4 funny.  
How does it do this? It checks if you press Alt F4 and plays a sound.

## Setup

You must have Python installed (preferably `3.11.9`), along with the modules listed in `requirements.txt`. These can be installed all at once using:

```bash
pip install -r requirements.txt
```

### Configuring

First, you need an MP3 file (you can use the default MP3). This MP3 will be the sound effect that plays when you press Alt F4 (you cannot stop the sound unless you exit the program, so don't use something too long).  
Rename the MP3 to `Sound Effect.mp3` and put it into the `Audio Compiler` folder. Then, run `Convert Audio.py`.  
Open `Output.txt`, copy the contents, and replace the contents of the variable `mp3_base64` with the copied text (it should be formatted like `mp3_base64 = r"""COMPILED_AUDIO_FILE"""`).  
Optionally, you can change the tray icon image using the `icon_data_uri` variable (it should be formatted like `icon_data_uri = r"""PNG_DATA_URI"""`, but keep in mind Windows caps tray icon resolution to `256x256` pixels).

You can also compile it into an executable using PyInstaller.  
For this, you'll need to install PyInstaller with:

```bash
pip install pyinstaller
```

Next, run the command:

```bash
./compile.bat
```

If you want to use a custom icon, you can run the command:

```bash
pyinstaller FunnyAltF4.py --onefile --noconsole --icon="ICON_PATH"
```

Replace `ICON_PATH` with the full file path to your icon.  
Default icons are provided by [https://favicon.io](https://favicon.io).

## Why did I make this?

I have no idea. It was 3 AM, and I thought it was funny at the time.  
As little as I use Alt F4, I often forget it's running and when I do use it, i get a unexpected sound effect, which gives me a little giggle.  
Personally, I find the default sound effect funny, but if you want something else, feel free to use your own sound.