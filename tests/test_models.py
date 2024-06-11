import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_author_creation_with_different_name(self):
        author = Author(2, "Jane Smith")
        self.assertEqual(author.name, "Jane Smith")

    def test_author_id(self):
        author = Author(3, "Alice Johnson")
        self.assertEqual(author.id, 3)

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_article_creation_with_different_title(self):
        article = Article(2, "Another Title", "Another Content", 2, 2)
        self.assertEqual(article.title, "Another Title")

    def test_article_content(self):
        article = Article(3, "Sample Title", "Sample Content", 3, 3)
        self.assertEqual(article.content, "Sample Content")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_magazine_creation_with_different_name(self):
        magazine = Magazine(2, "Health Monthly", "Health")
        self.assertEqual(magazine.name, "Health Monthly")

    def test_magazine_id(self):
        magazine = Magazine(3, "Lifestyle Quarterly", "Lifestyle")
        self.assertEqual(magazine.id, 3)

if __name__ == "__main__":
    unittest.main()
