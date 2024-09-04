import logging
import shutil
import os
from lxml import etree
from datetime import datetime

# Function to generate timestamped filename
def timestamped_filename(base_path, extension):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_path}_{timestamp}.{extension}"

# Function to back up XML file
def backup_xml_file(source_file, backup_dir):
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Source XML file not found: {source_file}")
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_file = timestamped_filename(os.path.join(backup_dir, 'TEST-CalculatorTestSuite_backup'), 'xml')
    shutil.copy2(source_file, backup_file)
    logging.info(f"Backup created: {backup_file}")

# Hardcoded paths
xml_file = 'C:\\Reports\\SoapUI_CICD_Calculator\\XML\\TEST-CalculatorTestSuite.xml'
html_dir = 'C:\\Reports\\SoapUI_CICD_Calculator\\HTML'
xslt_file = 'C:\\Users\\LKiruba\\Desktop\\SoapUI_Automation_CICD\\report-transform.xslt'
log_dir = 'C:\\Reports\\SoapUI_CICD_Calculator\\Log'
backup_dir = 'C:\\Reports\\SoapUI_CICD_Calculator\\Backup'

# Generate a timestamped log filename
log_filename = timestamped_filename(os.path.join(log_dir, 'transform'), 'log')

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

# Backup the XML file
backup_xml_file(xml_file, backup_dir)

# Generate a corresponding HTML file name
html_file = timestamped_filename(os.path.join(html_dir, 'TEST-CalculatorTestSuite'), 'html')

# Execute the transformation
transform_xml_to_html(xml_file, xslt_file, html_file)
