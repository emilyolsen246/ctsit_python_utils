import os


def prevent_overwrite(filename):
    if not os.path.exists(filename):
        return filename

    name, extension = os.path.splitext(filename)

    count = 1

    new_filename = f'{name} ({count}){extension}'
    while os.path.exists(new_filename):
        count += 1
        new_filename = f'{name} ({count}){extension}'

    return new_filename
