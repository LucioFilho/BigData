with open('text.txt', 'a') as file:
    print(file.read())

# write some file
with open('new_text.txt', 'w') as file:
    file.write('\nbla bla bla')

'''
a = append
r = read
w = write
'''