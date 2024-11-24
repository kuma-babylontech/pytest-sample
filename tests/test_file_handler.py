import pytest
from src.file_handler import write_to_file, read_from_file


@pytest.fixture
def temp_file(tmp_path):
    # tmp_path は、pytest が提供する組み込みフィクスチャで、一時ディレクトリのパスを返す
    file_path = tmp_path / "test_file.txt"
    yield file_path


def test_file_write_and_read(temp_file):
    """ ファイルへの書き込みと読み取りをテスト """
    content = "Hello, Pytest!"
    write_to_file(temp_file, content)
    assert read_from_file(temp_file) == content


def test_empty_file(temp_file):
    """ 空のファイルをテスト """
    write_to_file(temp_file, "")
    assert read_from_file(temp_file) == ""


def test_file_not_found(tmp_path):
    """ 存在しないファイルを読み取ると FileNotFoundError が発生することをテスト """
    non_existent_file = tmp_path / "non_existent.txt"
    with pytest.raises(FileNotFoundError):
        read_from_file(non_existent_file)
