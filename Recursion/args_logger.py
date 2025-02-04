def args_logger(*args, **kwargs):
    for i, arg in enumerate(args,1):
        print(f"{i}. {arg}")
    for key in sorted(kwargs):
        print(f"* {key}: {kwargs[key]}")