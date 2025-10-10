print("Hello World!")
# print(self, *args, sep=' ', end='\n', file=None):

# self - please ignore  (oops)
# *args - unlimited number of comma separated arguments.
print("Hemanth","Amma","Appa",123,3.142,True)
#Values are separated by space , to change that we need to add a separator at the end
print("Hemanth","Amma","Appa",123,3.142,True,sep="-*-")
# By default it will be a new line but if we need to add a new line need to add end="\n"
print("Hemanth","Amma","Appa",123,3.142,True,sep="-*-",end="\n")

# Indentation
#IndentationError: unexpected indent
# If we give space @ starting Indentation error will show , To remove that we need to
#click right and > Reformat code
