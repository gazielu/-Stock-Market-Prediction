import argparse
# Import seaborn
import seaborn as sns
# Apply the default theme
sns.set_theme()


from data_processing.data_analyzer import DataAnalyzer
from data_processing.data_loader import DataLoader
from data_processing.data_processor import DataProcessor


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage gazielu machine learning processing pipeline')
    
    parser.add_argument('--data-path',
                        type=str,
                        default=None,
                        help='url to load the data from')
    parser.add_argument('--flatfile-name',
                        type=str,
                        default=None,
                        help='local path to store the output')
    args = parser.parse_args()
    print('Parameters: {}'.format(args))

    data_loader = DataLoader()
    loaded_data = data_loader.load_local_csv(args.flatfile_name)
    # data_processor = DataProcessor(loaded_data)
    # processed_data,revenue_data = data_processor.process_data_for_analysis()
    # data_analyzer = DataAnalyzer(processed_data,revenue_data)
    # data_analyzer.perform_full_analysis()
 
else:
    pass

#print(processed_data.head(3))
#print(revenue_data.head(10))
# print(processed_data.head())
# data_loader = DataLoader()
# loaded_data = data_loader.load_local_csv('xx')
# loaded_data.head()

#https://towardsdatascience.com/data-driven-growth-with-python-part-1-know-your-metrics-812781e66a5b