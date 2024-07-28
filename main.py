from dearpygui import dearpygui as pygui
import json, os

import libs.colorpack_handle

class app:
    def __init__(self) -> None:
        # Variable Dashboard
        self.apptitle = "karPlanOut" # Title of the window
        
        self.appwidth = 1930 # Window's width
        self.appheight = 1040 # Window's height

        if os.path.exists(".\\settings.json"): #loading settings
            self.load_settings()
        else:
            self.create_settings()

        self.colorpack_load() # loading color palatte

        # Initializing and setting up stuff!
        self.init_pygui()
        self.font_load()
        
        # App pages
        self.page_firstpage()

        # Start the pygui!
        self.start_pygui()

    def init_pygui(self) -> None:
        pygui.create_context()
        pygui.create_viewport(
            title=self.apptitle,
            height=self.appheight,
            width=self.appwidth,
            x_pos=0,
            y_pos=0,
        )
        pygui.setup_dearpygui()

    def start_pygui(self) -> None:
        pygui.show_viewport()
        pygui.set_primary_window(self.apptitle, True)
        pygui.start_dearpygui()
        pygui.destroy_context()

    def create_settings(self) -> None:
        settings = {
            "colorpack" : "forest",
        }
        path = ".\\settings.json"
        with open(path, "w") as f:
            json.dump(settings, f, indent=3)
        self.settings = settings

    def load_settings(self) -> None:
        path = ".\\settings.json"
        with open(path, "r") as f:
            self.settings =  json.load(f)

    def font_load(self) -> None:
        self.fontpack = {}
        with pygui.font_registry():
            # General use fonts
            self.fontpack["heading"] = pygui.add_font(r"assets\fonts\Montserrat\static\Montserrat-ExtraBold.ttf", 24)
            self.fontpack["body"] = pygui.add_font(r"assets\fonts\Montserrat\static\Montserrat-Light.ttf", 13)
            
            # Specific use fonts
            self.fontpack["firstpage_buttons"] = pygui.add_font(r"assets\fonts\Jura\static\Jura-Bold.ttf", 16)

    def colorpack_load(self) -> None:
        self.colorpack_name = self.settings["colorpack"]
        self.colorpack = libs.colorpack_handle.load_colorpack(self.colorpack_name)

    def page_firstpage(self) -> None:
        with pygui.window(tag=self.apptitle):
            signin_button = pygui.add_button(
                label="Sign in",
                width=600,
                height=50
            )
            pygui.bind_item_font(signin_button, self.fontpack["firstpage_buttons"])

            guest_button = pygui.add_button(
                label="Look around as a guest",
                width=600,
                height=50,
            )
            pygui.bind_item_font(guest_button, self.fontpack["firstpage_buttons"])

if __name__ == "__main__":
    app()