def intro_to_game():
    print('Hi! Today we are going to play madlibs. Please choose a madlib sheet from the following options: ')
    print('A) Roses are Red')
    user_choice = input()
    return user_choice


user_choice = intro_to_game()
print(f"\nThe user picked sheet {user_choice}")
