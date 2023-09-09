import argparse
import json
import os

from clang.cindex import CursorKind, Index, TokenKind


def main():
    # コマンドライン引数をパースする。
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Input file")
    args = parser.parse_args()

    # 入力ファイル名を取得する。
    input_filename = os.path.basename(args.filename)

    # libclang の Index オブジェクトを作成する。
    index = Index.create()
    # 入力ファイルをパースする。
    # -x c++ オプションを指定することで、C++ のソースコードとしてパースする。
    translation_unit = index.parse(args.filename, args=["-x", "c++"])

    # コメントの行番号からコメント文字列へのディクショナリを作成する。
    comments = {}
    for token in translation_unit.cursor.get_tokens():
        if token.kind == TokenKind.COMMENT:
            line_number = token.location.line
            comment = token.spelling

            comments[line_number] = comment

    # 関数宣言の情報からなるリストを作成する。
    functions = []
    for child in translation_unit.cursor.get_children():
        # 関数宣言以外は無視する。
        if child.kind != CursorKind.FUNCTION_DECL:
            continue

        # ファイル名がない場合は無視する。
        if child.location.file is None:
            continue

        # ファイル名を取得する。
        filepath = child.location.file.name
        filename = os.path.basename(filepath)

        # 関数宣言があるファイルが入力ファイルに一致しない場合は無視する。
        # これがないと #include で読み込んだヘッダファイルの関数宣言も出力されてしまう。
        if filename != input_filename:
            continue

        # 各種情報を取得する。
        function_name = child.spelling
        return_type = child.result_type.spelling

        line_number = child.location.line
        comment = comments.get(line_number, "")

        params = []
        for param in child.get_arguments():
            param_name = param.spelling
            param_type = param.type.spelling

            params.append({
                "name": param_name,
                "type": param_type
            })

        functions.append({
            "name": function_name,
            "return_type": return_type,
            "params": params,
            "filename": filename,
            "line_number": line_number,
            "comment": comment
        })

    # JSON 形式で出力する。
    print(json.dumps(functions, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
