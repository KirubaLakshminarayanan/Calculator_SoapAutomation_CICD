<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <!-- Define template to match the root element -->
    <xsl:template match="/testsuite">
        <html>
            <head>
                <title>Test Report</title>
                <style>
                    body { font-family: Arial, sans-serif; }
                    table { width: 100%; border-collapse: collapse; }
                    th, td { border: 1px solid #ddd; padding: 8px; }
                    th { background-color: #f4f4f4; }
                    .pass { color: green; }
                    .fail { color: red; }
                </style>
            </head>
            <body>
                <h1>Test Report</h1>
                <table>
                    <tr>
                        <th>Status</th>
                        <th>Name</th>
                        <th>Time</th>
                        <th>Details</th>
                    </tr>
                    <!-- Iterate through each testcase -->
                    <xsl:for-each select="testcase">
                        <tr>
                            <!-- Display test case status -->
                            <td class="{if (failure) then 'fail' else 'pass'}">
                                <xsl:value-of select="if (failure) then 'Failed' else 'Passed'"/>
                            </td>
                            <!-- Display test case name -->
                            <td><xsl:value-of select="@name"/></td>
                            <!-- Display test case time -->
                            <td><xsl:value-of select="@time"/></td>
                            <!-- Display test case details, if available -->
                            <td>
                                <xsl:choose>
                                    <xsl:when test="failure">
                                        <xsl:value-of select="failure"/>
                                    </xsl:when>
                                    <xsl:otherwise>
                                        <xsl:text>No details available</xsl:text>
                                    </xsl:otherwise>
                                </xsl:choose>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
