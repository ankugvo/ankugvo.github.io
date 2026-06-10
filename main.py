p = "fhl"
x = []
while p != "q":
    p = input()
    x.append(p)
while "" in x:
    del x[x.index("")]
while "q" in x:
    del x[x.index("q")]
x.sort()
for i in x:
    print(f"                <tr><td>{i}</td></tr>")