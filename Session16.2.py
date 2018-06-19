

import numpy as np 
import pandas as pd


Dataset = np.array([3, 21, 98, 203, 17, 9])
Mean = Dataset.mean()
print("Mean of the Value:-")
print(Mean)
N= Dataset.size
Method = lambda V: pow(abs(V-Mean),2)  
    
Df = pd.DataFrame(Dataset,columns={'X'})

Df.describe()

Df['(X - X^)2'] = Df['X'].apply(Method)
Df.head(10)
Sigma = Df['(X - X^)2'].sum()

print("Sigma  :-\n",Sigma)
variance =Sigma/N 

print("Variance for Data :\n",variance)
print("Variance built-in numpy Function: \n ",Dataset.var())
print("Variance buit-in panda \n",Df['X'].var())