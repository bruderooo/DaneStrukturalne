<?xml version="1.0" encoding="utf-8" ?>

<!--   Stworzyc kilka szablonow XSLT ktore podpiete pod orginalny dokument-->
<!--   xml pozwola, wygenerowac dokument html, ktory zawsze bedzie mial naglowek-->
<!--   h1 w ktorym bedzie tytul zestawienia danych, a nastepnie wyswietli sie tabela-->
<!--   ktora rozwiaze nastepujace problemy:-->
<!--   c) wyswietli zestawienie podajace ile osob ma dana grupe krwi.-->

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <h1>Ile osób ma daną grupę krwi</h1>
            </head>
            <body>
                <table border="1">
                    <tr>
                        <th>Grupa krwi</th>
                        <th>Ilosc osob</th>
                    </tr>
                    <xsl:for-each select="dane/osoba">
                        <xsl:if test="position() = 1 or krew != preceding-sibling::osoba[1]/krew">
                            <tr>
                                <td>
                                    <xsl:value-of select="krew"/>
                                </td>
                                <td>
                                    <xsl:value-of select="count(../osoba[krew = current()/krew])"/>
                                </td>
                            </tr>
                        </xsl:if>
                    </xsl:for-each>
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
