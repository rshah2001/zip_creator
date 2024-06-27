import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress")
input1 = sg.Input()

# FileBrowse will allow users to select file from the system and that is the only use of this
button1 = sg.FilesBrowse("Choose", key='files')


label2 = sg.Text("Select Destination Folder")
input2 = sg.Input()

# Folder browse will let users choose the folder
button2 = sg.FolderBrowse("Choose", key='folder')

compress_button = sg.Button("Compress")

window = sg.Window("file compressor", layout=[[label1, input1, button1],
                                              [label2, input2, button2],
                                              [compress_button]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(";")
    folder = values['folder']
    make_archive(filepaths, folder)


window.close()
