import os
import shutil
import argparse


def flatten_files(src_dir, dest_dir):
    # フラットに格納するためのディレクトリを作成
    os.makedirs(dest_dir, exist_ok=True)

    # src_dir以下のすべてのファイルを探索
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # 元のファイルパスと新しいパスを定義
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)

            # ファイル名が重複する場合に備えて番号を追加する処理
            count = 1
            while os.path.exists(dest_file):
                name, ext = os.path.splitext(file)
                dest_file = os.path.join(dest_dir, f"{name}_{count}{ext}")
                count += 1

            # ファイルをコピー
            shutil.copy2(src_file, dest_file)

    print(f"すべてのファイルが {dest_dir} にフラットな形で保存されました。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flatten directory structure.")
    parser.add_argument("src_dir", help="Source directory path")
    parser.add_argument("dest_dir", help="Destination directory path")
    args = parser.parse_args()

    flatten_files(args.src_dir, args.dest_dir)
