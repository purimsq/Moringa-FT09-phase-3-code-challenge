if __name__ == "__main__":
    from author import Author
    from magazine import Magazine
    from article import Article

    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    article1 = author1.add_article(magazine1, "The Future of AI")
    article2 = author1.add_article(magazine2, "Health Benefits of Yoga")
    article3 = author2.add_article(magazine1, "Cybersecurity Trends")
    article4 = author2.add_article(magazine1, "AI in Healthcare")

    print(author1.articles())
    print(author1.magazines())
    print(magazine1.articles())
    print(magazine1.contributors())
    print(magazine1.article_titles())
    print(magazine1.contributing_authors())
    print(Magazine.top_publisher())
    print(author1.topic_areas())
