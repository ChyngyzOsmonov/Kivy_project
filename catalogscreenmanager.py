from kivy.uix.screenmanager import ScreenManager


class CatalogScreenManager(ScreenManager):
    def change_screen(self, new_screen):
        self.current = new_screen