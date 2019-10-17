word_input =  input()
word_match = "hello"
match_index = 0
letter =0
while letter < len(word_input) and match_index < len(word_match):
    if word_match[match_index] == word_input[letter]:
        match_index += 1
    letter += 1

retorno = ""
if match_index == len(word_match):
    retorno = "YES"
else:
    retorno = "NO"

print (retorno)
    