
import subprocess , os
import PySimpleGUI as sg
from sys import platform


font_file = "arial.ttf"
out_put_folder = ""
out_put_file = "arial.json"
font_quality = 40
pixel_perfect = True
cmd = ""

def generate_comand():
    pixel_perfect_num = 0
    if pixel_perfect:
        pixel_perfect_num = 1

    output_file_and_folder = ""
    if out_put_folder == "":
        output_file_and_folder = out_put_file
    else:
        output_file_and_folder = font_file + "/" + out_put_file

    

    cmd = "importador_fontes.exe" + " \"" + font_file + "\" \"" + output_file_and_folder + "\"  \"" + str(font_quality) + "\" \"" + str(pixel_perfect_num) + "\""
    print(cmd)
    os.system(cmd)
    


    


sg.theme('DarkBlue16')
UI = [
    

    [sg.Text("font file")],
    [sg.FileBrowse(key='font file')],

    [sg.Text("out put folder")],
    [sg.FolderBrowse(key="out put folder")],

    [sg.Text("out put file name")],
    [sg.Input(default_text="font.json",key="out put file name")],

    [sg.Text("font quality")],
    [sg.Input(default_text="40",key="font quality")],

    [sg.Text("pixel perfect")],
    [sg.Checkbox("",default=True,key="pixel perfect")],

    [sg.Button("generate comand"),sg.Button("EXIT")],
    [sg.Text("",key="cmd")],
    
    ] 

window = sg.Window('font reader ui', UI,size=(300,600))


    

while True:
    event, values = window.read()
    if event in (None, "generate comand"):
        font_file = values["font file"]
        out_put_folder = values["out put folder"]
        out_put_file = values["out put file name"]
        font_quality = int(values["font quality"])
        pixel_perfect = values["pixel perfect"]
        generate_comand()
    if event in (None, 'EXIT'):
        break
    
    

window.close()






