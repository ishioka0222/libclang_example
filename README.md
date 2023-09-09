# libclangを使用してC++言語のソースコードから関数宣言の情報を取得する例

## 実行方法

### Poetryがインストールされている場合

以下のコマンドで実行できます。

```bash
poetry install
poetry run main ./resources/header.h
```

### Poetryがインストールされていない場合

以下のコマンドで実行できます。

```sh
pip install -r requirements.txt
python ./src/libclang_example/main.py ./resources/header.h
```
