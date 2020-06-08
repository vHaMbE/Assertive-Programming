
code = input("please enter your moss code here")


def decode(sentance):
    scode = ""
    if sentance == "/":
        scode += " "
        count += 1
    elif sentance == ".-":
        scode += "a"
    elif sentance == "-...":
        scode += "b" 
    return(scode)

temp = ""
full = ""

for ch in code:
    if ch == ".":
        temp += "."
    elif ch == "-":
        temp += "-"
    elif ch == "/":
        counter += 1
        temp += "/"
    elif ch == " ":
        count2 += 1
        full += decode(temp)
        temp = ""
    else:
        print("error")
full += decode(temp)
assert full == counter
assert count2 == len(full)
print(full)

