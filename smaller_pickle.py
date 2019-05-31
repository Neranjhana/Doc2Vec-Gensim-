import pickle
import pandas as pd
data=pd.read_pickle('Processed_Input_Data.pkl')
data= data.sample(frac=1).reset_index(drop=True)
#data=data.drop(data.index[[500,6000]])
indexes_to_drop=[x for x in range(1,3000)]
#indexes_to_keep = set(range(data.shape[0])) - set(indexes_to_drop)
pickle_out=open("batch1.pickle","wb")
data_sliced = data.take(list(indexes_to_drop))
pickle.dump(data_sliced,pickle_out)