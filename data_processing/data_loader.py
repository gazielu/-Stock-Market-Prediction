import numpy as np
import pandas as pd
import os

class DataLoader:

    def load_local_csv(self, local_file):
        # here add some logic that loads the data (from local file / cloud storage / url / etc)
        # inheritance can be handy here
        #df = pd.DataFrame(np.random.randn(152, 18)) # lets say it was loaded from local csv
        path = os.path.join('data/',local_file )
        df = pd.read_csv(path,encoding="ISO-8859-1")
        print(f"Loaded data from {local_file}")

        return df

    def load_from_url(self, url, target_path=None):
        # reload data from the internet and store it locally
        df = pd.DataFrame(np.random.randn(50, 7)) # simulating data loading
        if target_path:
            # store data in target_path after loading
            pass

        print(f"DataLoader: Loaded data from {url} and stored it to {target_path}")
        return df

# data_loader = DataLoader()
# loaded_data = data_loader.load_local_csv('OnlineRetail.csv')
# loaded_data.head()

# import pandas as pd
# import os
# filename = "OnlineRetail.csv"
# path = os.path.join('../data/',filename )
# # #tx_data = pd.read_csv(r'C:\BI\Python\00_KnowledgeHub\044_ml-skeleton-main\data\OnlineRetail.csv',encoding="ISO-8859-1")
# tx_data = pd.read_csv(path,encoding="ISO-8859-1")
# print(tx_data.head())



# import os
# filename = "OnlineRetail.csv"
# path = os.path.join('../data/',filename )
# print(path)
# #os.getcwd()