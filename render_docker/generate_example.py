import random

result = []
for _ in range(100):
	example = []
	example.append(random.random())
	example.append(random.random())
	example.append(random.randint(10,100))
	example.append(random.randint(40,200))
	for _ in range(3):
		example.append(random.randint(0,50))
	for _ in range(3):
		example.append(random.randint(30,150))
	for _ in range(2):
		example.append(random.randint(0,50))
	for _ in range(4):
		example.append(random.choice([0,1]))
	result.append(example)
with open("generated_example.txt", "w") as f:
	f.write(str(result))
