import functions
import PySimpleGUI as GUI

label=GUI.Text("Type in an Art Prompt")
input= GUI.InputText(tooltip="Enter a Prompt!")
add_button = GUI.Button("Add")
W = GUI.Window('Art Prompts App',layout=[[label], [input], [add_button]])

W.read()
W.close()
