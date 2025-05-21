import json
import os

with open('3D.json', 'r', encoding='utf-8') as f:
    answer_data = json.load(f)
with open('valid_short_dialog.json', 'r', encoding='utf-8') as f:
    dialog_data = json.load(f)

dialog_map = {item['id']: item for item in dialog_data}
result = []

for entry in answer_data:
    id_ = entry['id']
    answer = entry['answer']
    predict = entry['predict']
    bleu1 = entry.get('bleu1', 0.0)
    rouge1 = entry.get('rouge1', 0.0)
    rougeL = entry.get('rougeL', 0.0)
    meteor = entry.get('meteor', 0.0)
    bert_f1 = entry.get('bert_f1', 0.0)

    if id_ in dialog_map:
        conversations = dialog_map[id_].get('conversations', [])
        last_human_type = None
        for conv in reversed(conversations):
            if conv.get('from') == 'human' and 'type' in conv:
                last_human_type = conv['type']
                break

        result.append({
            "id": id_,
            "type": last_human_type,
            "answer": answer,
            "predict": predict,
            "bleu1": bleu1,
            "rouge1": rouge1,
            "rougeL": rougeL,
            "meteor": meteor,
            "bert_f1": bert_f1
        })
    else:
        print(f"[Warning] ID {id_} not found in dialog data.")

with open('3D_new.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)