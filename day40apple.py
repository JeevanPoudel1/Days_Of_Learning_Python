import pandas as pd
df = pd.read_csv('pokemon.csv', index_col='Name')


pokemon = input("Enter the name of the Pokemon: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print("Pokemon not found in the dataset.")

# filtering data based on conditions
#filtering = keeping only the rows that satisfy a certain condition

filtered_df = df[df['Type 1'] == 'Fire']
print(filtered_df)


filter_attack = df[df['Attack'] > 150]
print(filter_attack)

heavy_pokemon = df[df['Generation'] > 3]
print(heavy_pokemon)

legendary_pokemon = df[df['Legendary'] == True]
print(legendary_pokemon)

attack_health = df[(df['Attack'] > 100) & (df['HP'] > 100)]
print(attack_health)

ff_pokemon = df[(df['Type 1'] == 'Fire') & (df['Type 2'] == 'Flying')]
print(ff_pokemon)


