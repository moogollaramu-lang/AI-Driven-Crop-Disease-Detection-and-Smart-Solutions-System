import os
import hashlib
import sys
from dotenv import load_dotenv
from github import Github
from github.GithubException import UnknownObjectException, GithubException

# Load environment variables from .env file
load_dotenv()

REPO_NAME = "moogollaramu-lang/AI-Driven-Crop-Disease-Detection-and-Smart-Solutions-System"
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define ignored patterns (equivalent to .gitignore)
IGNORED_PATTERNS = [
    ".git",
    "__pycache__",
    "plantvillage.zip",
    "PlantVillage-Dataset-master",
    "dog.jpg",
    "human.jpg",
    "leaf.jpg",
    ".env",
    "upload_to_github.py",
]

def should_ignore(path):
    parts = path.split(os.sep)
    for part in parts:
        if part in IGNORED_PATTERNS:
            return True
        if part.endswith(".pyc") or part.endswith(".pyo") or part.endswith(".pyd"):
            return True
    return False

def calculate_git_sha(content_bytes):
    """Calculate the Git blob SHA-1 of a file's contents."""
    header = f"blob {len(content_bytes)}\0".encode('utf-8')
    sha = hashlib.sha1()
    sha.update(header)
    sha.update(content_bytes)
    return sha.hexdigest()

def get_all_local_files():
    local_files = {}
    for root, dirs, files in os.walk(PROJECT_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, PROJECT_DIR)
            if not should_ignore(rel_path):
                local_files[rel_path.replace(os.sep, "/")] = full_path
    return local_files

def main():
    print(">>> Starting Crop Disease App GitHub Sync Automation...")
    
    # Get GITHUB_TOKEN from env or user input
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("[WARNING] GITHUB_TOKEN not found in environment or .env file.")
        token = input("Please enter your GitHub Personal Access Token (PAT): ").strip()
        if not token:
            print("[ERROR] GitHub PAT is required to upload files.")
            sys.exit(1)

    g = Github(token)
    
    try:
        print(f"[INFO] Connecting to GitHub repository: {REPO_NAME}...")
        repo = g.get_repo(REPO_NAME)
        print(f"[SUCCESS] Connected to repository: {repo.full_name}")
    except Exception as e:
        print(f"[ERROR] Failed to connect to repository: {e}")
        print("Please check your token permissions and make sure the repository exists and you have write access.")
        sys.exit(1)

    local_files = get_all_local_files()
    print(f"[INFO] Found {len(local_files)} files to upload (excluding ignored files).")

    for rel_path, local_path in local_files.items():
        print(f"\n--------------------------------------------------")
        print(f"[PROCESS] Processing: {rel_path} ...")
        
        # Read local file
        try:
            with open(local_path, "rb") as f:
                content = f.read()
        except Exception as e:
            print(f"[ERROR] Reading local file {local_path}: {e}")
            continue

        local_sha = calculate_git_sha(content)
        
        # Check if file exists on remote
        remote_sha = None
        remote_file = None
        try:
            remote_file = repo.get_contents(rel_path)
            remote_sha = remote_file.sha
        except UnknownObjectException:
            # File doesn't exist
            pass
        except GithubException as e:
            # Check if this is an empty repository error (404 empty)
            if e.status == 404 and "empty" in str(e).lower():
                # Repository is empty, treat as file doesn't exist
                pass
            else:
                print(f"[WARNING] GitHub Exception checking remote file {rel_path}: {e}")
                continue
        except Exception as e:
            print(f"[WARNING] Error checking remote file {rel_path}: {e}")
            continue

        if remote_sha == local_sha:
            print(f"[INFO] File is up-to-date on GitHub. Skipping.")
            continue

        commit_message = f"Sync: {'Update' if remote_file else 'Create'} {rel_path} via Automation"
        
        try:
            if remote_file:
                print(f"[INFO] Updating file on GitHub (size: {len(content)/1024:.1f} KB)...")
                repo.update_file(
                    path=rel_path,
                    message=commit_message,
                    content=content,
                    sha=remote_file.sha
                )
                print(f"[SUCCESS] Successfully updated {rel_path}!")
            else:
                print(f"[INFO] Creating file on GitHub (size: {len(content)/1024:.1f} KB)...")
                repo.create_file(
                    path=rel_path,
                    message=commit_message,
                    content=content
                )
                print(f"[SUCCESS] Successfully created {rel_path}!")
        except Exception as e:
            print(f"[ERROR] Failed to write {rel_path} to GitHub: {e}")
            print("Please ensure your token has adequate permissions (contents:write).")
            continue

    print(f"\n==================================================")
    print("[SUCCESS] All files synced to GitHub successfully!")
    print(f"Repository: https://github.com/{REPO_NAME}")
    print("==================================================")

if __name__ == "__main__":
    main()
