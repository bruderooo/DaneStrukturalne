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

        with open(f"genereted_{file}.html", "w") as f:
            f.write(str(result_tree))
