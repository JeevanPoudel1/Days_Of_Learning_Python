import io
import pandas as pd

# Your exact dataset loaded directly into the script
data = """Property_ID,Square_Feet,Bedrooms,Age_Years,Neighborhood,Has_Pool,Price_USD
PROP_1000,1660.0,4,48.0,Suburbs,No,295656
PROP_1001,2094.0,3,39.0,Suburbs,No,328726
PROP_1002,,4,29.0,Rural,No,343215
PROP_1003,1895.0,4,42.0,Suburbs,No,313386
PROP_1004,2438.0,2,26.0,Rural,Yes,382708
PROP_1005,,2,35.0,Suburbs,No,425610
PROP_1006,1266.0,2,25.0,Suburbs,No,229433
PROP_1007,2038.0,3,24.0,Downtown,No,371096
PROP_1008,1130.0,4,13.0,Downtown,No,316489
PROP_1009,2282.0,4,,Rural,No,426710
PROP_1010,2935.0,1,36.0,Downtown,No,403958
PROP_1011,930.0,3,45.0,Rural,No,190750
PROP_1012,2485.0,3,20.0,Suburbs,No,389260
PROP_1013,1569.0,2,1.0,Suburbs,Yes,325638
PROP_1014,3191.0,2,8.0,Downtown,No,506871
PROP_1015,2315.0,2,,Rural,Yes,325526
PROP_1016,3233.0,4,16.0,Rural,No,494346
PROP_1017,2015.0,2,14.0,Suburbs,No,325721
PROP_1018,1755.0,3,12.0,Suburbs,Yes,355095
PROP_1019,3124.0,3,23.0,Downtown,No,503715
PROP_1020,,2,15.0,Suburbs,No,329658"""

# 1. Load data from the string
df = pd.read_csv(io.StringIO(data))

# 2. Drop the identifier column
df = df.drop(columns=["Property_ID"])

# 3. Handle Missing Values (Imputation)
df["Square_Feet"] = df["Square_Feet"].fillna(df["Square_Feet"].mean())
df["Age_Years"] = df["Age_Years"].fillna(df["Age_Years"].mean())

# 4. Transform Categorical variables to numbers
df["Has_Pool"] = df["Has_Pool"].map({"No": 0, "Yes": 1})
df_encoded = pd.get_dummies(df, columns=["Neighborhood"], drop_first=True)

# 5. Isolate Target and Features inside Pandas
X_df = df_encoded.drop(columns=["Price_USD"])
y_df = df_encoded["Price_USD"]

# 6. Shuffle and Split rows using pure Pandas sampling (80% Train, 20% Test)
X_train_df = X_df.sample(frac=0.8, random_state=42)
y_train_df = y_df.loc[X_train_df.index]

X_test_df = X_df.drop(X_train_df.index)
y_test_df = y_df.drop(X_train_df.index)

print("--- TRANSFORMED DATAFRAME ---")
print(df_encoded.head())
print("\n--- PANDAS ML SPLIT ---")
print(f"Training Rows: {len(X_train_df)} | Testing Rows: {len(X_test_df)}")
