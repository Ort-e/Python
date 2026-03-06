from Users_metods import Users

db = Users("postgresql://postgres:111@localhost:5432/Test")


def test_add_users():
    email = "test123@mail.ru"

    db.insert_users(email)
    users_get = db.get_users(email)
    db.delete_users(email)

    assert users_get[0]['user_email'] == email


def test_updated_users():
    email = "test123@mail.ru"
    put_email = "updated"

    db.insert_users(email)
    users_get = db.get_users(email)
    db.updated_users(put_email, email)
    users_get_update = db.get_users(put_email)
    db.delete_users(put_email)

    assert users_get != users_get_update


def test_delete_users():
    email = "test123@mail.ru"

    db.insert_users(email)
    users_get = db.get_users(email)
    db.delete_users(email)
    users_get_delete = db.get_users(email)

    assert users_get != users_get_delete
