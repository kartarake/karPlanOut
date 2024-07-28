from dearpygui import dearpygui as pygui
import json, os, math

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

    def calc_for_x_centre(self, item_width:int|tuple|list, gap:int=0) -> int|tuple|list:
        if isinstance(item_width, tuple):
            sum_of_width = sum(item_width)
            n = len(item_width)
            free_space = self.appwidth - sum_of_width - n*gap
            half_space = math.ceil(free_space/2)
            x_pos = [half_space]
            first = True
            for width in item_width:
                if first: first = False; prev_width = width; continue
                x_pos.append(half_space + prev_width + gap)
                prev_width = prev_width + width + gap
        else:
            free_space = self.appwidth - item_width
            x_pos = math.ceil(free_space/2)
        return x_pos
    
    def calc_for_y_centre(self, item_height:int|tuple|list, gap:int=0) -> int|tuple|list:
        if isinstance(item_height, tuple):
            sum_of_height = sum(item_height)
            n = len(item_height)
            free_space = self.appheight - sum_of_height - n*gap
            half_space = math.ceil(free_space/2)
            y_pos = [half_space]
            first = True
            for width in item_height:
                if first: first = False; prev_width = width; continue
                y_pos.append(half_space + prev_width + gap)
                prev_width = prev_width + width + gap
        else:
            free_space = self.appwidth - item_height
            y_pos = math.ceil(free_space/2)
        return y_pos

    def page_firstpage(self) -> None:
        with pygui.window(tag=self.apptitle):
            signin_button = pygui.add_button(
                label="Sign in",
                width=600,
                height=50,
                tag="signin_button"
            )
            pygui.bind_item_font(signin_button, self.fontpack["firstpage_buttons"])
            pos = (self.calc_for_x_centre(600), self.calc_for_y_centre((50, 50), gap=10)[0])
            pygui.set_item_pos("signin_button", pos)

            guest_button = pygui.add_button(
                label="Look around as a guest",
                width=600,
                height=50,
                tag="guest_button"
            )
            pygui.bind_item_font(guest_button, self.fontpack["firstpage_buttons"])
            pos = (self.calc_for_x_centre(600), self.calc_for_y_centre((50, 50), gap=10)[1])
            pygui.set_item_pos("guest_button", pos)

if __name__ == "__main__":
    app()