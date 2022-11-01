

class join():
    def search(text):
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")
        
        
        q = []
 
        for j in search(text, tld="co.in", num=10, stop=10, pause=2):
            q.append(j)
        return q