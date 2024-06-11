class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be an instance of Author class.")

        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be an instance of Magazine class.")

        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters.")

        Article.all_articles.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Author must be an instance of Author class.")
    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError("Magazine must be an instance of Magazine class.")
    
    @property
    def title(self):
        return self._title
