<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"> 
<xsl:output method="text" version="1.0" encoding="UTF-8" indent="no" omit-xml-declaration="yes"/>
<xsl:template match="site">
<xsl:for-each select="link">
<xsl:value-of select="status"/>
<xsl:text> </xsl:text>
<xsl:value-of select="check"/>
<xsl:text> </xsl:text>
<xsl:value-of select="url"/>
<xsl:text>&#10;</xsl:text>
</xsl:for-each>
</xsl:template> 
</xsl:stylesheet>
