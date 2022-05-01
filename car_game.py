start_value = 'start'
stop_value = 'stop'
quit_value = 'quit'
help_value = 'help'
car_started = False
while True:
    user_input = input('> ')
    if user_input.lower() == start_value and car_started is False:
        print('Car started...Ready to go!')
        car_started = True
    elif user_input.lower() == start_value and car_started is True:
        print('Car already started.')
    elif user_input.lower() == stop_value and car_started is True:
        print('Car stopped.')
        car_started = False
    elif user_input.lower() == stop_value and car_started is False:
        print('Car already stopped.')
    elif user_input.lower() == quit_value:
        break
    elif user_input.lower() == help_value:
        print('')
        print('start - to start the car.')
        print('stop - to stop the car.')
        print('quit - to exit')
        print('')
    else:
        print("I don't understand that...")