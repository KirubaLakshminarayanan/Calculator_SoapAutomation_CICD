<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <!-- Define the output format -->
    <xsl:output method="html" indent="yes"/>

    <!-- Template to match the root element -->
    <xsl:template match="/">
        <html>
        <head>
            <title>SoapUI Test Report</title>
        </head>
        <body>
            <h1>SoapUI Test Report</h1>
            <table border="1">
                <tr>
                    <th>TestCase</th>
                    <th>Status</th>
                    <th>Time</th>
                </tr>
                <!-- Loop through each TestCase -->
                <xsl:for-each select="//testCase">
                    <tr>
                        <td><xsl:value-of select="@name"/></td>
                        <td><xsl:value-of select="@status"/></td>
                        <td><xsl:value-of select="@time"/></td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
