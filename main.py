import functions
import PySimpleGUI as GUI

label = GUI.Text("Type in an Art Prompt")
input1 = GUI.InputText(tooltip="Enter a Prompt!",key="n_prompt")
add_button = GUI.Button("Add")
edit_button =GUI.Button("Edit")
list_box = GUI.Listbox(values=functions.get_prompts(), key="prompts",
                       enable_events=True, size=[45, 10])


W = GUI.Window('Art Prompts App',
               layout=[[label, edit_button], [input1], [add_button],[list_box]],
               font=('Helvetica', 20))
while True:
    event, value = W.read()
    print(event)
    print(value)
    match event:
        case "Add":
            APrompts = functions.get_prompts()
            new_prompt = value["n_prompt"] + '\n'
            APrompts.append(new_prompt)
            functions.write_prompts(APrompts)
            W['prompts'].update(values=APrompts)
        case "Edit":
            prompt_edit = value["prompts"][0]
            new_prompt = value["n_prompt"] + '\n'

            APrompts = functions.get_prompts()
            index = APrompts.index(prompt_edit)
            APrompts[index] = new_prompt
            functions.write_prompts(APrompts)
            W['prompts'].update(values=APrompts)
        case "prompts":
            W['n_prompt'].update(value=value["prompts"][0])

        case GUI.WIN_CLOSED:
            break

W.close()
