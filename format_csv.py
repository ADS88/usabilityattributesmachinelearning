with open("training_data.csv") as training_data:
    lines = training_data.readlines()

formatted_lines = []
for line in lines:
    if line.strip() != '"':
        line = line.replace('"', "")
        line = line.replace(",", '"', 1)
        formatted_lines.append(line)

with open("formatted_data.csv", "w") as formatted_data:
    formatted_data.writelines(formatted_lines)