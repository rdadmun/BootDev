def replacer(old, new):
    def replace(decorated_func):
        def wrapper(text):
            modified_text = text.replace(old, new)
            return decorated_func(modified_text)
        return wrapper
    return replace
        
@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"