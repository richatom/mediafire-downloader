import platform
import subprocess
import pyperclip
import os
import time
def run():
    print('Paste mediafire link:')
    linkInput = input('')

    print('Paste output folder:')
    outputInput = input('')

    argOutput = '-o ' + outputInput

    subprocess.run('C:\\Windows\\System32\\cmd.exe', shell=True)
    os.chdir('Documents')
    time.sleep(0.2)
    pyperclip.copy('python mediafire.py' + ' '+ linkInput + ' ' + argOutput)
    pyperclip.paste()


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        exit(0)
