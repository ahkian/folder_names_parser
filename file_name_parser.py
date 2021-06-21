import os

y = 'y'
n = 'n'

def parse_file_name ():
    print( "Ensure your working directory is the one you wish to list")
    while True:
        continue_exec = str(input("Should function continue? (y/n)"))
        if continue_exec == "n":
            print("Exiting execution")
            return None
        elif continue_exec == "y":
            print ("Continuing Execution")
            break
        else:
            print("That is not a valid input")
    # This is where parsing happens
    output_file = open('C:\Users\dbrazel\Desktop\parser_output.txt', 'w')
    cwd = os.getcwd()
    my_files = os.listdir(cwd)
    for f in my_files:
        output_file.write(f + ", ")
        print(f)
    output_file.close()
    
    
    
parse_file_name()