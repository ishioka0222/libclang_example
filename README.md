# PythonのlibclangでC++のヘッダーファイルから情報を抽出する例

説明は以下のURLで公開しています。  
https://qiita.com/ishioka0222/items/3be5df6f8c503a8e307f

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
