def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string)==0 or len(string)==1:
        return string

    smallOutput=removeConsecutiveDuplicates(string[1:])

    if string[0]==string[1]:
        return smallOutput
    else:
        return string[0]+smallOutput
# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
