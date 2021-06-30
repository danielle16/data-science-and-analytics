import pandas as pd 

# Read csv file
df = pd.read_csv("Resources/cities.csv")

# Save df to file
df.to_html("data.html", index=False)

# Assign to string
table = df.to_html()
print(table)