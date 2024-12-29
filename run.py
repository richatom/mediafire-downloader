import subprocess

def main():
    downloadable_link = input("Enter the downloadable link: ")
    output_file_path = input("Enter the output file path: ")
    command = f"python mediafire.py {downloadable_link} -o {output_file_path}"
    
    print(f"Running command: {command}")
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")


if __name__ == "__main__":
    main()