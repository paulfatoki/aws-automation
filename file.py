definition1 = """
A computer file is a computer resource for recording data discretely in a
computer storage device. Just as words can be written 
to paper, so information can be written to a computer
file. Files can be edited and transferred through the 
internet on that particular computer system."""

#We will write this into a file with the name file_definition.txt:

open("file_definition.txt", "w").write(definition1)

#read the content of the file into a test file

new_text = open("file_definition.txt").read()
print(new_text)


#now read the file line by line
open("ad_lesbiam.txt", "w").write(new_text)

with open("ad_lesbiam.txt", "r") as fh:
    for line in fh:
        print(line.strip())
        
#if you do not want to use with, then you can use the code below 
# but without excluively closing end loop

fh = open("ad_lesbiam.txt")
for line in fh:
        print(line.strip())
fh.close()