output = open("output.txt", "w", encoding="utf-8")

with open("../BengaliWordList_439.txt", encoding="utf-8") as f:
    for line in f.readlines():
        if line.strip().endswith("মাস"):
            output.write(line)
output.close()