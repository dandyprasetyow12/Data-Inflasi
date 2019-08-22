import pandas as pd

data = pd.read_excel (r'C:\Users\dandyprasetyow\Desktop\inflasi.xlsx') 
df = pd.DataFrame(data, columns= ['Month','Inflasi','Kesimpulan'])
print (df)