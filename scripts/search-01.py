import os
sourceFile = "/tmp/inspiredev/passwords.txt"
destinationFile = "/tmp/inspiredev/selected_passwords.txt"
selectedPass = []

if os.path.isfile(sourceFile):
    print(f"File {sourceFile} exists.")
    with open(sourceFile, "r") as file:
        for line in file:
            if "123" in line:
                selectedPass.append(line.strip())
            
            if len(selectedPass) >= 100:
                break
else:
    print(f"File {sourceFile} does not exist.")

with open(destinationFile, "w") as file:
    for password in selectedPass:
        file.write(password + "\n")
