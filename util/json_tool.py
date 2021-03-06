"""
Copyright (c) 2018 iCyP
Released under the MIT license
https://opensource.org/licenses/mit-license.php

"""

import json
import struct
import sys
import tkinter.filedialog
from collections import OrderedDict

read_path = tkinter.filedialog.askopenfilename(
    filetypes=[("glb,vrm,json", "*.glb;*.vrm;*.json")]
)
loaded_json = ""
with open(read_path, "rb") as f:
    filetype = read_path.split(".")[-1]
    if filetype in ("vrm", "glb"):
        binary = f.read()
        magic = 12  # offset from header
        bi_size = struct.unpack("<I", binary[magic : magic + 4])[0]
        magic = 20  # offset from header
        loaded_json = json.loads(
            binary[magic : magic + bi_size].decode("utf-8"),
            object_pairs_hook=OrderedDict,
        )
        with open(read_path + ".json", "wt") as file:
            file.write(json.dumps(loaded_json, indent=4))
    elif filetype == "json":
        loaded_json = json.load(f)
    else:
        print("unsupported format :{}".format(filetype))
        sys.exit(1)

# something do in below with loaded_json


# for scene in loaded_json["scenes"]:
for i, m in enumerate(loaded_json["materials"]):
    print(i, m["name"])

with open(read_path + "_skin" + ".json", "wt") as f:
    f.write(json.dumps(loaded_json, indent=4))
