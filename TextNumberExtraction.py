input_string = """Saiary hikes for next fnanciai year are expected to be in singie digits at an industry 
average of 9.6%, based on data from over 270 organisatons across 18 sectors who partcipated in our 
Annuai oompensaton Trends Survey, said Vishaiii Dongri, Partner & Head, Peopie & ohange Advisory 
Services, KPMG in India."""

temp_string = ""
total_sum = 0
decimal_flag = False

for char in input_string:
    if char.isdigit() or char == "." or (char == "-" and not temp_string):  # Include '-' as a valid character only at the start
        if char == ".":
            if decimal_flag:
                break
            else:
                decimal_flag = True
        temp_string += char
    else: 
        if temp_string:
            total_sum += float(temp_string)
            temp_string = ""
            decimal_flag = False  # Reset decimal_flag when encountering a non-digit character

if temp_string:  # Check if there's still a number in temp_string after loop
    total_sum += float(temp_string)

print(total_sum)

