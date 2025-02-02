def new_clipboard(initial_clipboard):
    copy_clip = initial_clipboard.copy()
    def copy_to_clipboard(key, value):
        copy_clip[key] = value
    def paste_from_clipboard(key):
        return copy_clip.get(key,"")
    return copy_to_clipboard, paste_from_clipboard
