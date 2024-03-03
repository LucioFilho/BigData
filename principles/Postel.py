# Postel's Law (Robustness Principle):
'''
Jon Postel's law states that one should:
- be conservative in what you do, 
- be liberal in what you accept from others,
which encourages developers to design systems that accept a wide range of inputs but produce 
a narrow range of outputs.
'''

'''
Postel's Law, also known as the Robustness Principle, was formulated by Jon Postel 
in the context of TCP/IP network protocol design. It states: 
"Be conservative in what you do, be liberal in what you accept from others." 
This principle guides the development of systems that are more resilient and interoperable 
y suggesting that software should be strict about its own outputs but flexible 
in handling inputs received from other systems. 
Here are examples illustrating the application of Postel's Law in various contexts:
'''

# API Development:
'''
Application: When developing an API, ensure it accepts various data formats 
for inputs (e.g., dates in "YYYY-MM-DD" or "DD/MM/YYYY" formats) while always returning 
data in a consistent, well-documented format.
'''
def process_date_input(date_str):
    # Accepts date in different formats and parses it
    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError("Invalid date format")

# Web Form Processing
'''
Application: A web form that accepts telephone numbers should be able to process and store 
them in a standardized format, even if users enter the number with varying formats 
(e.g., with country codes, spaces, or dashes).
'''
def normalize_phone_number(phone_number):
    # Remove spaces, dashes, and parentheses
    normalized_number = re.sub(r"[ \-()]", "", phone_number)
    # Ensure standard format
    if not normalized_number.startswith("+"):
        normalized_number = "+1" + normalized_number  # Assuming default country code
    return normalized_number

# Configuration File Readers:
'''
Application: Software that reads configuration files should be tolerant of common variations, 
such as different types of line endings, extra whitespace, or comments, 
ensuring that the software functions correctly across different environments and editing tools.
'''
def read_config(file_path):
    config = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("#") or not line:  # Skip comments and empty lines
                continue
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()
    return config

# Data Parsing Libraries:
'''
Application: Libraries that parse CSV files could be designed to automatically detect and handle 
different delimiters (e.g., commas, semicolons), quote characters, and line endings,
making the library useful in a wider range of scenarios without requiring pre-configuration.
'''
import csv

def parse_csv_auto_delimiter(file_path):
    with open(file_path, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        for row in reader:
            # Process each row

# Network Protocols Implementation:
'''Application: Implementations of network protocols can accept packets or messages that slightly 
deviate from the standard (e.g., unexpected order of headers, additional unknown headers) 
as long as the essential information is intact and understandable, while always sending out 
strictly standard-compliant messages.
'''

# General Guideline:
'''
The essence of Postel's Law is to build systems that are robust and interoperable, 
reducing the chance of failures due to minor deviations or incompatibilities. 
By designing software that can gracefully handle a variety of inputs, 
developers can create more user-friendly and resilient applications. 
However, it's important to balance this flexibility with the need for security 
and validation to avoid introducing vulnerabilities.
'''
