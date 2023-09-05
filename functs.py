def show_get_next_step():
    print('1. Add new password')
    print('2. Get a password')
    print('3. Edit a password')
    print('4. Delete a password')
    print('5. Generate and Save Password')
    print('6. Show password by keyword')
    print('7. Exit')
    b = input('-> ')
    if not b.isdigit():
        print('Please enter a number')
        return show_get_next_step()
    else:
        b = int(b)
        if b not in range(1, 8):
            print('Please enter a number between 1 and 7')
            return show_get_next_step()
        else:
            return b