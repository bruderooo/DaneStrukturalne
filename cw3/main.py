from collections import defaultdict
from pathlib import Path
import json

import jsonschema

if __name__ == '__main__':
    loaded = json.loads(Path("dl.json").read_text())
    json_schema = json.loads(Path("schema.json").read_text())

    freq = defaultdict(int)

    for each in loaded:
        for number in each["numer"]:
            freq[number] += 1

    out = {
        "czestotliwosc": freq,
        "najczesciej": int(max(freq, key=freq.get)),
        "najrzadziej": int(min(freq, key=freq.get)),
    }

    Path("wynik_dl.json").write_text(json.dumps(out, indent=4))
    jsonschema.validate(instance=out, schema=json_schema)
