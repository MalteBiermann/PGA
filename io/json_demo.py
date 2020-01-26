import json
import urllib.request
import ssl

import sys
sys.path.append(".")

from datentyp.punkt import Punkt

j_s = """{
    "Hersteller": "Fiat",
    "Baujahr": 1990,
    "Halter":{
        "Nachname": "Golly",
        "Vorname": "Andreas"
    }
}"""

j_d = json.loads(j_s)
print(json.dumps(j_d, sort_keys=True, indent=4))


# with open("../testdata/json1.csv") as fh:
#     j_d2 = json.loads(fh)
# print(json.dumps(j_d2, sort_keys=True, indent=4)) 

k = ssl._create_unverified_context()
with urllib.request.urlopen("https://py.webmapping.eu/kfz.json",context=k) as j_url:
    j_d3 = json.loads(j_url.read().decode())
print(json.dumps(j_d3, sort_keys=True, indent=4))

with open(r"C:\Users\hir0\OneDrive\VSC-Workspace\PGA\testdata\json_url_output.json", "w") as fh_w:
    json.dump(j_d3, fh_w)
    
p = Punkt(1, 2)
print(p.__dict__)

with open(r"C:\Users\hir0\OneDrive\VSC-Workspace\PGA\testdata\json_punkt_output.json", "w") as fh_w:
    json.dumps(p, fh_w, default=Punkt.get_json())

p2 = Punkt()
with open(r"C:\Users\hir0\OneDrive\VSC-Workspace\PGA\testdata\json_punkt_output.json") as fh_r:
    p2.set_json(json.dumps(fh_r))
