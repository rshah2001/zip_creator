import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    # this is a directory to zip files
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            file.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["bonus3.py", "bonus4.py"], dest_dir="dest")
