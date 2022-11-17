

class join():
    # This is where data is searched for.
    def search(text, how):
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")

        q = []

        for j in search(text, tld="co.in", num=how, stop=how, pause=2):
            q.append(j)
        return q
