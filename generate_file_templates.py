import json
import os
import re

def sanitize_title(title):
    # Remove special characters and punctuation, convert to lowercase
    sanitized = re.sub(r'[^\w\s]', '', title)
    # Replace spaces with underscores and convert to lowercase
    return sanitized.replace(' ', '_').lower()

def create_solution_files():
    # Read the challenges.json file
    with open('challenges.json', 'r') as f:
        data = json.load(f)
    
    # Create solutions directory if it doesn't exist
    os.makedirs('solutions', exist_ok=True)
    
    # Create a solution file for each challenge
    for day, title in data['challenge_titles'].items():
        # Format the day number as two digits
        day_num = f"{int(day):02d}"
        
        # Create the filename
        filename = f"{day_num}_{sanitize_title(title)}.py"
        filepath = os.path.join('solutions', filename)
        
        # Create the file content
        content = f'''"""
This is a solution to day {day} of AoC {data['year']}

Challenge title: {title}
Challenge link : https://adventofcode.com/{data['year']}/day/{day}

Solution: https://github.com/tligorio/advent_of_code_2023/blob/main/solutions/{filename}

Time complexity: O(...)
Space complexity: O(...)

"""

'''
        
        # Write the file
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"Created {filepath}")

if __name__ == "__main__":
    create_solution_files()
