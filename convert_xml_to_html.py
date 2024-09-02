import logging
from lxml import etree
import os
from datetime import datetime

# Function to generate timestamped filename
def timestamped_filename(base_path, extension):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_path}_{timestamp}.{extension}"

# Function to get the latest directory from a base directory
def get_latest_directory(base_directory):
    dirs = [d for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]
    if not dirs:
        raise FileNotFoundError(f"No directories found in {base_directory}")
    latest_dir = max(dirs, key=lambda d: os.path.getmtime(os.path.join(base_directory, d)))
    return os.path.join(base_directory, latest_dir)

# Function to get the latest file from a directory
def get_latest_file(directory, extension):
    files = [f for f in os.listdir(directory) if f.endswith(f'.{extension}')]
    if not files:
        raise FileNotFoundError(f"No files with extension .{extension} found in {directory}")
    latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
    return os.path.join(directory, latest_file)

# Generate a timestamped log filename
log_filename = timestamped_filename('C:\\Reports\\SoapUI_CICD_Calculator\\Log\\transform', 'log')

# Configure logging
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
xml_base_dir = 'C:\\Reports\\SoapUI_CICD_Calculator\\XML'
html_dir = 'C:\\Reports\\SoapUI_CICD_Calculator\\HTML'
xslt_file = 'C:\\Users\\LKiruba\\Desktop\\SoapUI_Automation_CICD\\report-transform.xslt'

# Get the latest directory and file
latest_xml_dir = get_latest_directory(xml_base_dir)
xml_file = get_latest_file(latest_xml_dir, 'xml')

# Generate a corresponding HTML file name
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
html_file = f'{html_dir}\\TEST-CalculatorTestSuite_{timestamp}.html'

# Execute the transformation
transform_xml_to_html(xml_file, xslt_file, html_file)
