import json

with open('2D_new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

max_values = {
    'bleu1': 0,
    'rouge1': 0,
    'rougeL': 0,
    'meteor': 0,
    'bert_f1': 0
}
min_values = {
    'bleu1': 1,
    'rouge1': 1,
    'rougeL': 1,
    'meteor': 1,
    'bert_f1': 1
}

for entry in data:
    for metric in max_values:
        max_values[metric] = max(max_values[metric], entry[metric])
        min_values[metric] = min(min_values[metric], entry[metric])

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if (max_val - min_val) != 0 else 0

normalized_data = []
for entry in data:
    normalized_entry = entry.copy()
    for metric in max_values:
        normalized_entry[metric] = normalize(entry[metric], min_values[metric], max_values[metric])
    normalized_data.append(normalized_entry)

with open('2D_norm.json', 'w', encoding='utf-8') as f:
    json.dump(normalized_data, f, indent=4, ensure_ascii=False)


with open('2D_norm.json', 'r') as f:
    data = json.load(f)

for item in data:
    bleu1 = item.get('bleu1', 0)
    rouge1 = item.get('rouge1', 0)
    rougeL = item.get('rougeL', 0)
    meteor = item.get('meteor', 0)
    bert_f1 = item.get('bert_f1', 0)
    ave = (bleu1 + rouge1 + rougeL + meteor + bert_f1) / 5
    item['ave'] = ave

with open('2D_norm.json', 'w') as f:
    json.dump(data, f, indent=4)
