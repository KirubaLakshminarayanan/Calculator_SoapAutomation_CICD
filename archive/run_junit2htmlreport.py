import xml.etree.ElementTree as ET
import sys

def convert_junit_to_html(xml_file_path, html_file_path):
    """
    Convert a JUnit XML report to an HTML report.

    :param xml_file_path: Path to the JUnit XML file.
    :param html_file_path: Path where the HTML report will be saved.
    """
    try:
        # Parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # Create an HTML file
        with open(html_file_path, 'w') as html_file:
            html_file.write('<html><head><title>JUnit Report</title></head><body>\n')
            html_file.write('<h1>JUnit Report</h1>\n')
            
            for testcase in root.findall(".//testcase"):
                name = testcase.get('name')
                classname = testcase.get('classname')
                result = 'Passed'
                if testcase.find('failure') is not None:
                    result = 'Failed'
                html_file.write(f'<h2>{classname} - {name}</h2>\n')
                html_file.write(f'<p>Result: {result}</p>\n')

            html_file.write('</body></html>\n')

        print(f"HTML report successfully created: {html_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python run_junit2htmlreport.py <path_to_junit_xml> <path_to_output_html>")
        sys.exit(1)

    # Get file paths from command line arguments
    xml_file_path = sys.argv[1]
    html_file_path = sys.argv[2]

    # Convert JUnit XML to HTML
    convert_junit_to_html(xml_file_path, html_file_path)
