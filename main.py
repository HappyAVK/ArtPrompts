import functions
import PySimpleGUI as GUI

label = GUI.Text("Type in an Art Prompt")
input1 = GUI.InputText(tooltip="Enter a Prompt!",key="prompt")
add_button = GUI.Button("Add")
W = GUI.Window('Art Prompts App',
               layout=[[label], [input1], [add_button]],
               font=('Helvetica', 20))
while True:
    event, value = W.read()
    print(event)
    print(value)
    match event:
        case "Add":
            APrompts = functions.get_prompts()
            new_prompt = value["prompt"] +'\n'
            APrompts.append(new_prompt)
            functions.write_prompts(APrompts)
        case GUI.WIN_CLOSED:
            break

W.close()
