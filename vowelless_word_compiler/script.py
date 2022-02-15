output = open("output.txt", "w", encoding="utf-8")

with open("../BengaliWordList_439.txt", encoding="utf-8") as f:
    for line in f.readlines():
        if not any(
            i in line
            for i in (
                "া",  # আ-কার
                "ি",  # ই-কার
                "ী",  # ঈ-কার
                "ু",  # উ-কার
                "ূ",  # ঊ-কার
                "ৃ",  # ঋ-কার
                "ে",  # এ-কার
                "ৈ",  # ঐ-কার
                "ো",  # ও-কার
                "ৌ",  # ঔ-কার
            )
        ):
            output.write(line)
output.close()