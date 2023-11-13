def format_title(title):
    # Replace certain symbols with words or remove them
    title = title.replace('&', 'and').replace('#', 'number').replace('%','').replace(':','').replace('!','').replace('?','')
    # Remove additional unwanted characters if necessary
    return title


def create_files_from_input_old(C):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i in range(0, len(lines), 3):
        class_number = lines[i].strip()
        class_info = lines[i + 1].strip()

        # Extract date for filename
        date_part = class_info.split(' ')[-5]
        date_for_filename = date_part.replace('-', '')

        # Format the title part of the filename
        title_part = format_title(' '.join(class_info.split(' ')[:-4]))

        # Replace spaces with underscores and other special characters if needed
        title_for_filename = title_part.replace(' ', '_').replace('(', '').replace(')', '')

        # Prepare file name and content
        file_name = f"{date_for_filename}_{class_number}강_{title_for_filename}.md"
        file_content = f"{class_number}. {class_info}\n"

        # Write to a file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(file_content)
        print(f"Created file: {file_name}")


import re

# Define the regular expression pattern for parsing the input
pattern = re.compile(
    r'(?P<lecture_number>\d+)\n'  # Lecture number
    r'(?P<title>.+?) '  # Title (non-greedy to stop at first space after title)
    r'(?P<date>\d{4}-\d{2}-\d{2})'  # Date (YYYY-MM-DD)
    r'\((?P<day_of_week>.+?)\)'  # Day of the week (inside parentheses)
    r' (?P<time>\d{2}:\d{2}~\d{2}:\d{2})'  # Time (HH:MM~HH:MM)
    r' (?P<online_offline>\d+\((온|오프)\))',  # Online or offline indicator
    re.MULTILINE
)

def create_files_from_input(input_text):
    # Find all matches in the input text
    matches = pattern.finditer(input_text)

    for match in matches:
        # Extract components from the match object
        lecture_number = match.group('lecture_number')
        title = match.group('title')
        date = match.group('date')
        day = match.group('day_of_week')

        # Prepare file name and content
        mod_title = title.replace(' ', '_')
        mod_date = date.replace('-', '')

        file_name = f"{date}_{lecture_number}강_{format_title(mod_title)}.md"
        file_content = f"\n-[ ] 정리 : {date}({day}) {lecture_number}강. {title}\n\n"

        # Write to a file
        print(f"Writing to file: {file_name}")
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(file_content)


# Replace '/path/to/your/input.txt' with the actual path to your input file
input_file_path = 'input.txt'
# Read the contents of the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()
# Call the function with the actual path to process the files
    create_files_from_input(input_text)

