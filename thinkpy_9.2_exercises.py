# EX. ONE
fin = open('words.txt')

def reader():
    for line in fin:
        fin.readline()
        word = line.strip()
        if len(word) > 20:
            print(word)

    # reader()

# EX. TWO

def has_no_e(word):
    if 'e' in word:
        return False
    return True

# print(has_no_e('heather'))
# print(has_no_e('trak'))

# EX. THREE
def avoids(word,forbidden_letter):
    for letters in word:
        if letters in forbidden_letter:
            return False
        return True
    
# print(avoids('tree', 'aio'))

def askavoids():
    forbidden = input('forbidden letters:')
    count = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden):
            count = count +1
    print(count)

#askavoids()

# EX. FOUR

def uses_only(word,letters):
    for characters in word:
        if characters not in letters:
            return False
    return True
    
# print(uses_only('tree', 'eter'))
print(uses_only('tree', 'apot'))

# EX. SIX
def is_abecadarian(word):
    previous=word[0]
    for letter in word:
        if letter<previous:
            return False
        previous = letter
    return True

# print(is_abecadarian('abcde'))
