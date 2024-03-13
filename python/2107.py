# author Kennethsoh

import math

print("Type of Question -- Option")
print("Find num of M for prob > 0.5 (one pool) -- 1")
print("Find num of M for prob > XX (two pool) -- 2")
print("Find probability given M and K (two pool) -- 3")
print("Find M and K, given n & probability (2 equal pool) -- 4")
option = int(input("Option: "))


if (option == 1):
  numOfMessages = input("Num of Messages (M) [optional]: ")
  numOfBits = int(input("Num of bits in hash (log(T, 2)): "))
  if (numOfMessages == ""):
    M = math.ceil(math.log(1.17*(math.sqrt(math.pow(2,numOfBits))), 2))
    print(f"Minimum number of messages m = 2^{M}")
  else:
    numOfMessages = int(numOfMessages)
    if (numOfMessages > 1.17*(math.sqrt(math.pow(2,numOfBits)))):
      print("Yes, Collision probability > 0.5") 
    else:
      print("No, Collision probability < 0.5")

elif (option == 2):
  k = int(input("Num of messages in 1st pool (k): "))
  n = int(input("Num of bits in hash (n): "))
  prob = (1 - float(input("Probability (1-0): ")))
  m = math.log(((math.log(prob) / math.log(2.7) ) / (k*math.pow(2,-n))) * -1, 2)
  mround = math.ceil(m)
  notation = ""
  if (mround < 20 and mround >= 10 ):
    notation = "K"
    mround = mround - 10
  elif (mround < 30 and mround >= 20):
    notation = "M"
    mround = mround - 20
  elif (mround < 40 and mround >= 30):
    notation = "G"
    mround = mround - 30
  elif (mround >= 40):
    notation = "T"
    mround = mround - 40
  mround = pow(2,mround)
  
  print(f"Number of messages m required = 2^{math.ceil(m)}, or approx {mround}{notation}")

# Find probability given k and m 
elif (option == 3):
  k3 = int(input("Num of messages in 1st pool (k): "))
  m3 = int(input("Num of messages in 2nd pool (m): "))
  n3 = int(input("Num of bits in hash (n): "))
  prob3 = 1 - math.pow(2.7, (-k3 * m3 * math.pow(2, -n3)))
  print(f"Probability = {prob3}")
  print(f"Probability = 2^{math.ceil(math.log(prob3, 2))}")
  


# Assuming k and m have the same value, find k or m, given n and probability
elif (option == 4):
  n4 = int(input("Num of bits in hash (n): "))
  prob4 = (1 - float(input("Probability (1-0): ")))
  k4 = math.sqrt(((math.log(prob4)/math.log(2.7)) / math.pow(2,-n4)) * -1)
  k4 = math.log(k4, 2)
  kround = math.ceil(k4)
  notation = "K"
  if (kround < 20 and kround >= 10 ):
    notation = "K"
    kround = kround - 10
  elif (kround < 30 and kround >= 20):
    notation = "M"
    kround = kround - 20
  elif (kround < 40 and kround >= 30):
    notation = "G"
    kround = kround - 30
  elif (kround >= 40):
    notation = "T"
    kround = kround - 40
  kround = pow(2, kround)
  
  print(f"k or m, assuming same value, is 2^{math.ceil(k4)}, or approx {kround}{notation}")


else:
  print("Give a valid option input")
  












 


