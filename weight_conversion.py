weight = float(input('Input the weight : '))
lbs_or_kgs = input('(L)bs or (K)g ? ')
if lbs_or_kgs.upper() == 'L':
    print('Weight is ', weight*.45, ' kg.')
elif lbs_or_kgs.upper() == 'K':
    print('Weight is ', weight*2.2, ' lbs')
else:
    print('Enter correct option')
