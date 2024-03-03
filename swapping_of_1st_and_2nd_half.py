string = input("Enter the string : ")

#Swapping part
if len(string) > 1:
    mid = len(string)//2
    left_half = string[:mid]
    right_half = string[mid:]
    print("The 1st half is : ",left_half)
    print("The 2nd half is : ",right_half)
    print("By Swapping the 1st and 2nd half we get : ", right_half + left_half)
else:
    print("---Please write some lengthy string, that contains atleast 2 or more letters---")

