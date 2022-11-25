
from functions import write_prompts, get_prompts
import time

clock=time.strftime("%b %d %Y, %H:%M:%S")
print(f"it is currently {clock}")
while True:
    user_prompt = input("Type add, edit, show, complete or exit")
    user_prompt = user_prompt.strip()

    # match user_prompt:
    if user_prompt.startswith("add"):
        art_prompt = user_prompt[4:] + "\n"
        if len(user_prompt) == 3:
            print("Type in a prompt after add")
            continue

        APrompts = get_prompts("prompts.txt")

        APrompts.append(art_prompt.title())

        write_prompts(aprompts_arg=APrompts)

    elif user_prompt.startswith("show"):

        APrompts = get_prompts("prompts.txt")

        for count, item in enumerate(APrompts):
            item = item.strip("\n")
            print(f"{count + 1}-{item}")

    elif user_prompt.startswith("complete"):
        try:
            num = int(user_prompt[8:])

            APrompts = get_prompts("prompts.txt")

            index=num - 1

            completed_proj = APrompts[index]

            completed_proj=completed_proj.strip('\n')

            APrompts.pop(num-1)

            write_prompts(aprompts_arg=APrompts)

            print(f"You have completed {completed_proj}!!!")

        except IndexError:

            print("Fucking hell mate you dont have that many prompts to complete")

            continue

    elif user_prompt.startswith("exit"):
        break

    elif user_prompt.startswith("edit"):
        try:
            num = int(user_prompt[5:])

            APrompts = get_prompts("prompts.txt")

            old_prompt = APrompts[num-1]

            old_prompt = old_prompt.strip("\n")

            new_prompt = input(f"What will {old_prompt} change to?")

            APrompts[num-1] = new_prompt.title() + '\n'

            print(f"{old_prompt} has been changed to {new_prompt}!")

            write_prompts(aprompts_arg=APrompts)

        except ValueError:
            print(" Error, Use 'show' to see the prompt list and type the prompt number, not the title")
            user_prompt = input("Type add, edit, show, complete or exit")
            user_prompt = user_prompt.strip()
    else:
        print("Wrong input Chucklenuts!")


print('Well fuck off then')








