short = input('Choose an option A/B : ')

# рахує скільки букв в тексті
if short == 'A':
    text = input('Enter some text: ')
    f_set = {}
    for i in set(text):    # множество не виводить однакові
        f_set[i] = text.count(i)    # рахує  входящі елементи в списку
    print(f_set)

# виводить слова в алфавітному порядку
if short == 'B':
    s_text = input('Enter some text: ').split()  # розділяє на список
    st = ''
    for i in sorted(s_text):   # сортурує по алфавіту
        st = st + i + "; \n"
    print(st)
