import os
import argparse
import sys


def create_structure_from_file(file_path, drive, dry_run=False):
    try:
        if not os.path.exists(file_path):
            print(f"❌ Error: '{file_path}' does not exist.")
            return

        with open(file_path, "r") as f:
            lines = f.readlines()

        stack = []
        root_dir = None

        for line in lines:
            if not line.strip():
                continue

            indent = len(line) - len(line.lstrip(" "))
            name = line.strip()

            # Root folder
            if root_dir is None:
                root_dir = os.path.join(drive, name.rstrip("/"))

                if dry_run:
                    print(f"[DRY RUN] 📁 Would create root folder: {root_dir}")
                else:
                    os.makedirs(root_dir, exist_ok=True)
                    print(f"📁 Root folder ready: {root_dir}")

                stack.append((root_dir, indent))
                continue

            while stack and stack[-1][1] >= indent:
                stack.pop()

            parent_path = stack[-1][0]
            new_path = os.path.join(parent_path, name.rstrip("/"))

            if name.endswith("/"):
                if dry_run:
                    print(f"[DRY RUN] 📂 Would create folder: {new_path}")
                else:
                    os.makedirs(new_path, exist_ok=True)
                    print(f"📂 Folder ready: {new_path}")

                stack.append((new_path, indent))

            else:
                if dry_run:
                    print(f"[DRY RUN] 📄 Would create file: {new_path}")
                else:
                    if not os.path.exists(new_path):
                        with open(new_path, "w") as f:
                            pass
                        print(f"📄 File created: {new_path}")
                    else:
                        print(f"📄 File exists (skipped): {new_path}")

        if dry_run:
            print("\n✅ Dry run completed. No files were created.")
        else:
            print("\n✅ Structure merged successfully!")

    except PermissionError:
        print("❌ Permission denied. Try running as administrator or choose another drive.")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Project Structure Generator")
    parser.add_argument("--file", default="structure.txt", help="Path to structure file")
    parser.add_argument("--drive", default="D:\\", help="Drive or base path")
    parser.add_argument("--dry-run", action="store_true", help="Preview without creating files")

    args = parser.parse_args()

    create_structure_from_file(args.file, args.drive, args.dry_run)
