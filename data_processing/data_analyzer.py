
#%matplotlib inline
import matplotlib.pyplot as plt

import seaborn as sns

# Apply the default theme
sns.set_theme()

class DataAnalyzer:
    def __init__(self, df,revenue):
        self.df = df
        self.revenue = revenue

    #def perform_full_analysis(self, target_path): old with target to save the picture
    def perform_full_analysis(self):
        #self.perform_distribution_analysis(target_path)
        #self.perform_distribution_analysis(target_path)
        self.perform_monthly_revenue_scatter_analysis()
        print(f"DataAnalyzer: performed full analysis")

    def perform_correlation_analysis(self, target_path):
        # do some stuff here, work on correlations etc
        # maybe store results to a file
        print(f"DataAnalyzer: performed correlation analysis")

    def perform_distribution_analysis(self, target_path):
        # work on distributions etc
        # maybe store graphs to a file
        print(f"DataAnalyzer: performed distribution analysis")

    def perform_monthly_revenue_scatter_analysis(self):
        # work on distributions etc
        
        #X and Y axis inputs for Plotly graph. We use Scatter for line graphs
        sns.lineplot(data=self.revenue, x='InvoiceYearMonth', y='Revenue')
        plt.show()
        print(f"DataAnalyzer: performed distribution analysis")
