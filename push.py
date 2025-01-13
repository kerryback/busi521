import os
os.system("git pull origin main")
os.system("quarto render")
with open("docs/CNAME", "w") as f:
    f.write("https://busi521.kerryback.com")
os.system("git add .")
os.system("git commit -m 'update'")
os.system("git push origin main")