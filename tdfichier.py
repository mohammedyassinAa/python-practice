# package est un ensemble de modules organises dans des repetoires.
# Doc string documentation du  code Description variables et le retour  
with open("notes.txt", "r") as file :
    lines = file.readlines()
    lines=[line.strip() for line in lines]
print (lines)

# Q2
notes = [float(line.strip()) for line in lines]
moyenne = sum(notes)/len(notes)

print(f"{moyenne: .2f}" )
# Q3
with open('notes.txt', 'r') as file:
    lines = file.readlines()


with open('notes2.txt', 'w') as file2:
    for line in lines:
        note = float(line.strip())
        if note > 10:
            print("admis")
        else :
            print ("non admis")

file2.write(f"{note:.1f}\n")
