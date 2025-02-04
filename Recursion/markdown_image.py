def create_markdown_image(alt_text):
    def inner(url):
        escaped_url = url.replace('(', '%28').replace(')', '%29')

        def innermost(title = None):
            markdown_image = f"![{alt_text}]({escaped_url})"
            if title:
                markdown_image = markdown_image.rstrip(')') + f' "{title}")'
            return markdown_image

        return innermost

    return inner
