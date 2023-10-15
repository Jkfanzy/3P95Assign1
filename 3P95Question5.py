def processString(input_str):
    output_str = ""
    for char in input_str:
        if char.isupper():
            output_str += char.lower()
        elif char.isnumeric():
            output_str += char * 2 
        else:
            output_str += char.upper()
    return output_str



def deltaDebug(input_str):
    print(input_str)
    n = len(input_str)
    if n == 1:
        lower_input = input_str.lower()
        print(lower_input)
        if lower_input != str.lower(processString(lower_input)):
            print(lower_input)
            return lower_input
        
        return ""
    
    return deltaDebug(input_str[:-1])








def main():
    input = str.lower("abc123defG123")
    output = str.lower(processString("abcdefG"))
    print(input == output)

    out = deltaDebug(input)
    print(out)
main()