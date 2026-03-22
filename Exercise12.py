#Write the program copy the content of one file other
def read_the_file(o_filename,c_filename):
    with open(o_filename,"r") as rfile, open(c_filename,"w") as wfile:
        for item in rfile:
            wfile.write(item)              
read_the_file("sample.txt","copysample.txt") 

'''
#Write the program copy the content of one file other
def copy_file(source_file, destination_file):
    with open(source_file, "r") as rfile:
        content = rfile.read()

    with open(destination_file, "w") as wfile:
        wfile.write(content)

copy_file("sample.txt", "copysample.txt")

'''