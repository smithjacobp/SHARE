import os
def parent_directory():
    os.chdir("..")
    r = os.getcwd()
    return r
print(parent_directory())

# is this an ok method, idk
# i mean it worked