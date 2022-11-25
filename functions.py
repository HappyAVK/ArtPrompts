def get_prompts(filepath="promts.txt"):
    """HNNNNNG AQUA CUTE CUTE CUTE"""
    with open(filepath, "r") as file:
        local_prompts = file.readlines()
    return local_prompts


def write_prompts(aprompts_arg, filepath="promts.txt"):
    with open(filepath, "w") as file:
        file.writelines(aprompts_arg)
