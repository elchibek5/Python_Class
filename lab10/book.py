class Book:
    def __init__(self, title, author, publisher):
        self.__title = title # [cite: 4, 5]
        self.__author = author
        self.__publisher = publisher

    # Accessors and Mutators
    def get_title(self): return self.__title
    def set_title(self, title): self.__title = title

    def get_author(self): return self.__author
    def set_author(self, author): self.__author = author

    def get_publisher(self): return self.__publisher
    def set_publisher(self, publisher): self.__publisher = publisher

    def __str__(self): #
        return f"Book: {self.__title} by {self.__author}"