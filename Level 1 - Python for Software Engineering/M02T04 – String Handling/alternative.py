sentence = input('Enter a string: ')
new_sentence = ''

for i in range(len(sentence)):
    if i%2 ==1:
        new_sentence += sentence[i].upper()
    else:
        new_sentence += sentence[i].lower()

print(new_sentence)

sentence       = input('Enter a string: ')
new_sentence   = sentence.split()
final_sentence = ""

for i in range(len(new_sentence)):
    if i%2 ==1:
        final_sentence += new_sentence[i].upper()
        final_sentence += " "
    else:
        final_sentence += new_sentence[i].lower()
        final_sentence += " "

final_sentence.strip
print(final_sentence)