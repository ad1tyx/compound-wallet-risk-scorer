import pandas as pd
import numpy as np

# Step 1: Load the wallet addresses
wallets_df = pd.read_csv('Wallet id - Sheet1.csv')  # change filename if needed

np.random.seed(42)  # For reproducibility (so your results are deterministic)

n = len(wallets_df)

# Step 2: Mock feature engineering (Replace with real on-chain data if available)
# In a real project, fetch & compute from Compound protocol data
wallets_df['num_liquidations'] = np.random.poisson(lam=0.15, size=n)     # most wallets have 0, some 1+
wallets_df['total_borrowed']   = np.random.uniform(250, 10000, size=n)   # USD value borrowed
wallets_df['total_supplied']   = wallets_df['total_borrowed'] + np.random.uniform(500, 10000, size=n) # always above borrowed
wallets_df['active_days']      = np.random.randint(15, 1500, size=n)     # days active in protocol (mock)

# Derived: Collateralization Ratio
wallets_df['collateral_ratio'] = wallets_df['total_supplied'] / (wallets_df['total_borrowed'] + 1e-8)

# Step 3: Feature normalization (min-max scaling)
def normalize(col):
    return (col - col.min()) / (col.max() - col.min() + 1e-8)

wallets_df['n_liquidations_norm']  = normalize(wallets_df['num_liquidations'])
wallets_df['total_borrowed_norm']  = normalize(wallets_df['total_borrowed'])
wallets_df['collateral_ratio_norm']= normalize(wallets_df['collateral_ratio'])
wallets_df['active_days_norm']     = normalize(wallets_df['active_days'])

# Step 4: Risk Index Calculation
# Lower index = lower risk. Weights are illustrative and industry-reasonable.
risk_index = (
    0.40 * wallets_df['n_liquidations_norm'] +          # More liquidations = higher risk
    0.25 * (1 - wallets_df['collateral_ratio_norm']) +  # Lower collateral = higher risk
    0.20 * wallets_df['total_borrowed_norm'] +          # More borrowed = higher risk
    0.15 * (1 - wallets_df['active_days_norm'])         # Newer users = higher risk
)
wallets_df['score'] = np.round((1 - risk_index).clip(0, 1) * 1000).astype(int)

# Step 5: Output as required
wallets_df[['wallet_id', 'score']].to_csv('wallet_scores.csv', index=False)
print("Done. Output saved to wallet_scores.csv")
