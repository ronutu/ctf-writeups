import pandas as pd

df = pd.read_csv("packetz.csv")

flag = ""
key = "OLKC" * 17 + "OL"
for i in range(len(df["Differentiated Services Field"])):
    flag += chr(
        int(
            df["Differentiated Services Field"][
                len(df["Differentiated Services Field"]) - i - 1
            ],
            0,
        )
        ^ ord(key[i])
    )

print(flag)
