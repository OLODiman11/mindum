import PIL.Image
from winapp import WinApp

if __name__ == '__main__':
    image = PIL.Image.open('icon.png')  # https://www.freepik.com/icon/brain_9667266
    app = WinApp('Mindum', image)
    app.run()
