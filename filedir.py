from pathlib import Path

#path = Path ("list.py")
#print(path.exists())
#path = Path("email")   
#print(path.rmdir())


path = Path()
for file in path.glob("*.py"): # "*" if you want directory
    print(file) 