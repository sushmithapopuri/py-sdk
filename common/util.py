

def write_output(output:str, file_name:str = None) -> None: 
    if not file_name:
        file_name = "output.json"
    print(file_name, output)