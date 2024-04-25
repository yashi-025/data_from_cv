import re
from pdfminer.high_level import extract_text



# Function to extract awards and achievements
def extract_project(data):

    title=[]
    org=[]
    date=[]
    tech=[]
    desc=[]
    name_pattern = re.compile(r'^(Title|Application)')
    orga_pattern = re.compile(r'^(Client|Organisation)')
    dura_pattern = re.compile(r'(Duration)')
    tech_pattern = re.compile(r'Environment|Technolog')
    date_pattern = re.compile(r'Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December')
    desc_pattern = re.compile(r'(Description)')

    empty_line=False
    is_start=False
    is_tech=False
    is_desc=False

    # Iterate through the lines in the extracted text
    for line in data.split('\n'):
        # Check if the line matches the pattern
        if line.isspace():
            is_tech = False
            if is_desc:
                is_desc = False
                is_start = False
                continue

        if desc_pattern.match(line) and is_start:
            is_tech = False
            is_desc=True

        if tech_pattern.match(line) and is_start:
            is_tech = True



        if is_tech:
            print(line)
            continue
        if is_desc:
            print(line)
            continue

        if name_pattern.match(line):
            print(line)
        if orga_pattern.match(line):
            print(line)
            is_start=True
        if is_start:
            if date_pattern.match(line) or dura_pattern.match(line):
                print(line)