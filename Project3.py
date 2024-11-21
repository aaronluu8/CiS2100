import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# --- Step 1: Load and preview the data ---
file_path = 'sales_data.csv'  # Ensure your CSV file is in the correct path
data = pd.read_csv(file_path)

# Dataset Overview
print("Dataset Overview:")
print(data.head())
print(data.info())

# --- Step 2: Data Preprocessing ---
# Convert 'Product Name' to a basket format: each order becomes a row of products purchased
basket = data.groupby(['OrderID', 'Product Name'])['Product Name'].count().unstack().fillna(0)

# Convert the counts to 1s and 0s (1 if purchased, 0 if not)
basket = basket.applymap(lambda x: 1 if x > 0 else 0)

# --- Step 3: Market Basket Analysis ---
# Generate frequent itemsets using the Apriori algorithm
min_support = 0.1  # Minimum support value, can be adjusted
frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)

# Display the frequent itemsets
print("\nFrequent Itemsets:")
print(frequent_itemsets.sort_values('support', ascending=False).head())

# --- Step 4: Generate Association Rules ---
# Define minimum confidence for association rules
min_confidence = 0.3  # Minimum confidence value, can be adjusted

# Generate the association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence, num_itemsets=10)

# Display the top association rules
print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())

