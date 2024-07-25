from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import os

class firstpage(Screen):
    pass    

class karPlanOut(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kivy_folder = ".\\kivy\\"

    def build(self):
        list_of_rpaths = os.listdir(self.kivy_folder)
        list_of_paths = [os.path.join(self.kivy_folder, path) for path in list_of_rpaths]

        for path in list_of_paths:
            Builder.load_file(path)

        sm = ScreenManager()
        sm.add_widget(firstpage())

        return sm

if __name__ == "__main__":
    karPlanOut().run()