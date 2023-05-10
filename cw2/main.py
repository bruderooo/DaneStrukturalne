from collections import Counter
from pathlib import Path
from lxml import etree


def dict2xml(dict_data: dict):
    def elem(data):
        if isinstance(data, dict):
            out = ""
            for key, val in data.items():
                if isinstance(key, int):
                    out += f'<liczba wartosc="{key}">{elem(val)}</liczba>'
                else:
                    out += f'<{key}>{elem(val)}</{key}>'
            return out
        return data

    return f'<?xml version="1.0"?><!DOCTYPE root SYSTEM "wynik_dl.dtd"><root>{elem(dict_data)}</root>'


if __name__ == '__main__':
    filepath = Path(__file__).parent.joinpath("dl.xml")
    parser = etree.XMLParser(dtd_validation=True)
    tree = etree.parse(filepath, parser=parser)

    all_nums = (int(elem.text) for elem in tree.iter("numer"))
    sorted_freq = sorted(Counter(all_nums).items(), key=lambda x: x[1])

    most_common, *_, least_common = sorted_freq
    out = {
        "czestotliwosc": dict(sorted_freq),
        "najczesciej": least_common[0],
        "najrzadziej": most_common[0],
    }

    xml_converted = dict2xml(out)
    dom = etree.fromstring(xml_converted, parser=parser)
    pretty_xml_as_string = etree.tostring(dom, pretty_print=True, encoding="unicode")

    with open("wynik_dl.xml", "w") as f:
        f.write(pretty_xml_as_string)
