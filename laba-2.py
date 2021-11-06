short = input("Choose an action A/B: ")

# рахує скільки букв в тексті
if short == "A":
    s = []
    text = input("Enter a text: ")
    for i in range(len(text)):
        if text[i] not in s and text[i] not in " ,.":
            s.append(text[i])
            s.append(text.count(text[i]))
    print(s)

# виводить слова в алфавітному порядку
elif short == "B":
    words = input("Enter a text: ").split(" ")
    w = []
    for p in words:
        if len(p) >= 3 and str.lower(p) not in w:
            w.append(str.lower(p))
    print(sorted(w))
