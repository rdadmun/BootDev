def new_resizer(max_width, max_height):
    def inner(min_width = 0, min_height = 0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")
        def innermost(width, height):
            new_width = max(min_width, min(width, max_width))
            new_height = max(min_height, min(height, max_height))
            return new_width, new_height
        return innermost
    return inner
