import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from catalogscreenmanager import CatalogScreenManager
from kivy.properties import StringProperty
from kivymd.uix.list import ILeftBody, OneLineAvatarListItem
from screen1 import Screen1
from screen2 import Screen2
from screen3 import Screen3


class CatalogNavDrawer(MDNavigationDrawer):
    pass

class NavigationDrawerIconButton(OneLineAvatarListItem):
    source = StringProperty()

class MainApp(MDApp):
    pass


if __name__ == "__main__":
    MainApp().run()