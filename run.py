import platform
import subprocess
import pyperclip
import os
def run():
    print('Paste mediafire link\n}')
    linkInput = input('')

    print('Paste output folder\n')
    outputInput = input('')

    argOutput = '-o ' + outputInput

    if platform == 'Windows':
        subprocess.run('C:\Windows\System32\cmd.exe', shell=True)
        pyperclip.copy('python mediafire.py' + ' '+ linkInput + ' ' + outputInput)
        os.chdir('C:\Users\atom\Documents\GitHub/mediafire-downloader')
        pyperclip.paste()
    else:
        exit


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        exit(0)
