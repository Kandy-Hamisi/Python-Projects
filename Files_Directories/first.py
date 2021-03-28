from pathlib import Path

#Absolute Path -- root of hard drive
#Relative path -- from specific folder

path1 = Path("ecommerce")

print(path1.exists())

# path1.mkdir - Adds a directory
# path1.rmdir - removes a directory
# path1.glob('*.py')

for file in path1.glob('*.py'):
    print(file)
