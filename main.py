from flask import Flask
import subprocess
import time as t
import pyautogui


app = Flask(__name__)

@app.route('/open')
def index():
    openKassa()
    return 'Success'


def openKassa():
    p = subprocess.Popen(['start', 'cmd', '/k', 'copy con com5:'], shell=True)
    t.sleep(0.1)
    pyautogui.press('enter')
    t.sleep(0.5)
    pyautogui.press('alt')
    pyautogui.press('f4')
    pyautogui.press('alt')
    pyautogui.press('f4')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')