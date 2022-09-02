#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(message, shift):
  result = []
  for i in message:
    if i != " ":
      if ord (i) + shift < 123 and ord (i) > 96:
        result.append(chr (ord (i) + shift))
      elif ord (i) < 97:
        result.append(chr (ord (i)))
      else:
        result.append(chr (ord (i) + shift - 122 + 97))
    else:
      result.append(" ")
  return ''.join(result)

def decrypt(message, shift):
  result = []
  for i in message:
    if i != " ":
      if ord (i) - shift > 96 and ord (i) > 96:
        result.append(chr (ord (i) - shift))
      elif ord (i) < 97:
        result.append(chr (ord (i)))
      else:
        result.append(chr (ord (i) - shift + 122 - 97))
    else:
      result.append(" ")
  return ''.join(result)

  
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
print(encrypt("hello world!",9))
print(decrypt("qnuux gxbum!",9))