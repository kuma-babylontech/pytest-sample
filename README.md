# Pytestプロジェクト

テストにPytestを使用するPythonプロジェクトです。

## インストール

1. リポジトリをクローンします:
    ```sh
    git clone https://github.com/kuma-babylontech/pytest-sample.git
    ```
2. プロジェクトディレクトリに移動します:
    ```sh
    cd pytest-sample
    ```
3. 仮想環境を作成します:
    ```sh
    python -m venv venv
    ```
4. 仮想環境を有効化します:
    - Windowsの場合:
        ```sh
        .venv\Scripts\activate
        ```
    - macOS/Linuxの場合:
        ```sh
        source .venv/bin/activate
        ```
5. 依存関係をインストールします:
    ```sh
    pip install -r requirements.txt
    ```

## テストの実行

テストを実行するには、次のコマンドを使用します:
```sh
pytest
```

カバレッジ付き
```sh
pytest --cov
```
