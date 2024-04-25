import re
from pdfminer.high_level import extract_text



# Function to extract awards and achievements
def extract_awards_and_achievements(data):
    is_req_head = False
    content = []

    # Iterate through the lines in the extracted text
    for line in data.split('\n'):
        # Check if the line matches the pattern
        if line.isspace():
            continue

        heading_pattern = re.compile(r'^(Awards|Certifications)')
        heading_not_pattern = re.compile(r'^(Education|Profile|Employ|Experience|Hobbies|Projects|Academic|Extra Curricular|Environment|Skills|Roles)')

        if heading_not_pattern.match(line):
            if is_req_head:
                is_req_head=False

        if heading_pattern.match(line):
            #print(line)
            is_req_head=True
        
        if is_req_head:
            content.append(line+'\n')

    return content