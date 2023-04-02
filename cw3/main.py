from collections import defaultdict
from pathlib import Path
import json
from typing import Dict

import jsonschema
import yaml


def compute_output(data: Dict):
    freq = defaultdict(int)

    for each in data:
        for number in each["numer"]:
            freq[number] += 1

    return {
        "czestotliwosc": dict(freq),
        "najczesciej": int(max(freq, key=freq.get)),
        "najrzadziej": int(min(freq, key=freq.get)),
    }


def compute_for_json():
    loaded = json.loads(Path("dl.json").read_text())
    json_schema = json.loads(Path("schema.json").read_text())

    out = compute_output(loaded)

    jsonschema.validate(instance=out, schema=json_schema)
    Path("wynik_dl.json").write_text(json.dumps(out, indent=4))


def compute_for_yaml():
    local_path = Path(__file__).parent

    with local_path.joinpath("dl_file.yml").open() as f:
        parsed = yaml.safe_load(f)['root']['data']

    out = compute_output(parsed)

    with local_path.joinpath("wynik_dl.yml").open("w") as f:
        yaml.dump(out, f)


if __name__ == '__main__':
    compute_for_json()
    compute_for_yaml()
