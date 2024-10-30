# 1. random() # returns values from 0 to 1 with decimal values
'''from random import *
for i in range(10):
    print(random()) 

# 2. randint() # returns integers only
from random import *
for i in range(10):
    print(randint(1,30))

# 3. uniform() # returns float values between x and y
from random import *
print(uniform(1,10)) # returns single value only
for i in range(10): # returns 10 random values
    print(uniform(1,5))


# 4. randrange()
from random import *
print(randrange(10)) # returns single value only
print(randrange(1,10,2)) # returns single value only
'''

# 5. choice()
from random import *
list = ["A","B","C","D","E","F"]
print(list)
for i in range(10):
    print(choice(list)) # prints 10 times random values from list

