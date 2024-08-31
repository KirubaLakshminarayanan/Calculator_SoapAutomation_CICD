import os
import lxml.etree as ET

def convert_xml_to_html(xml_file, xslt_content, output_file):
    # Parse the XML file
    try:
        xml_tree = ET.parse(xml_file)
    except ET.XMLSyntaxError as e:
        print(f"Error parsing XML file: {e}")
        return

    # Load XSLT content
    try:
        xslt_tree = ET.XML(xslt_content)
        transform = ET.XSLT(xslt_tree)
    except ET.XSLTParseError as e:
        print(f"Error parsing XSLT content: {e}")
        return

    # Perform transformation
    try:
        result_tree = transform(xml_tree)
        result_tree.write(output_file, pretty_print=True, method="html")
        print(f"HTML report generated: {output_file}")
    except Exception as e:
        print(f"Error during transformation: {e}")

if __name__ == "__main__":
    # Define paths
    xml_file = 'soapui-reports/TEST-CalculatorTestSuite.xml'
    xslt_content = '''<?xml version="1.0" encoding="UTF-8"?>
    <xsl:stylesheet version="1.0"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="/">
            <html>
                <body>
                    <h2>Test Report</h2>
                    <table border="1">
                        <tr>
                            <th>Test Case</th>
                            <th>Status</th>
                        </tr>
                        <xsl:for-each select="//testCase">
                            <tr>
                                <td><xsl:value-of select="name"/></td>
                                <td><xsl:value-of select="status"/></td>
                            </tr>
                        </xsl:for-each>
                    </table>
                </body>
            </html>
        </xsl:stylesheet>'''

    output_file = 'soapui-reports/report.html'

    # Perform the conversion
    convert_xml_to_html(xml_file, xslt_content, output_file)
