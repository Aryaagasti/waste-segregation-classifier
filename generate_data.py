import pandas as pd
import numpy as np

np.random.seed(42)
data_size = 1000

data = {
    'material_type': np.random.choice([1, 2, 3], data_size),  # 1: Paper, 2: Food, 3: Battery
    'decomposition_time': np.random.randint(1, 25, data_size),
    'source': np.random.choice([1, 2, 3], data_size),  # 1: Home, 2: Restaurant, 3: Industry
    'target': np.random.choice(['Recyclable', 'Organic', 'Hazardous'], data_size)
}

df = pd.DataFrame(data)
df.to_csv('data/synthetic_data.csv', index=False)
print("Data generated and saved to 'data/synthetic_data.csv'")