<?xml version="1.0" encoding="utf-8" ?>

<!--   b) wyswietli dane odczytane z pliku xml posortowane rosnaco-->
<!--     wzgledem pola wiek, a pozniej malejaco wzgledem pola waga.-->

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>Table</title>
            </head>
            <body>
                <h1>Table</h1>
                <table border="1">
                    <tr>
                        <th>Imie</th>
                        <th>Data</th>
                        <th>Wiek</th>
                        <th>Waga</th>
                        <th>Wzrost</th>
                        <th>Krew</th>
                    </tr>
                    <xsl:apply-templates select="dane/osoba">
                        <xsl:sort select="wiek" order="ascending"/>
                        <xsl:sort select="waga" order="descending"/>
                    </xsl:apply-templates>
                </table>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="osoba">
        <tr>
            <td>
                <xsl:value-of select="imie"/>
            </td>
            <td>
                <xsl:value-of select="data"/>
            </td>
            <td>
                <xsl:value-of select="wiek"/>
            </td>
            <td>
                <xsl:value-of select="waga"/>
            </td>
            <td>
                <xsl:value-of select="wzrost"/>
            </td>
            <td>
                <xsl:value-of select="krew"/>
            </td>
        </tr>
    </xsl:template>

</xsl:stylesheet>