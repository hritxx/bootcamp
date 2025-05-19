def snakecase(lines):
    for _, line in lines:
        snake = line.replace(" ", "_").lower()
        yield ("end", snake)