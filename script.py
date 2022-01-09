import pandas as pd
df = pd.read_csv ('blast_res.csv')

values = df.iloc[:,1].unique()

d = {}
i = 0

f = open("output.csv", "w")
for x in values:
    d["string{0}".format(i)] = ""
    for y in range(364):
        if df.iloc[y].Resistance == x:
            d["string{0}".format(i)] += df.iloc[y].Block + "; "
    f.write(x.astype(str) + ', ' + d["string{0}".format(i)] + "\n")
    i+=1
f.close()
