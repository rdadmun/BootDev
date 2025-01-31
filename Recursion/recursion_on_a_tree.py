def list_files(parent_directory, current_filepath=""):
    filepath_lst = []
    for key in parent_directory:
        new_path = current_filepath + "/" + key
        if isinstance(parent_directory[key], dict):
            filepath_lst.extend(list_files(parent_directory[key], new_path))
        else:
            filepath_lst.append(new_path)
    return filepath_lst
