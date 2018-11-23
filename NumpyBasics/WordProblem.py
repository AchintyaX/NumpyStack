# here we have word problem to be solved 




# the admission fee at a small fare is a $1.5  for children in $4 for
# adults on a certain day.2200 people enter the fair and five thousand fifty dollars is collected.
# How many children and how many adults attended.

# lets solve the problem using matrices

import numpy as np

# from the given data lets say we gave x1 as the num children
# x2 as the number of adults 

fair = np.array([[1,1],[1.5, 4]])
# the prices are in the fair variable

moneyCollected = np.array([[2200], [5050]])
# the money collected is in the moneyCollected array
# so lets find the number of children and adults
X = np.linalg.solve(fair,moneyCollected)

print("the number of children that were present were", X[0,0])
print("the number of adults that were present were", X[1,0])