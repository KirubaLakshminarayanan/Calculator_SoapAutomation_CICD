<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <!-- Define the root template -->
    <xsl:template match="/">
        <html>
            <head>
                <title>Test Report</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 20px; }
                    table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
                    th, td { border: 1px solid #ddd; padding: 8px; }
                    th { background-color: #4CAF50; color: white; text-align: left; }
                    tr:nth-child(even) { background-color: #f2f2f2; }
                    tr:hover { background-color: #e2e2e2; }
                    .status-passed { color: green; }
                    .status-failed { color: red; }
                    .status-unknown { color: orange; }
                    .summary { margin-top: 20px; padding: 10px; border: 1px solid #ddd; }
                    .summary h2 { margin-top: 0; }
                </style>
            </head>
            <body>
                <h1>Test Report</h1>
                
                <!-- Display test suite details -->
                <xsl:for-each select="//testsuite">
                    <h2>Test Suite: <xsl:value-of select="@name" /></h2>
                    
                    <!-- Display properties -->
                    <h3>Properties</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Property Name</th>
                                <th>Value</th>
                            </tr>
                        </thead>
                        <tbody>
                            <xsl:for-each select="properties/property">
                                <tr>
                                    <td><xsl:value-of select="@name" /></td>
                                    <td><xsl:value-of select="@value" /></td>
                                </tr>
                            </xsl:for-each>
                        </tbody>
                    </table>
                    
                    <!-- Display test cases -->
                    <h3>Test Cases</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <xsl:if test="testcase[@classname]"> <th>Classname</th> </xsl:if>
                                <th>Time</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <xsl:for-each select="testcase">
                                <tr>
                                    <td><xsl:value-of select="@name" /></td>
                                    <xsl:if test="@classname">
                                        <td><xsl:value-of select="@classname" /></td>
                                    </xsl:if>
                                    <td><xsl:value-of select="@time" /></td>
                                    <xsl:variable name="statusClass">
                                        <xsl:choose>
                                            <xsl:when test="failure or error">status-failed</xsl:when>
                                            <xsl:otherwise>status-passed</xsl:otherwise>
                                        </xsl:choose>
                                    </xsl:variable>
                                    <td class="{$statusClass}">
                                        <xsl:choose>
                                            <xsl:when test="not(failure) and not(error)">Passed</xsl:when>
                                            <xsl:when test="failure">
                                                Failed
                                                <xsl:if test="failure">
                                                    <br /><strong>Reason:</strong> <xsl:value-of select="failure/@message" />
                                                </xsl:if>
                                            </xsl:when>
                                            <xsl:otherwise>Unknown</xsl:otherwise>
                                        </xsl:choose>
                                    </td>
                                </tr>
                            </xsl:for-each>
                        </tbody>
                    </table>
                </xsl:for-each>

                <!-- Display summary -->
                <div class="summary">
                    <h2>Summary</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Total Tests</th>
                                <th>Passed</th>
                                <th>Failed</th>
                                <th>Unknown</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><xsl:value-of select="count(//testcase)" /></td>
                                <td><xsl:value-of select="count(//testcase[not(failure) and not(error)])" /></td>
                                <td><xsl:value-of select="count(//testcase[failure or error])" /></td>
                                <td><xsl:value-of select="count(//testcase[not(failure) and not(error) and not(@classname)])" /></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                
                <!-- Report generation details -->
                <div class="summary">
                    <h2>Report Details</h2>
                    <p>Report generated on: <xsl:value-of select="current-dateTime()" /></p>
                </div>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
