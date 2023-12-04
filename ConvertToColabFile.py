import pandas as pd

# 設置原始和新文件的路徑
original_csv_path = 'structured_data_mac.csv'
modified_csv_path = 'modified_structured_data_mac.csv'

# 讀取原始 CSV 文件
df = pd.read_csv(original_csv_path)

# 更新 'Image Path' 列
df['Image Path'] = df['Image Path'].apply(
    lambda x: f'/content/drive/My Drive/Colab Notebooks/Hans/{x}' if pd.notnull(x) else x)

# 保存修改後的數據到新文件
df.to_csv(modified_csv_path, index=False)

print("CSV file has been modified and saved.")
