import os
import subprocess
import sys

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # --- MODIFIED ---
    # Define the base saves folder path relative to this script
    # This is more portable than using ../saves
    base_saves_folder = os.path.join(script_dir, "saves")
    # --- END MODIFIED ---
    
    # Define other paths relative to the script
    posts_path = os.path.join(script_dir, "posts.txt")
    processed_path = os.path.join(script_dir, "processed.txt")
    config_path = os.path.join(script_dir, "gallery-dl.conf")

    # Check for config file
    if not os.path.exists(config_path):
        print(f"Error: gallery-dl.conf not found at {config_path}")
        return

    # Ensure the base saves folder exists
    if not os.path.exists(base_saves_folder):
        print(f"Creating base saves folder at: {base_saves_folder}")
        os.makedirs(base_saves_folder)
        
    # Read URLs from posts.txt
    try:
        with open(posts_path, "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"posts.txt not found at {posts_path}")
        print("Please create it and add the URLs you want to download.")
        open(posts_path, 'a').close()
        return

    if not urls:
        print("posts.txt is empty. Nothing to download.")
        return

    # Build the single gallery-dl command
    cmd = [
        "gallery-dl",
        "--config", config_path,
        "-d", base_saves_folder  # <-- This sets the root save path
    ] + urls

    print(f"Found {len(urls)} URLs. Starting gallery-dl...")
    print(f"Saving to base directory: {base_saves_folder}")

    try:
        # Run the command
        result = subprocess.run(cmd, check=False)

        # Check if the command was successful
        if result.returncode == 0:
            print(f"Download complete. Moving {len(urls)} URLs to processed.txt.")
            
            # Archive successfully processed URLs
            try:
                with open(processed_path, "a", encoding="utf-8") as pf:
                    for url in urls:
                        pf.write(url + "\n")
                
                # Clear posts.txt
                with open(posts_path, "w", encoding="utf-8") as pf:
                    pf.write("")
                print("posts.txt has been cleared.")
                
            except IOError as e:
                print(f"Error archiving URLs: {e}")
                print("Please check file permissions for processed.txt.")

        else:
            print(f"gallery-dl finished with an error (code: {result.returncode}).")
            print("posts.txt was *not* modified. You can re-run the script to try again.")

    except FileNotFoundError:
        print("\n--- ERROR ---")
        print("Command 'gallery-dl' not found.")
        print("Please ensure gallery-dl is installed and accessible in your system's PATH.")
        print("-------------")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()