def updated_output_text(output_text, string):
    if output_text != "":
        return output_text + string
    else:
        return string

output_text = ""
available_formatters = ["plain", "bold", "italic", "inline-code", "link",
                        "header", "new-line", "ordered-list", "unordered-list"]
while True:
    formatter = input("Choose a formatter: ")
    if formatter == "!help":
        print("Available formatters: ", end="")
        print(*available_formatters)
        print("Special commands: !help !done")
    elif formatter == "!done":
        with open("output.md", "w") as foutput:
            foutput.writelines(output_text)
        break
    elif formatter in available_formatters:
        if formatter == "header":
            while True:
                level = int(input("Level: "))
                if level < 1 or level > 6:
                    print("The level should be within the range of 1 to 6")
                    continue
                break
            text = input("Text: ")
            output_string = "#" * level + " " + text
            output_text = updated_output_text(output_text, output_string + "\n")
        elif formatter == "plain":
            output_string = input("Text: ")
            output_text = updated_output_text(output_text, output_string)
        elif formatter == "new-line":
            output_text = updated_output_text(output_text, "\n")
        elif formatter == "bold":
            text = input("Text: ")
            output_string = f"**{text}**"
            output_text = updated_output_text(output_text, output_string)
        elif formatter == "italic":
            text = input("Text: ")
            output_string = f"*{text}*"
            output_text = updated_output_text(output_text, output_string)
        elif formatter == "inline-code":
            text = input("Text: ")
            output_string = f"`{text}`"
            output_text = updated_output_text(output_text, output_string)
        elif formatter == "link":
            label = input("Label: ")
            url = input("URL: ")
            output_string = f"[{label}]({url})"
            output_text = updated_output_text(output_text, output_string)
        elif formatter in ("ordered-list",  "unordered-list"):
            while True:
                num_of_rows = int(input("Number of rows: "))
                if num_of_rows <= 0:
                    print("The number of rows should be greater than zero")
                    continue
                break

            for i in range(num_of_rows):
                row_string = input(f"Row #{i + 1}: ")
                if formatter == "ordered-list":
                    num_of_row = f"{i + 1}."
                else:
                    num_of_row = "*"
                output_string = f"{num_of_row} {row_string}"
                if i > 0:
                    output_text += "\n"
                output_text += output_string
            output_text += "\n"

        print(output_text)
    else:
        print("Unknown formatting type or command")