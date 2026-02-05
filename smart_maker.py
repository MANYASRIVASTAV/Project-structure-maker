
import os


def create_project():

    # Get Desktop Path (Windows)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    project_name = input("Enter project name: ")

    base_path = os.path.join(desktop_path, project_name)

    os.makedirs(base_path, exist_ok=True)

    print("\nProject folder created on Desktop:", base_path)


    while True:

        folder = input("\nEnter folder name (or 'done' to finish): ")

        if folder.lower() == "done":
            break

        folder_path = os.path.join(base_path, folder)

        os.makedirs(folder_path, exist_ok=True)

        print(" Folder created:", folder)


        while True:

            file = input(f"   Enter file inside '{folder}' (or 'next' to stop): ")

            if file.lower() == "next":
                break

            file_path = os.path.join(folder_path, file)

            open(file_path, "w").close()

            print("   File created:", file)


    print("\n✅ Project structure ready on Desktop!")


if __name__ == "__main__":
    create_project()
