<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="UTF-8"/>
<xsl:template match="/">
<html>
<head><title>Videos</title>
</head>
<body>
  <h1>Our Videos</h1>
<table width="100%" border="1">
  <THEAD>
           <TR>
                <TD width="35%"><B>Title</B></TD>
                <TD width="15%"><B>Author</B></TD>
                <TD width="10%"><B>Upload-Date</B></TD>
                <TD width="10%"><B>Link</B></TD>
          </TR>
   </THEAD>
  <TBODY>
             <xsl:for-each select="videos/video">
             <TR>
                  <TD width="35%"><xsl:value-of select="title" /></TD>
                  <TD width="15%"><xsl:value-of select="author" /></TD>
                  <TD width="10%"><xsl:value-of select="upload-date" /></TD>
                  <TD width="10%"><xsl:value-of select="link" /></TD>
            </TR>
            </xsl:for-each>
  </TBODY>
</table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
