def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

#print(has_no_e('trak'))

fin = open('words.txt')
line=fin.readline()

print(has_no_e(line)) # first word in words.txt