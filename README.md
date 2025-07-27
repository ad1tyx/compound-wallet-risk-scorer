Certainly! Here's a polished and well-structured explanation you can include in your project folder (e.g., as a `README.md` or `EXPLANATION.txt`) or directly in your assignment submission. It clearly outlines your approach, rationale, and methodology in a professional tone:

# Wallet Risk Scoring: Approach and Explanation

## 1. Data Collection Method

The assignment provided a list of wallet addresses, but no direct access to their on-chain transaction histories for Compound V2 or V3. To build a scalable and practical risk scoring pipeline, the solution simulates key wallet features through synthetic data generation that mimics real-world behavior.

In a production environment, these features would be obtained by querying on-chain data through APIs such as The Graph, Alchemy, Etherscan, or DeFi analytics platforms, extracting transaction events like deposits, borrows, repayments, and liquidations associated with each wallet.

The current design keeps the pipeline modular, so replacing the synthetic data with actual on-chain data later would require minimal code changes.

## 2. Feature Selection Rationale

The features selected for scoring are widely recognized indicators of wallet risk in lending protocols:

- **Number of Liquidations:** Reflects how frequently a wallet failed to maintain sufficient collateral, causing forced asset sales. More liquidations directly correlate to higher risk.
- **Total Borrowed:** Represents the amount of assets borrowed by the wallet. Higher borrow amounts increase exposure and potential risk.
- **Total Supplied:** The volume of assets supplied or collateralized. This helps determine the wallet’s collateral buffer.
- **Collateralization Ratio:** Calculated as total supplied divided by total borrowed. A higher ratio indicates a safer position with more collateral backing debt.
- **Active Days:** The length of time the wallet has been active in the protocol. Older wallets typically have more stable and trustworthy behavior patterns.

These features collectively capture both behavior (liquidations, time active) and exposure (borrowed vs. supplied), essential for a robust risk assessment.

## 3. Scoring Methodology

To create a consistent and comparable risk score across wallets, the following process is applied:

- **Normalization:** Each feature is normalized via min-max scaling to bring values into the [0,nge, preventing dominance by any single metric due to scale differences.
  
- **Weighted Risk Index:** A weighted sum of normalized risk factors computes the wallet’s overall risk profile.
  
  - Number of liquidations contributes 40% — as it is the most direct signal of poor risk management.
  - Collateralization ratio (inverted) contributes 25% — lower collateral ratios signify higher risk.
  - Total borrowed contributes 20% — capturing the scale of exposure.
  - Active days (inverted) contributes 15% — newer wallets tend to have higher risk due to limited history.

- **Final Score Calculation:**  
  The risk index is inverted and scaled to a 0-1000 score, where higher scores indicate lower risk. Mathematically:

  $$
  \text{score} = (1 - \text{Risk Index}) \times 1000
  $$

This approach yields an intuitive, normalized risk score that reflects wallet behavior and exposure comprehensively.

## 4. Justification of Risk Indicators

- **Liquidation Events:** Empirically, liquidation history is among the strongest predictors of future risk since it signals failure in maintaining liquidation thresholds.

- **Collateralization Ratio:** This is a fundamental DeFi risk metric implemented in protocols like Compound and Aave to prevent undercollateralized loans.

- **Total Borrowed:** The amount borrowed indicates the wallet’s exposure to market conditions and debt repayment requirements.

- **Account Age (Active Days):** Established wallets generally have more predictable borrowing and repayment behavior, decreasing risk.

The weighted scoring reflects industry best practices, balancing direct defaults, exposure, and behavioral factors.

## 5. Scalability and Future Improvements

The scoring pipeline is fully modular and ready to incorporate live data sources whenever available. When connected to on-chain data APIs or subgraphs, the synthetic feature generation can be replaced by actual metrics with no changes in scoring logic.

Additional features like repayment timeliness, debt-to-collateral volatility, or interaction with multiple protocols can be integrated to enhance prediction accuracy in future iterations.

# Summary

This approach delivers a clear, transparent, and interpretable wallet risk score based on sound DeFi lending risk principles, with a scalable architecture suitable for both simulated and real-world data.
