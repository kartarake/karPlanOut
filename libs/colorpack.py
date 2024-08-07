import json
import os

empty_colorpack = {
    "header":"This is a colorpack file for karPlanOut application.",
    "version":"v0",
    "primary":None,
    "primary_bg":None,
    "secondary":None,
    "text":None,
    "accent1":None,
    "accent2":None,
    "accent3":None,
}

def create_empty_colorpack(name:str) -> str:
    path = f".\\colorpacks\\{name}.json"
    os.makedirs(path, exist_ok=True)
    with open(path, "w") as f:
        json.dump(empty_colorpack, f, indent=3)
    return path

def load_colorpack(name:str) -> dict:
    path = f".\\colorpacks\\{name}.json"
    with open(path, "r") as f:
        return json.load(f)

def convert_hex_to_rgb(hexcode:str) -> None:
    if hexcode.startswith("#"):
        hexcode = hexcode[1:]
    if not len(hexcode) == 6:
        return IndexError("Hexcode is of invalid length.")
    
    red = int(hexcode[:2], 16)
    green = int(hexcode[2:4], 16)
    blue = int(hexcode[4:], 16)
    return (red, green, blue)