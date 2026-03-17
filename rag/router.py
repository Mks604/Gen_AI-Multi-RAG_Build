class QueryRouter:
    def route(self, query):
        query = query.lower()

        if "policy" in query or "rule" in query:
            return "vector"
        elif "best" in query or "near" in query:
            return "web"
        else:
            return "db"