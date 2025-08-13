def string_to_list_of_lists(data):
    
    lines = data.strip().split("\n")

    first_line = lines[0]

    other_lines = lines[1:]

    result = []
    for i in range(0, len(other_lines), 2):
        group = [first_line, other_lines[i]]
        if i + 1 < len(other_lines):
            group.append(other_lines[i + 1])
        result.append(group)

    return result


input_str = """first line
second line
third line
fourth line
fifth line"""

print(string_to_list_of_lists(input_str))