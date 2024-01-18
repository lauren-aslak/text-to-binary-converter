message = input('enter the phrase you would like to convert: ')
ascii = 0
asciiNums = []
alphabet = [" ","!",".","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a", "b", "c", "d", "e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",'t','u','v','w','x','y','z']
asciiEquiv = [32,33,46,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
biNum = 0
decNum = 0

def letterToAscii():
  global message
  global ascii
  global alphabet
  global asciiEquiv

  for i in range(len(message)):
    letter = message[i]
    for i in range(len(alphabet)):
      if letter == alphabet[i]:
        asciiNums.append(asciiEquiv[i])


def asciiToBinary():
  global biNum
  global decNum
  global asciiNums

  for i in range(len(asciiNums)):
    num = asciiNums[i]
    #no clue why the range num has to be 8 (maybe bc that's how many if/elifs there are??)
    for i in range(8):
      if num >= 128:
        num -= 128
        biNum += 10000000
      elif num >= 64:
        num -= 64
        biNum += 1000000
      elif num >= 32:
        num -= 32
        biNum += 100000
      elif num >= 16:
        num -= 16
        biNum += 10000
      elif num >= 8:
        num -= 8
        biNum += 1000
      elif num >= 4:
        num -= 4
        biNum += 100
      elif num >= 2:
        num -= 2
        biNum += 10
      elif num >= 1:
        num -= 1
        biNum += 1
    print(biNum)
    biNum = 0


letterToAscii()

print(asciiNums)

asciiToBinary()