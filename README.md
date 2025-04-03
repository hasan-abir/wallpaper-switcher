# Wallpaper Switcher (Windows)

It switches wallpaper randomly from your own collection of pictures.

NOTE: Windows defender prompt will come up only because this is an unsigned app. No need to panic. Either way, the code is all here if you are skeptical about it.

## App guide

- Download `Wallpaper.zip` from the latest [release](https://github.com/hasan-abir/wallpaper-switcher/releases/tag/v1.0.0)
- Extract it as usual, and run `Wallpaper.exe` to see it work
- It choose from one of the pictures in the `Wallpapers` folder; so to add your own pictures to the mix, copy them to this folder
- If you accidentally delete the folder, you can just run the .exe again for it generate the folder (note: without the `_internal` folder the exe won't work)
- You can schedule a task to run this exe, for example, every morning to get a new picture for the day.

## Developer guide

### Installation

Use this guide to create a python environment ([venv](https://docs.python.org/3/library/venv.html))

Then, install all the packages

```bash
pip install -r requirements.txt
```

### Running

To generate a .exe file in dist

```bash
pyinstaller --name WallpaperSwitcher --icon "wallpaper-switcher.ico" src/main.py
```

To run the actual script

```bash
py src/main.py
```

To test the script

```bash
py -m unittest tests/test_main.py
```
