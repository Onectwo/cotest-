import os.path
import numpy as np

filename = "COBOX_1.5.2_TEST"
extension = ".xml"
increment = 0;
print('Welcome to the COBOX TEST')

fullFilename = filename + extension

while os.path.isfile(fullFilename):
				increment += 1
				fullFilename = "%s.%i%s" %(filename, increment, extension)

print (fullFilename)
with open(fullFilename,"w+") as f:
                                a = []
                                for i in range(0, 21):
                                    var = input(" The test result "+str(i+1)+ "   ") 
                                    a.append(var)
                                    f.write(str(i+1))
                                    f.write("    ")
                                    f.write(str(var))
                                    f.write('\n')

				
