def pairStar(string):
    # Please add your code here
    if len(string)==0 or len(string)==1:
        return string

    smallOutput=pairStar(string[1:])

    if string[0]==string[1]:
        return string[0] + '*' + smallOutput
    else:
        return string[0]+smallOutput
    pass

# Main
string = input().strip()
print(pairStar(string))
