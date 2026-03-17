# rag/serpapi_retriever.py

import os
from serpapi.google_search import GoogleSearch

class SerpAPIRetriever:
    def query(self, query):
        params = {
            "q": query + " hospital",
            "api_key": os.getenv("SERPAPI_API_KEY"),
            "engine": "google"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        if "organic_results" in results:
            return "\n".join([r.get("title", "") for r in results["organic_results"][:3]])

        return "No web results"