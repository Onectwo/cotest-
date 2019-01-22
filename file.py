import os.path

filename = "COBOX_1.5.2_TEST"
extension = ".xml"
increment = 0;

fullFilename = filename + extension

while os.path.isfile(fullFilename):
				increment += 1
				fullFilename = "%s.%i%s" %(filename, increment, extension)

print (fullFilename)
with open(fullFilename,"w+") as f:

				f.write("Noroc, vai Vasea")
