print ("""
    1.Подсчитать букв
    2.Слова в алф порядке
    """)

choise = input()
if choise == '1':

  text = input('Enter a text: ')
  chars = "abcdefghijklmnopqrstuvwxyzaABCDEFGHIJKLMNOPQRSTUVWXYZA"
  for char in chars:
      count = text.count(char)
      if count >= 1:
          print(char, count)
elif choise == '2':
  text = input('Enter words: ')
  remove_digits = str.maketrans('', '', '0123456789')
  text_wo_digits = text.translate(remove_digits)
  words = text_wo_digits.split()
  words.sort()
  print(' '.join(words))
else:
 print('Error')