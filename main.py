#print(f'nameError - {type(NameError)}}')
'''print(maxim)
print('hello')'''
try:
    print('start code')
    #print(illia) error
    print('no error')
except:
    print('we have error')
print('the end')

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#print(f'nameError - {type(NameError)}}')
'''print(maxim)
print('hello')'''
try:
    print('start code')
    print(10/0) #error
    print('no error')
except NameError:
    print('we have NameError')
except ZeroDivisionError:
    print("we have ZeroDivisionError ")
try:
    print('start code')
    print(5/0)
    print('no error')
except (NameError,ZeroDivisionError) as error:
    print("error")
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
try:
    try:
        print('start')
        print(error)
        print('no error')
    except SyntaxError:
        print('Wrong Syntax')
except NameError as error
    print('error')