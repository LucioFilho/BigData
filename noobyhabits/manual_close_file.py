# manually calling close file
def manually_calling_close_on_a_file(filename):
    f = open(filename, "w")
    f.write("hello!\n") # if it fails it never closes
    f.close()

# do it instead
def manually_calling_close_on_a_file(filename):
    with open(filename) as f:
        f.write("hello!\n")