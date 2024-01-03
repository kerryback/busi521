import os
for ext in ["aux", "fdb_latexmk", "fls", "log", "nav", "out", "snm", "synctex.gz", "toc"]:
    os.system(f"del .\latex\*.{ext}")
os.system("move .\latex\*.pdf .\docs")
