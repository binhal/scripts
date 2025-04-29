#!/usr/bin/env python3
"""
Time-Based ID Generator
Generates a time-based ID in the format YYYYMMDDHHMM
"""

import argparse
import datetime
import sys


def generate_time_id(date_time=None):
    """
    Generate a time-based ID in the format YYYYMMDDHHMM

    Args:
        date_time: Optional datetime object or string. If None, uses current time.

    Returns:
        String time ID in the format YYYYMMDDHHMM
    """
    if date_time is None:
        # Use current time
        now = datetime.datetime.now()
    elif isinstance(date_time, str):
        # Parse string date/time
        try:
            now = datetime.datetime.fromisoformat(date_time)
        except ValueError:
            try:
                # Try with more flexible parsing
                formats = [
                    "%Y-%m-%d %H:%M:%S",
                    "%Y-%m-%d %H:%M",
                    "%Y-%m-%d",
                    "%Y/%m/%d %H:%M:%S",
                    "%Y/%m/%d %H:%M",
                    "%Y/%m/%d",
                    "%d-%m-%Y %H:%M:%S",
                    "%d-%m-%Y %H:%M",
                    "%d-%m-%Y",
                    "%d/%m/%Y %H:%M:%S",
                    "%d/%m/%Y %H:%M",
                    "%d/%m/%Y",
                ]

                for fmt in formats:
                    try:
                        now = datetime.datetime.strptime(date_time, fmt)
                        break
                    except ValueError:
                        continue
                else:
                    raise ValueError(f"Could not parse date: {date_time}")
            except Exception as e:
                raise ValueError(f"Invalid date format: {date_time}. Error: {str(e)}")
    else:
        now = date_time

    # Format the time ID
    time_id = now.strftime("%Y%m%d%H%M")
    return time_id


def main():
    parser = argparse.ArgumentParser(description="Generate a time-based ID")
    parser.add_argument(
        "--date",
        "-d",
        type=str,
        help="Date and time (ISO format or YYYY-MM-DD HH:MM:SS)",
    )
    parser.add_argument(
        "--now", "-n", action="store_true", help="Use current time (default)"
    )
    parser.add_argument(
        "--interactive", "-i", action="store_true", help="Run in interactive mode"
    )

    args = parser.parse_args()

    if args.interactive:
        print("Time-Based ID Generator")
        print("======================")
        print("1. Generate ID for current time")
        print("2. Generate ID for custom date/time")
        choice = input("Choose an option (1-2): ")

        if choice == "1":
            time_id = generate_time_id()
            print(f"\nTime ID: {time_id}")
        elif choice == "2":
            date_str = input(
                "Enter date and time (YYYY-MM-DD HH:MM:SS or YYYY-MM-DD): "
            )
            try:
                time_id = generate_time_id(date_str)
                print(f"\nTime ID: {time_id}")
            except ValueError as e:
                print(f"Error: {str(e)}")
        else:
            print("Invalid choice")
    else:
        try:
            if args.date:
                time_id = generate_time_id(args.date)
            else:
                time_id = generate_time_id()

            print(time_id)
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
