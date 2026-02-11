sample_bay = [ "Basalt", "Silica", "Iron", "Dust"]
print(sample_bay[0]) #Printing 1st item in list
print(sample_bay[-1]) #'-1' > Negative indexing
print(len(sample_bay)) #Printing total no of samples

for sample in sample_bay:
    print(f"Transmitting data for: {sample}")

new_findings = []
for i in range(3):
    rock = input ("Enter rock: ")
print(new_findings)

if "Dust" in sample_bay:
    sample_bay.remove("Dust")
print(sample_bay)