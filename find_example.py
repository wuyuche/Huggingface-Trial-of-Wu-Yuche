import json
from collections import defaultdict

with open('2D_norm.json', 'r') as f:
    data_2d = json.load(f)
with open('3D_norm.json', 'r') as f:
    data_3d = json.load(f)

ave_2d = {item['id']: item.get('ave', 0) for item in data_2d}
ave_3d = {item['id']: item.get('ave', 0) for item in data_3d}
id_to_type = {item['id']: item['type'] for item in data_2d if 'id' in item and 'type' in item}

type_to_diffs = defaultdict(list)
for id_ in ave_2d:
    if id_ in ave_3d and id_ in id_to_type:
        type_ = id_to_type[id_]
        diff = abs(ave_2d[id_] - ave_3d[id_])
        type_to_diffs[type_].append((id_, diff))

for type_, id_diffs in type_to_diffs.items():
    top2 = sorted(id_diffs, key=lambda x: x[1], reverse=True)[:2]
    print(f"\nType: {type_}")
    for id_, diff in top2:
        print(f"  id: {id_}, ave_diff: {diff:.7f}")
