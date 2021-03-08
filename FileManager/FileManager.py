import os
import shutil
import json
import logging
import PySimpleGUI as sg
sg.theme("DarkAmber")

layout = [
    [sg.Text('Path'), sg.Text(size=(15, 1), key='OUT')],
    [sg.Input(key='-IN-')],
          [sg.CloseButton("OK"), sg.CloseButton("Cancel")]

]
window = sg.Window("FileManager",layout)
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    path = (values['-IN-'])

window.close()


global logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def log_intiate(path):
    logging.basicConfig(filename= os.path.join(path,"Filemanager.log"), format='%(asctime)s %(message)s',
                        filemode='w')
    # global logger
    # logger = logging.getLogger()
    # logger.setLevel(logging.INFO)

def log(info):
    logger.info(info)
    print(info)

def del_oldini(path):
    path = os.path.join(os.path.join(path, ".ini"))
    if os.path.exists(path) or os.path.exists(os.path.join(path,"FileManager.log")):
        log(f'Deleting ini from {path}')
        shutil.rmtree(path, ignore_errors=True)
        log(f'Deleted ini from {path}')
    else:
        pass

def filemanager():
    del_oldini(path)
    log_intiate(path)

    file_list = os.listdir(path)
    for i in file_list:
        log(f'{i} is a {os.path.splitext(i)[1]} folder')
        extension = os.path.splitext(i)[1]

        if extension == '.log' or '':
            log(f'No new file found')
            continue
        if os.path.exists(path + '/' + extension):
            shutil.move(path + '/' + i, path + '/' + extension + '/' + i)
        else:
            os.makedirs(path + '/' + extension)
            shutil.move(path + '/' + i, path + '/' + extension + '/' + i)

if __name__ =="__main__":
    filemanager()
    log("EveryThingRocks")