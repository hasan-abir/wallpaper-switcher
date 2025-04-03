# Wallpaper Switcher (Windows)

It switches wallpaper randomly from your own collection of pictures.

## App guide

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
