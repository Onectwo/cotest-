import numpy as np 

print('Welcome to the COBOX TEST')

a = []
for i in range(0, 21):
    var = input(" The test result "+str(i+1)+ "   ")
    a.append(var)
    #print("The test nr.  " + str(i+1) + " is " + str(var))

print("The test outcome is:", np.array(a).T)
