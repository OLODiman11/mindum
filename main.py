import PIL.Image
from winapp import WinApp
from hotkeylistener import HotKeyListener, capture_hotkey_combination


listener: HotKeyListener
app: WinApp


def on_hotkey_pressed():
    print('Hello!')


def change_hotkey_combination():
    global listener, app
    old_comb = listener.combination
    listener.stop()
    new_comb = capture_hotkey_combination()
    listener = HotKeyListener(new_comb, on_hotkey_pressed)
    listener.start()
    app.remove_menu_item(old_comb)
    app.add_menu_item(new_comb, change_hotkey_combination)


if __name__ == '__main__':
    listener = HotKeyListener('<alt_gr>+m', on_hotkey_pressed)
    listener.start()

    image = PIL.Image.open('icon.png')  # https://www.freepik.com/icon/brain_9667266
    app = WinApp('Mindum', image)
    app.add_menu_item('<alt_gr>+m', change_hotkey_combination)
    app.run()
    listener.stop()
    listener.join()
