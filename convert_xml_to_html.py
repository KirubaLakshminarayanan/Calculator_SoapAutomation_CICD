import logging
from lxml import etree
import os
from datetime import datetime

# Function to generate timestamped filename
def timestamped_filename(base_path, extension):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_path}_{timestamp}.{extension}"

# Function to get the most recent XML file
def get_most_recent_file(directory, extension):
    files = [f for f in os.listdir(directory) if f.endswith(f".{extension}")]
    if not files:
        raise FileNotFoundError(f"No files with extension {extension} found in {directory}")
    
    # Get full paths and sort by modification time
    full_paths = [os.path.join(directory, f) for f in files]
    most_recent_file = max(full_paths, key=os.path.getmtime)
    return most_recent_file

# Configure logging
log_filename = timestamped_filename('C:\\Users\\LKiruba\\Desktop\\SoapUI_Automation_CICD\\Log\\transform', 'log')
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def transform_xml_to_html(xml_file, xslt_file, html_file):
    try:
        # Check if files exist
        if not os.path.exists(xml_file):
            raise FileNotFoundError(f"XML file not found: {xml_file}")
        if not os.path.exists(xslt_file):
            raise FileNotFoundError(f"XSLT file not found: {xslt_file}")

        # Load XML and XSLT
        logging.info(f"Loading XML file: {xml_file}")
        xml = etree.parse(xml_file)
        logging.info(f"Loading XSLT file: {xslt_file}")
        xslt = etree.parse(xslt_file)
        transform = etree.XSLT(xslt)
        
        # Transform XML to HTML
        logging.info("Starting XML to HTML transformation")
        html = transform(xml)
        
        # Save the HTML to a file
        logging.info(f"Saving HTML file: {html_file}")
        with open(html_file, 'wb') as f:
            f.write(etree.tostring(html, pretty_print=True))
        logging.info("Transformation completed successfully")

    except etree.XMLSyntaxError as e:
        logging.error(f"XML syntax error: {e}")
    except etree.XSLTParseError as e:
        logging.error(f"XSLT parse error: {e}")
    except FileNotFoundError as e:
        logging.error(e)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Paths to directories
xml_directory = 'C:\\Users\\LKiruba\\Desktop\\SoapUI_Automation_CICD\\Reports\\XML'
xslt_file = 'C:\\Users\\LKiruba\\Desktop\\SoapUI_Automation_CICD\\report-transform.xslt'

# Get the most recent XML file
xml_file = get_most_recent_file(xml_directory, 'xml')
html_file = timestamped_filename('C:\\Users\\LKiruba\\Desktop\\SoapUI_Automation_CICD\\Reports\\HTML\\TEST-CalculatorTestSuite', 'html')

# Execute the transformation
transform_xml_to_html(xml_file, xslt_file, html_file)
