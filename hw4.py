def rep_char(c, n):
    return c * n

def draw_box_around_text(text_lines):
    max_length = max(len(line) for line in text_lines)
    print(rep_char('-', max_length + 4))
    for line in text_lines:
        print(f" {line}" + " " * (max_length - len(line)) + "")
    print(rep_char('-', max_length + 4))


name = input("Input his/her name: ")


message_lines = [
    f"Hello {name},",
    "Welcome to Seoul."
]


draw_box_around_text(message_lines)