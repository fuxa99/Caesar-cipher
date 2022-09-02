from art import logo

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

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "encode":  
  print(encrypt(text,shift))
else:
  print(decrypt(text,shift))