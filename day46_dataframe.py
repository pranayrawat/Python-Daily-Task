import pandas as pd

data = [[2009,"Brothers","Drama"],[2002,"Spider-Man","Sci-fi"],[2009,"WatchMen","Drama"],[2010,"Inception","Sci-fi"],[2009,"Avatar","Fantasy"]]

df = pd.DataFrame(data,index=[i+1 for i in range(len(data))],columns=["year","Title","genre"])
print(df)