import pytest
from src.db import create_table, insert_user, fetch_user


@pytest.fixture
def db_connection():
    """
    データベース接続を確立し、それを使用するためにyieldし、その後に閉じることを保証します。

    Yields:
        conn: データベース接続オブジェクト。
    """
    conn = create_table()
    yield conn
    conn.close()


def test_insert_and_fetch_user(db_connection):
    """ データベースへのユーザーの挿入と取得をテストします。

    このテスト関数は以下の手順を実行します:
    1. `insert_user` 関数を使用して、ID 1 と名前 "John Doe" のユーザーをデータベースに挿入します。
    2. `fetch_user` 関数を使用して、データベースからID 1 のユーザーを取得します。
    3. 取得したユーザーが挿入したユーザーと一致することをアサートします。

    引数:
        db_connection: データベースと対話するために使用されるデータベース接続オブジェクト。

    例外:
        AssertionError: 取得したユーザーが挿入したユーザーと一致しない場合。
    """
    insert_user(db_connection, 1, "John Doe")
    user = fetch_user(db_connection, 1)

    assert user == (1, "John Doe")


def test_fetch_nonexistent_user(db_connection):
    """
    存在しないユーザーをデータベースから取得するテスト。

    このテストは、データベースに存在しないIDのユーザーを取得しようとすると
    Noneが返されることを確認します。

    引数:
        db_connection: データベース接続オブジェクト。

    アサート:
        取得したユーザーがNoneであること。
    """
    user = fetch_user(db_connection, 999)
    assert user is None


def test_duplicate_user_id(db_connection):
    """
    重複するユーザーIDでユーザーを挿入すると例外が発生することをテストします。

    引数:
        db_connection: データベース接続オブジェクト。

    手順:
        1. ユーザーID 1 と名前 "Alice" のユーザーを挿入します。
        2. 同じユーザーID 1 と名前 "Bob" の別のユーザーを挿入しようとします。
        3. 重複するユーザーIDのために例外が発生することを確認します。
    """
    insert_user(db_connection, 1, "Alice")
    with pytest.raises(Exception):
        insert_user(db_connection, 1, "Bob")


def test_create_table(db_connection):
    """
    テーブルが正しく作成されることをテストします。

    引数:
        db_connection: データベース接続オブジェクト。

    手順:
        1. テーブル 'users' が存在することを確認します。
    """
    cursor = db_connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table = cursor.fetchone()
    assert table is not None
    assert table[0] == 'users'
