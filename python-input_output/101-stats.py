#!/usr/bin/python3
import sys

"""
Script that reads lines from standard input (stdin), computes metrics about file sizes and status codes,
and prints them every 10 lines and after a keyboard interrupt (CTRL+C).

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
  """Prints the current statistics."""
  global total_size, status_counts
  print(f"Total file size: {total_size}")
  for code, count in sorted(status_counts.items()):
    if count > 0:
      print(f"{code}: {count}")


try:
  for line in sys.stdin:
    # Extract data from the line (handle potential errors)
    try:
      ip, date, _, _, status_code, file_size = line.strip().split()
      total_size += int(file_size)
      status_counts[int(status_code)] += 1
      line_count += 1
    except (ValueError, IndexError):
      print(f"Error parsing line: {line.strip()}", file=sys.stderr)

    # Print stats every 10 lines
    if line_count % 10 == 0:
      print_stats()
      total_size = 0
      status_counts = {code: 0 for code in status_counts}

  # Print stats on keyboard interrupt
except KeyboardInterrupt:
  print_stats()
