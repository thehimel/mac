#!/usr/bin/env python3
"""
Timestamp Updater - Update creation time and modification time to current time (macOS)

This script updates creation time and modification time for all files and 
directories in a given directory tree to the current time on macOS.

Usage:
    python update_timestamps.py /path/to/your/directory
    python update_timestamps.py ~/Documents/myproject
    python update_timestamps.py .

Examples:
    python update_timestamps.py /home/user/documents
    python update_timestamps.py ~/Documents/myproject
    python update_timestamps.py .  # Current directory
"""
import os
import sys
import subprocess
from datetime import datetime

def set_creation_time_macos(file_path, timestamp):
    """Set creation time on macOS using SetFile command"""
    try:
        # Format date for SetFile command (MM/DD/YYYY HH:MM:SS)
        date_str = datetime.fromtimestamp(timestamp).strftime('%m/%d/%Y %H:%M:%S')
        
        # Use SetFile to change creation date
        result = subprocess.run(['SetFile', '-d', date_str, file_path], 
                              capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            return True
        else:
            print(f"    SetFile error: {result.stderr.strip()}")
            return False
            
    except FileNotFoundError:
        print("    SetFile command not found. Install Xcode Command Line Tools:")
        print("    xcode-select --install")
        return False
    except Exception as e:
        print(f"    SetFile error: {e}")
        return False

def update_timestamps_recursive(directory_path):
    """
    Update creation time and modification time for all files and directories recursively
    
    Usage:
        python update_timestamps.py /path/to/your/directory
        python update_timestamps.py ~/Documents/myproject
        python update_timestamps.py .
    
    Args:
        directory_path (str): Path to the directory to process
    """
    # Validate directory path
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist")
        return False
    
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a directory")
        return False
    
    files_updated = 0
    dirs_updated = 0
    creation_time_updated = 0
    errors = 0
    current_time = datetime.now().timestamp()
    
    print(f"Updating timestamps in: {directory_path}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    # Walk through directory tree
    for root, dirs, files in os.walk(directory_path):
        # Update directory timestamps
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                # Update access and modification time
                os.utime(dir_path, (current_time, current_time))
                dirs_updated += 1
                print(f"✓ DIR:  {dir_path}")
                
                # Update creation time
                if set_creation_time_macos(dir_path, current_time):
                    creation_time_updated += 1
                    print(f"    ✓ Creation time updated")
                    
            except Exception as e:
                errors += 1
                print(f"✗ DIR:  {dir_path} - Error: {e}")
        
        # Update file timestamps
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                # Update access and modification time
                os.utime(file_path, (current_time, current_time))
                files_updated += 1
                print(f"✓ FILE: {file_path}")
                
                # Update creation time
                if set_creation_time_macos(file_path, current_time):
                    creation_time_updated += 1
                    print(f"    ✓ Creation time updated")
                    
            except Exception as e:
                errors += 1
                print(f"✗ FILE: {file_path} - Error: {e}")
    
    # Update the root directory itself
    try:
        os.utime(directory_path, (current_time, current_time))
        dirs_updated += 1
        print(f"✓ DIR:  {directory_path} (root)")
        
        # Update creation time for root directory
        if set_creation_time_macos(directory_path, current_time):
            creation_time_updated += 1
            print(f"    ✓ Creation time updated")
            
    except Exception as e:
        errors += 1
        print(f"✗ DIR:  {directory_path} (root) - Error: {e}")
    
    # Print summary
    print("-" * 50)
    print(f"Summary:")
    print(f"  Files updated: {files_updated}")
    print(f"  Directories updated: {dirs_updated}")
    print(f"  Total updated: {files_updated + dirs_updated}")
    print(f"  Creation times updated: {creation_time_updated}")
    print(f"  Errors: {errors}")
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    return errors == 0

def main():
    """
    Main function to handle command line arguments
    
    Usage:
        python update_timestamps.py /path/to/your/directory
        python update_timestamps.py ~/Documents/myproject
        python update_timestamps.py .
    
    Examples:
        python update_timestamps.py /home/user/documents
        python update_timestamps.py ~/Documents/myproject
        python update_timestamps.py .  # Current directory
    """
    if len(sys.argv) != 2:
        print("Usage: python update_timestamps.py <directory_path>")
        print("Example: python update_timestamps.py /path/to/your/directory")
        print("")
        print("Note: This script uses SetFile command (requires Xcode Command Line Tools)")
        print("Install with: xcode-select --install")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    # Convert relative path to absolute path
    directory_path = os.path.abspath(directory_path)
    
    success = update_timestamps_recursive(directory_path)
    
    if success:
        print("\n✅ All timestamps updated successfully!")
        sys.exit(0)
    else:
        print("\n❌ Some errors occurred during update")
        sys.exit(1)

if __name__ == "__main__":
    main()
    