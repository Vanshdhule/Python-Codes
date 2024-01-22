import string
import random
choice = input("Do you want to code or decode? ")

if choice == "code":
  text = input("Enter here : ")
  words = text.split(" ")
  nwords = []
  for word in words:
    if(len(text) >= 3):
          new_text = word[1:] + word[0]
          r1 = "".join(random.choice(string.ascii_letters) for _ in range(3))
          r2 = "".join(random.choice(string.ascii_letters) for _ in range(3))
          final_text = r1 + new_text + r2
          nwords.append(final_text)   
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
    

    
else:
  nwords = []
  text = input("Enter here : ")
  words = text.split(" ")
  for word in words:
    if(len(text) >= 3):
      stnew =word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
  
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
