# https://www.youtube.com/watch?v=BdQOFOyHgfk&t=57s&ab_channel=NeuralNine

import pystray
import PIL.Image
from typing import Callable


class WinApp:
    def __init__(self, title: str, image: PIL.Image):
        self.title = title
        self.image = image
        self.__icon = pystray.Icon('Mindum', image, menu=pystray.Menu(
            pystray.Menu.SEPARATOR,
            pystray.MenuItem('Exit', self.stop)
        ))

    def add_menu_item(self, text: str, action: Callable):
        items = [pystray.MenuItem(text, action)] + list(self.__icon.menu.items)
        self.__icon.menu = pystray.Menu(*items)

    def remove_menu_item(self, text: str):
        items = list(self.__icon.menu.items)
        for i, item in enumerate(items):
            if item.text == text:
                self.__icon.menu = pystray.Menu(*(items[:i]+items[i+1:]))

    def run(self):
        self.__icon.run()

    def stop(self):
        self.__icon.stop()
