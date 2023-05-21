from lxml import etree


if __name__ == '__main__':
    xmlschema_doc = etree.parse("xstl_xpath.xsd")
    xmlschema = etree.XMLSchema(xmlschema_doc)

    doc = etree.parse("xstl_xpath.xml")
    print(xmlschema.validate(doc))

    files = [
        "bmi",
        "cnt",
        "dane",
        "sort",
    ]

    for file in files:
        xmlslt_doc = etree.parse(f"{file}.xslt")
        transform = etree.XSLT(xmlslt_doc)
        result_tree = transform(doc)

        if file == "dane":
            rules = {
                "th": "background-color: #ff0000;",
                "td:nth-child(1), td:nth-child(2)": "background-color: #00ff00;",
                "td:nth-child(3), td:nth-child(4)": "background-color: #0000ff;",
                "td:nth-child(5), td:nth-child(6)": "background-color: #ffa900;"
            }

            # Dodaj element <style> do drzewa XML
            style_element.insert(0, style_element)

        with open(f"genereted_{file}.html", "w") as f:
            f.write(str(result_tree))
