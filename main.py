from dearpygui import dearpygui as pygui

class app:
    def __init__(self) -> None:
        self.apptitle = "karPlanOut"
        
        self.appwidth = 1930
        self.appheight = 1040

        self.init_pygui()
        
        self.page_firstpage()

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

    def page_firstpage(self) -> None:
        with pygui.window(tag=self.apptitle):
            pygui.add_button(label="Sign in")
            pygui.add_button(label="Look around as a guest")

if __name__ == "__main__":
    app()