import os

try:
    filename = 'sample.png'
    f = open(filename, 'rU') 
    text = f.read() 
    f.close()
except IOError: 
  
    # print(os.error) will <class 'OSError'> 
    print('Problem reading: ' + filename)

# Get current path
print(os.getcwd())

# Rename file
'''
fd = "GFG.txt"
os.rename(fd,'New.txt')
'''d

# Opens notepad without user seeing commands
'''
cmd = 'notepad'
os.system(cmd)
'''

# Displays the home dir(windows os)
# 'echo' to display
'''
# os.system("echo %userprofile%")
'''

# Shows current file path
# Should run with exit code 0(no errors)
'''
copy = os.system("cd")
print("'cd' ran with exit code %d" % copy)
'''

# Should fail with exit code 1(errors)
'''
unknown_dir = os.system("cd doesnotexist")
print("`cd doesnotexis` ran with exit code %d" % unknown_dir)
'''
