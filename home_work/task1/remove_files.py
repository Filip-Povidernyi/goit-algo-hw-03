import os
from pathlib import Path
import sys
import shutil


def wrapper(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}. Please check the path.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

    return inner


@wrapper
def check_folder(path: Path, dest: Path) -> str:

    for file in path.iterdir():

        if file.is_file():

            if file.suffix.lower() in ('.jpeg', '.png', '.jpg', '.svg', '.tif'):
                shutil.copy(file, dest / 'images' / file.name)
                print(f"Copied {file.name} to {dest}")

            elif file.suffix.lower() in ('.mp4', '.avi', '.mov', '.mkv'):
                shutil.copy(file, dest / 'videos' / file.name)
                print(f"Copied {file.name} to {dest}")

            elif file.suffix.lower() in ('.mp3', '.wav', '.flac'):
                shutil.copy(file, dest / 'audio' / file.name)
                print(f"Copied {file.name} to {dest}")

            elif file.suffix.lower() in ('.pdf', '.docx', '.txt'):
                shutil.copy(file, dest / 'documents' / file.name)
                print(f"Copied {file.name} to {dest}")

            elif file.suffix.lower() in ('.zip', '.gztar', '.bztar', '.xztar', '.tar', '.tar.gz', '.tar.bz2', '.tar.xz'):
                shutil.unpack_archive(file, dest / 'archives' / file.stem)
                print(f"Unpacked {file.name} to {dest}")

            else:
                shutil.copy(file, f"{dest}/others/{file.name}")
                print(f"Copied {file.name} to {dest}")

        elif file.is_dir():

            new_path = path / file.name
            check_folder(new_path, dest)

    return f"All files from {path} have been copied to {dest}"


def main():
    args = sys.argv[1:]
    path_folder = ''
    dest_path = ''
    if len(args) == 1:
        path_folder = args[0]
    elif len(args) == 2:
        path_folder = args[0]
        dest_path = args[1]
    else:
        print(
            "Usage: python home_work/task1/remove_files.py <path to working folder> <path to destination folder>")
        sys.exit(1)

    path = Path(path_folder)

    if not dest_path:
        dest = path / 'dest'
        os.makedirs(dest, exist_ok=True)
    else:
        dest = Path(f"{dest_path}/dest")
        os.makedirs(dest, exist_ok=True)

    os.makedirs(dest / 'images', exist_ok=True)
    os.makedirs(dest / 'videos', exist_ok=True)
    os.makedirs(dest / 'audio', exist_ok=True)
    os.makedirs(dest / 'documents', exist_ok=True)
    os.makedirs(dest / 'archives', exist_ok=True)
    os.makedirs(dest / 'others', exist_ok=True)

    print(check_folder(path, dest))


if __name__ == "__main__":
    main()
