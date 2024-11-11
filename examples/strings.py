multiline_str = """del int
int(6.342)
Out[67]: 6"""
print(multiline_str)

text = "He said \"That\'s it\""
print(text)

special_characters = "\n \t \\ \u2212"
print(special_characters)

# f-strings
total_minutes = 123
hour = total_minutes // 60
minute = total_minutes % 60

# Without f-strings, variables have to be converted to str
message = "hour is: " + str(hour) + ", minute is: " + str(minute)

message1 = f"hour is: {hour}, minute is: {minute}"
print(message1)

message2 = f"hour is: {total_minutes // 60}, minute is: {total_minutes % 60}"
print(message2)

message3 = f"Time is {hour:02}:{minute:02}"
print(message3)

print(f"Total minutes as float: {total_minutes:.2f}")