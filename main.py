import art
def caesar_cipher(text, shift, action):
  result = ""
  if action == "decode":
      shift = -shift
  for char in text:
      if char.isalpha():
          alphabet = 'abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
          position = alphabet.index(char)
          new_position = (position + shift) % 26
          result += alphabet[new_position]
      else:
          result += char
  return result
print(art.logo)
while True:
  mode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  if mode not in ["encode", "decode"]:
      print("Invalid input. Please type 'encode' or 'decode'.")
      continue

  message = input("Type your message with no spaces: ")
  shift = int(input("Type the shift number: "))

  result = caesar_cipher(message, shift, mode)
  print(f"Here's the {mode}d result: {result}")

  again = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
  if again != "yes":
      break
