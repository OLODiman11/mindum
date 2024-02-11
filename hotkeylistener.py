from pynput import keyboard
from typing import Callable


class HotKeyListener:
    def __init__(self, combination: str, callback: Callable):
        self.combination = combination
        self.callback = callback
        self.hotkey = keyboard.HotKey(keyboard.HotKey.parse(combination), self.on_activate)
        self.__listener = keyboard.Listener(
            on_press=self.for_canonical(self.hotkey.press),
            on_release=self.for_canonical(self.hotkey.release))

    def on_activate(self):
        self.callback()

    def for_canonical(self, func):
        return lambda k: func(self.__listener.canonical(k))

    def start(self):
        self.__listener.start()

    def join(self):
        self.__listener.join()

    def stop(self):
        self.__listener.stop()


class HotKeyCapture:
    def __init__(self):
        self.combination = []
        self.__keys_pressed = []
        self.__listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)

    def start(self):
        self.__listener.start()

    def join(self):
        self.__listener.join()

    def stop(self):
        self.__listener.stop()

    def on_press(self, k: keyboard.KeyCode):
        k = self.__listener.canonical(k)
        try:
            self.combination.append(str(k.char))
        except AttributeError:
            self.combination.append(f'<{str(k)[4:]}>')
        self.__keys_pressed.append(k)

    def on_release(self, k):
        try:
            self.__keys_pressed.remove(k)
            if len(self.__keys_pressed) == 0:
                self.combination = '+'.join(self.combination)
                self.__listener.stop()
        except ValueError:
            pass


def capture_hotkey_combination() -> str:
    hkc = HotKeyCapture()
    hkc.start()
    hkc.join()
    return hkc.combination
