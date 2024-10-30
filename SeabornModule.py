'''import matplotlib.pyplot as plt 
import seaborn as sb 
sb.displot([0,1,2,3,4,5,6,8,7,9],hist=False)
plt.show()'''


'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=100), hist=False)

plt.show()'''


'''
import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)
'''
    
import pandas as pd 
mydata = {
    'Name ':['Raj','Kishore','Lokesh','Nani'],
    'age ':[20,23,16,18]
}

x=pd.DataFrame(mydata)
print(x)