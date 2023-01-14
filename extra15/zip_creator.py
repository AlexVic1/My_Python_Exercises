import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.path(dest_dir, "Compressed.zip")
    with zipfile.ZipFile(dest_dir, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath, arcname=filepath.name)
            
if __name__ == '__main__':
    make_archive(filepaths=[''])            