# bookstore.py

# ------------------------
# Mock functions
# ------------------------
def browse_books(category):
    books = {
        "Fiction": ["Book A", "Book B"],
        "Science": ["Book C"],
    }
    return books.get(category, [])

def search_books(query_type, query_value):
    books = [
        {"title": "Book A", "author": "Author X", "category": "Fiction", "price": 200, "desc": "Nice Fiction Book"},
        {"title": "Book B", "author": "Author Y", "category": "Fiction", "price": 300, "desc": "Another Fiction Book"},
        {"title": "Book C", "author": "Author Z", "category": "Science", "price": 150, "desc": "Science Book"},
    ]
    if query_type == "title":
        return [b for b in books if b["title"] == query_value]
    elif query_type == "author":
        return [b for b in books if b["author"] == query_value]
    elif query_type == "category":
        return [b for b in books if b["category"] == query_value]
    return []

def add_to_cart(cart, book):
    if not book:   # edge case: invalid book
        return cart
    if book in cart:
        cart[book] += 1
    else:
        cart[book] = 1
    return cart


# ------------------------
# Positive Test Cases
# ------------------------

# TC001-01: Verify browsing valid category (Fiction → returns Book A, Book B)
def test_browse_books_valid_category():
    result = browse_books("Fiction")
    assert "Book A" in result
    assert "Book B" in result

# TC001-02: Verify empty category (Poetry → no books found)
def test_browse_books_empty_category():
    result = browse_books("Poetry")
    assert result == []  # No books found

# TC002-01: Verify adding single book to cart
def test_add_single_book_to_cart():
    cart = {}
    cart = add_to_cart(cart, "Book A")
    assert cart["Book A"] == 1

# TC002-02: Verify adding multiple books to cart
def test_add_multiple_books_to_cart():
    cart = {}
    cart = add_to_cart(cart, "Book A")
    cart = add_to_cart(cart, "Book B")
    assert cart["Book A"] == 1
    assert cart["Book B"] == 1

# TC002-03: Verify cart updates quantity (Book A added twice → qty = 2)
def test_update_cart_quantity():
    cart = {}
    cart = add_to_cart(cart, "Book A")
    cart = add_to_cart(cart, "Book A")
    assert cart["Book A"] == 2


# ------------------------
# Negative / Failure Test Cases
# ------------------------

# TC001-03: Verify invalid category (123Invalid → return empty)
def test_browse_books_wrong_category():
    result = browse_books("123Invalid")
    assert result == []   # Should return empty

# TC002-04: Verify invalid book input (None → cart unchanged)
def test_add_invalid_book():
    cart = {}
    cart = add_to_cart(cart, None)   # Invalid input
    assert cart == {}  # Cart should remain empty

# TC002-05 (Not implemented): Verify removing item from cart
# NOTE: Remove functionality not implemented in code yet.
def test_cart_quantity_not_negative():
    cart = {"Book A": 1}
    # simulate mistake: removing not implemented
    assert cart["Book A"] >= 0


# ------------------------
# Extended Tests: Filter + Search
# ------------------------

# TC001-04: Verify search by title (Book A → returns Author X)
def test_search_by_valid_title():
    result = search_books("title", "Book A")
    assert result[0]["author"] == "Author X"

# TC001-05: Verify search by author (Author Y → returns Book B)
def test_search_by_valid_author():
    result = search_books("author", "Author Y")
    assert result[0]["title"] == "Book B"

# TC001-06: Verify search by category (Fiction → returns Book A, Book B)
def test_search_by_category_keyword():
    result = search_books("category", "Fiction")
    titles = [b["title"] for b in result]
    assert "Book A" in titles and "Book B" in titles

# TC001-07: Verify search shows details (title, price, desc present)
def test_search_results_display_fields():
    result = search_books("title", "Book A")[0]
    assert "title" in result and "price" in result and "desc" in result

# TC001-08: Verify invalid search keyword (NonExistingBook → empty list)
def test_search_invalid_keyword():
    result = search_books("title", "NonExistingBook")
    assert result == []

# TC002-06 (Future): Verify cart total calculation
# TC002-07 (Future): Verify empty cart checkout blocked
