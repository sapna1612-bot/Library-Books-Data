<!DOCTYPE html>
<html>
<head>
    <title>Library Books</title>
</head>
<body>
    <h1>All Books</h1>
    <ul>
        {% for book in books %}
            <li>{{ book.title }} by {{ book.author }} (ISBN: {{ book.isbn }})</li>
        {% empty %}
            <li>No books available.</li>
        {% endfor %}
    </ul>
</body>
</html>
