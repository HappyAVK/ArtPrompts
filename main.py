import functions
import PySimpleGUI as GUI

label = GUI.Text("Type in an Art Prompt")
input1 = GUI.InputText(tooltip="Enter a Prompt!")
add_button = GUI.Button("Add")
W = GUI.Window('Art Prompts App',layout=[[label], [input1], [add_button]])

W.read()
W.close()
