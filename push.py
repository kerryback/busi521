import os
os.system("git add .")
string = "my message"
os.system("git commit -m %s" % string)
os.system("git push origin main")