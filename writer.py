class Writer:
    def append(content, destination):
        with open(destination, 'a') as file:
            file.writelines(content)