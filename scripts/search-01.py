sourceFile = "/tmp/inspiredev/passwords.txt"
selectedPass = []

with open(sourceFile, "r") as file:
    for line in file:
        if "123" in line:
            selectedPass.append(line.strip())
        
        if len(selectedPass) >= 100:
            break

for password in selectedPass:
    print(password)