import pandas as pd

class DBRetriever:
    def __init__(self, path="data/hospitals.csv"):
        self.df = pd.read_csv(path)

    def query(self, query):
        results = self.df[self.df.apply(lambda row: query.lower() in str(row).lower(), axis=1)]
        return results.to_string(index=False) if not results.empty else "No DB results"