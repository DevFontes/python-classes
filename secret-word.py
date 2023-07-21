import os

secret_word = 'jolinha'
correct_letters = ''
count = 0

while True:
    # print(f'The word have {len(secret_word)} letters')

    typed_letter = input('Type one letter: ')
    count += 1

    if len(typed_letter) > 1:
        print('Type only one letter')
        continue

    if typed_letter in secret_word:
        correct_letters += typed_letter

    formed_word = ''
    for correct in secret_word:
        if correct in correct_letters:
            formed_word += correct
        else:
            formed_word += '*'
    print(formed_word)

    if formed_word == secret_word:
        os.system('clear')
        print('You Win!! Congratulations!')
        print('The secret word was', secret_word)
        print(f'You trying {count} times!')
        break