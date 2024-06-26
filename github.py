import os
import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: {stderr.decode('utf-8')}")
    else:
        print(stdout.decode('utf-8'))

def convert_folder_to_git(folder_path, remote_url=None, token=None):
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Change to the target directory
    os.chdir(folder_path)
    
    # Initialize the Git repository
    run_command("git init")

    # Add all files to the repository
    run_command("git add .")

    # Commit the files
    run_command('git commit -m "Initial commit"')

    # Add remote repository if provided
    if remote_url and token:
        # Parse the remote_url to include the token
        auth_remote_url = remote_url.replace("https://", f"https://{token}@")
        run_command(f"git remote add origin {auth_remote_url}")
        run_command("git push -u origin master")
    elif remote_url:
        run_command(f"git remote add origin {remote_url}")
        run_command("git push -u origin master")

if __name__ == "__main__":
    # Tentukan path folder, URL remote repository, dan token di sini
    folder_path = "/home/yoan/TUGASAKHIR"
    remote_url = "https://github.com/joenav23/TUGASAKHIR.git"
    token = "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"  # Ganti dengan personal access token yang sesuai
    
    convert_folder_to_git(folder_path, remote_url, token)
