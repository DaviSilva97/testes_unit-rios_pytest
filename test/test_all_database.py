import dados.database as db

def test_add_in_database():
    assert db.add_in_database("teste", 180)

def test_get_all_in_database():
    assert len(db.get_all_books()) > 0   