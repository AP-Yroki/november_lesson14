import os

def print_reps(directory):
    content = (os.listdir(directory))

    print(f'Cодержимое директории {directory}: ')
    for item in content:
        print(item)

    item_path = os.path.join(directory, item)
    if os.path.isdir(item_path):
        print_reps(item_path)



print_reps('C:\\Users\\User\\Desktop\\Python Tests\\Python lessons\\venv')