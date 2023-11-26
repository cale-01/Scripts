import os
from prettytable import PrettyTable
from heapq import nlargest

def get_size(path, inaccessible):
    total = 0
    num_files = 0
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
                    num_files += 1
                elif entry.is_dir():
                    dir_size, dir_num_files = get_size(entry.path, inaccessible)
                    total += dir_size
                    num_files += dir_num_files
    except PermissionError:
        inaccessible.append(path)  # Add inaccessible path to the list
    return total, num_files

def display_sizes(directory, all_files, inaccessible):
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        try:
            if os.path.isfile(path):
                size = os.path.getsize(path)
                all_files.append((size, 1, path))
            else:
                size, num_files = get_size(path, inaccessible)
                all_files.append((size, num_files, path))
                display_sizes(path, all_files, inaccessible)
        except PermissionError:
            inaccessible.append(path)  # Add inaccessible path to the list

def main():
    directory = r"C:\Users"  # Replace with your directory
    all_files = []
    inaccessible = []
    display_sizes(directory, all_files, inaccessible)
    
    # Get the top 20 largest files/directories
    largest_files = nlargest(20, all_files)

    # Display inaccessible files/directories
    if inaccessible:
        inaccessible.sort()  # Sort in alphabetical order
        print("\nInaccessible Files/Directories:")
        table = PrettyTable()
        table.field_names = ["File/Directory Path"]
        for path in inaccessible:
            table.add_row([path])
        print(table)
        
    # Display the results
    table = PrettyTable()
    table.field_names = ["Rank", "File Path", "Size (bytes)", "Size (GB)", "Number of Files"]
    for i, (size, num_files, path) in enumerate(largest_files, start=1):
        size_gb = round(size / (1024 ** 3), 2)  # Convert size to GB
        table.add_row([i, path, size, f'({size_gb} GB)', num_files])
    print(table)


if __name__ == "__main__":
    main()
