import json
import pandas as pd

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_averages(data):
    types = set()
    for entry in data:
        types.add(entry['type'])
    
    types = list(types)
    metrics = ['bleu1', 'rouge1', 'rougeL', 'meteor', 'bert_f1']
    averages = {metric: {t: [] for t in types} for metric in metrics}
    for entry in data:
        type_ = entry['type']
        for metric in metrics:
            averages[metric][type_].append(entry[metric])
    
    for metric in metrics:
        for t in types:
            averages[metric][t] = sum(averages[metric][t]) / len(averages[metric][t]) if averages[metric][t] else 0
    
    return averages, types

def main():
    data_2d = read_json('2D_norm.json')
    data_3d = read_json('3D_norm.json')
    averages_2d, types = calculate_averages(data_2d)
    averages_3d, _ = calculate_averages(data_3d)
    df_2d = pd.DataFrame(averages_2d).transpose()
    df_3d = pd.DataFrame(averages_3d).transpose()
    common_types = list(set(df_2d.columns) & set(df_3d.columns))
    df_2d = df_2d[common_types]
    df_3d = df_3d[common_types]
    df_2d.columns = ['2D ' + col for col in df_2d.columns]
    df_3d.columns = ['3D ' + col for col in df_3d.columns]
    
    columns = []
    for t in types:
        columns.append(f'2D {t}')
        columns.append(f'3D {t}')

    result_df = pd.concat([df_2d, df_3d], axis=1)[columns]

    print(result_df)
    with open('model_comparison.txt', 'w', encoding='utf-8') as file:
        for index, row in result_df.iterrows():
            file.write('\t'.join(map(str, row)) + '\n')

if __name__ == "__main__":
    main()