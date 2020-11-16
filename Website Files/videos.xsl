<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="UTF-8"/>
<xsl:template match="/">
  <link rel="stylesheet" type="text/css" href="videos.css"/>
<html>
<head>

</head>
<div class="topnav">
  <a class="active" href="index.html">Home</a>
  <a href="#about">About</a>
</div>
<body>
  <h1>All Informational Videos</h1>
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
                  <TD width="10%">
                    <a href="{link}">Video Link
                    </a>
                  </TD>
            </TR>
            </xsl:for-each>
  </TBODY>
</table>

<h1>Python Videos</h1>
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
          <xsl:if test = "@category = 'python programming'">
             <TR>
                  <TD width="35%"><xsl:value-of select="title" /></TD>
                  <TD width="15%"><xsl:value-of select="author" /></TD>
                  <TD width="10%"><xsl:value-of select="upload-date" /></TD>
                  <TD width="10%">
                    <a href="{link}">Video Link
                    </a>
                  </TD>
            </TR>
          </xsl:if>
            </xsl:for-each>
  </TBODY>
</table>

<h1>General Trading Videos</h1>
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
          <xsl:if test = "@category = 'general trading'">
             <TR>
                  <TD width="35%"><xsl:value-of select="title" /></TD>
                  <TD width="15%"><xsl:value-of select="author" /></TD>
                  <TD width="10%"><xsl:value-of select="upload-date" /></TD>
                  <TD width="10%">
                    <a href="{link}">Video Link
                    </a>
                  </TD>
            </TR>
          </xsl:if>
            </xsl:for-each>
  </TBODY>
</table>

<h1>Simple Moving Average Videos</h1>
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
          <xsl:if test = "@category = 'simple moving average information'">
             <TR>
                  <TD width="35%"><xsl:value-of select="title" /></TD>
                  <TD width="15%"><xsl:value-of select="author" /></TD>
                  <TD width="10%"><xsl:value-of select="upload-date" /></TD>
                  <TD width="10%">
                    <a href="{link}">Video Link
                    </a>
                  </TD>
            </TR>
          </xsl:if>
            </xsl:for-each>
  </TBODY>
</table>

</body>
</html>
</xsl:template>
</xsl:stylesheet>
