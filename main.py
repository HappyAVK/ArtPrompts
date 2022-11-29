import functions
import PySimpleGUI as GUI
import time
GUI.theme("DarkPurple4")
clock = GUI.Text(key="clock")
label = GUI.Text("Type in an Art Prompt")
input1 = GUI.InputText(tooltip="Enter a Prompt!", key="n_prompt")
add_button = GUI.Button("Add")
edit_button = GUI.Button("Edit")
complete_button = GUI.Button("Complete")
list_box = GUI.Listbox(values=functions.get_prompts(), key="prompts",
                       enable_events=True, size=(45, 10))
exit_button = GUI.Button("Exit")

W = GUI.Window('Art Prompts App',
               layout=[[label, edit_button, complete_button],
                       [input1],
                       [add_button],
                       [list_box],
                       [exit_button, clock]],
               font=('Helvetica', 20))
while True:
    event, value = W.read(timeout=200)
    W['clock'].update(value=time.strftime("%b %d, %Y, %H:%M:%S"))
    #print(event)
    #print(value)
    match event:
        case "Add":
            APrompts = functions.get_prompts()
            new_prompt = value["n_prompt"].strip("\n") + '\n'
            APrompts.append(new_prompt)
            functions.write_prompts(APrompts)
            W['prompts'].update(values=APrompts)
        case "Edit":
            try:
                prompt_edit = value["prompts"][0]
                new_prompt = value["n_prompt"] + '\n'

                APrompts = functions.get_prompts()
                index = APrompts.index(prompt_edit)
                APrompts[index] = new_prompt
                functions.write_prompts(APrompts)
                W['prompts'].update(values=APrompts)
            except IndexError:
                GUI.popup("Select an Item Numbnuts!", font=10)
        case "prompts":
            W['n_prompt'].update(value=value["prompts"][0])

        case "Complete":
            try:
                to_complete_prompt = value["prompts"][0]
                APrompts = functions.get_prompts()
                APrompts.remove(to_complete_prompt)
                functions.write_prompts(APrompts)
                W['prompts'].update(values=APrompts)
                W["n_prompt"].update(value="")
            except IndexError:
                GUI.popup("You haven't selected anything to complete, Idiot", font=10)

        case GUI.WIN_CLOSED:
            break
        case "Exit":
            break

W.close()
