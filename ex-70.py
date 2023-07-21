phrase = 'Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.'

i = 0
more_times = 0
letter_more_times = ''

while i < len(phrase):
    actual_letter = phrase[i]
    actual_letter_times = phrase.count(actual_letter)

    if actual_letter == ' ':
        i += 1
        continue

    if more_times < actual_letter_times:
        more_times = actual_letter_times
        letter_more_times = actual_letter
    
    i += 1
print(f'Letter: {letter_more_times} times: {more_times}')