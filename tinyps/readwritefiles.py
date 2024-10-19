from pathlib import Path
import zipfile
import shutil


def file_extractor():
    global out_path
    out_path = Path.home() / "Downloads" / "autobor_files"
    if not out_path:
        zipfile_path = (
            Path.home() / "Downloads" / "Automate_the_Boring_Stuff_onlinematerials.zip"
        )

        out_path = Path.home() / "Downloads" / "autobor_files"

        with zipfile.ZipFile(zipfile_path, "r") as zip_file:
            zip_file.extractall(out_path)


def move_file():
    data_folder = Path("datasets")
    if not data_folder:
        data_folder.mkdir(parents=True, exist_ok=True)

    destination = data_folder / "autobor_files"

    if not destination.exists():
        shutil.copytree(out_path, destination)


file_extractor()
move_file()
