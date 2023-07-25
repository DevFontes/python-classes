questions = [
    {
        'Question': 'How much is 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'How much is 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'How much is 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

correct_answers = 0
for i in questions:
    print('Question:', i['Question'])
    print()

    options = i['Options']

    for j, option in enumerate(options):
        print(f'{j})', option)
    print()

    chosen = input('Chose one option: ')

    hit = False
    chosen_int = None
    qty_options = len(options)

    if chosen.isdigit():
        chosen_int = int(chosen)

    if chosen_int is not None:
        if chosen_int >= 0 and chosen_int < qty_options:
            if options[chosen_int] == i['Answer']:
                hit = True

    print()
    if hit:
        correct_answers += 1
        print('Hit 👍')
    else:
        print('Mistake ❌')

    print()

print('You got', correct_answers, 'ansers right')
print('of', len(questions), 'questions.')