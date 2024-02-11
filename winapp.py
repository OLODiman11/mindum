# https://www.youtube.com/watch?v=BdQOFOyHgfk&t=57s&ab_channel=NeuralNine

import pystray
import PIL.Image


class WinApp:
    def __init__(self, title: str, image: PIL.Image):
        self.title = title
        self.image = image
        self.__icon = pystray.Icon('Mindum', image, menu=pystray.Menu(
            # pystray.Menu.SEPARATOR,
            pystray.MenuItem('Exit', self.stop)
        ))

    def run(self):
        self.__icon.run()

    def stop(self):
        self.__icon.stop()
