# EXERCISE ONE
fin=open('words.txt')

def threedoubleletters(word):
    i = 0
    while len(word)-5>i:
        if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
            print(word)
            return True
        i = i+1
    
for line in fin:
    word=line.strip()
    #threedoubleletters(word)

# EXERCISE TWO
def is_palindrome(s):
    return s == s[::-1]

def odometer(word):
    num = int(word)
    # Check the required palindrome conditions
    if (is_palindrome(str(num)[2:6]) and
        is_palindrome(str(num + 1)[1:6]) and
        is_palindrome(str(num + 2)[1:5]) and
        is_palindrome(str(num + 3))):
        print(num)

fin = open('6digitpin.pdf.txt')

for line in fin:
    word = line.strip()
   # odometer(word)

# EXERCISE THREE
def is_reversal(word1,word2):
    if str(word1) == str(word2)[::-1]:
        return True

#print(is_reversal('73','37'))
                  




        

            
        
        


