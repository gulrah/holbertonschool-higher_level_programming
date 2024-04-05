#!/usr/bin/python3
import sys
from collections import defaultdict

# Initialize variables to keep track of metrics
total_file_size = 0
status_counts = defaultdict(int)

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            # Split the line by spaces to extract necessary information
            parts = line.strip().split()
            status_code = parts[-2]
            file_size = int(parts[-1])
            
            # Update metrics
            total_file_size += file_size
            status_counts[status_code] += 1
            
            # Print statistics every 10 lines
            if i % 10 == 0:
                print("File size: {}".format(total_file_size))
                for code in sorted(status_counts.keys()):
                    print("{}: {}".format(code, status_counts[code]))
                print()
                
        except (IndexError, ValueError):
            # Ignore lines that do not match the expected format
            pass

except KeyboardInterrupt:
    # Print statistics when interrupted by KeyboardInterrupt (CTRL + C)
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))
