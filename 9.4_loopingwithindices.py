def is_abecedarian(word):
    i = 0
    while len(word) - 1> i:
        if word[i+1]<word[i]:
            return False
        i = i + 1
        return True
    
print(is_abecedarian('abcdef'))
