from article import Article

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string.")

        Magazine.all_magazines.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters.")
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors_count = {}
        for article in self.articles():
            if article.author in authors_count:
                authors_count[article.author] += 1
            else:
                authors_count[article.author] = 1
        
        return [author for author, count in authors_count.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not Article.all_articles:
            return None
        magazine_count = {}
        for article in Article.all_articles:
            if article.magazine in magazine_count:
                magazine_count[article.magazine] += 1
            else:
                magazine_count[article.magazine] = 1

        top_magazine = max(magazine_count, key=magazine_count.get)
        return top_magazine
