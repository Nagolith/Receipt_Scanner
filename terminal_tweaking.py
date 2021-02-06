import os

# Shows current file path
# Should run with exit code 0
copy = os.system("cd")
print("'cd' ran with exit code %d" % copy)

# Meant to fail to show error vs success
unknown_dir = os.system("cd doesnotexist")
print("`cd doesnotexis` ran with exit code %d" % unknown_dir)