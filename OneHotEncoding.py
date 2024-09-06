import pandas as pd
# file_path = "DMAL.csv"
# df = pd.read_csv(file_path)
# data=pd.DataFrame(df)
# dummies = pd.get_dummies(data)

# print(data,"\n")
# print(dummies)
# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder

# data = pd.read_csv("OneHot.csv")

# categorical_columns = ['Name', 'Gender']

# encoder = OneHotEncoder(handle_unknown='ignore')
# encoder.fit(data[categorical_columns])

# encoded_data = encoder.transform(data[categorical_columns]).toarray()

# numerical_columns = ['Age']
# data = pd.concat([data[numerical_columns], pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out())], axis=1)

# print(data)

df=pd.read_csv('DMAL.csv')
print(pd.DataFrame(df), "\n")
print(pd.get_dummies(pd.DataFrame(df)))

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
df=pd.read_csv('OneHot.csv')

cat_data=['Name','Gender']
encoder=OneHotEncoder(handle_unknown='ignore')

encoder.fit(df[cat_data])
encoded=encoder.transform(df[cat_data]).toarray()

num_data=['Age']
df1=pd.concat([df[num_data],pd.DataFrame(encoded,columns=encoder.get_feature_names_out())],axis=1)

print(df1)