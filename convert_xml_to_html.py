import logging
from lxml import etree
import os
from datetime import datetime

# Function to generate timestamped filename
def timestamped_filename(base_path, extension):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_path}_{timestamp}.{extension}"

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

# Generate timestamped paths for XML and HTML files
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
xml_file = f'C:\\Reports\\SoapUI_CICD_Calculator\\XML\\TEST-CalculatorTestSuite_{timestamp}.xml'
xslt_file = 'C:\\Users\\LKiruba\\Desktop\\SoapUI_Automation_CICD\\report-transform.xslt'
html_file = f'C:\\Reports\\SoapUI_CICD_Calculator\\HTML\\TEST-CalculatorTestSuite_{timestamp}.html'

# Execute the transformation
transform_xml_to_html(xml_file, xslt_file, html_file)
