number_dict = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : 'nine',
    "10" : "ten"
}
user_inp = input("Enter number : ")
x = 0
output_text = ''
error_flag = False
for x in user_inp:
    if number_dict.get(x) is None:
        print('Invalid input, type only numbers..!')
        error_flag = True
        break
    else:
        output_text += number_dict.get(x) + " "
if not error_flag:
    print(output_text)
