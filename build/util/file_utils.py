import filecmp
import os
import shutil
import zipfile


def copy_with_updates(src_dir, dest_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            src_path = os.path.join(root, file)
            dest_path = os.path.join(dest_dir, os.path.relpath(src_path, src_dir))

            # Check if the destination file exists and if it's the same as the source file
            if os.path.exists(dest_path) and filecmp.cmp(src_path, dest_path, shallow=False):
                print(f"Skipping {file} - No changes")
            else:
                # Create the destination directory if it doesn't exist
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                # Copy the file with its original metadata (timestamps, permissions, etc.)
                shutil.copy2(src_path, dest_path)
                print(f"Copied {file} - Updated")

    # Remove files from destination that no longer exist in the source
    for root, _, files in os.walk(dest_dir):
        for file in files:
            dest_path = os.path.join(root, file)
            src_path = os.path.join(src_dir, os.path.relpath(dest_path, dest_dir))
            if not os.path.exists(src_path):
                os.remove(dest_path)
                print(f"Removed {file}")


def zip_files(src_files, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for src_file_path, arcname in src_files:
            zipf.write(src_file_path, arcname=arcname)


def remove_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Removed {file_path}")
