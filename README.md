Brief Explanation
Data Collection Method
For this assignment, the primary data provided was a list of wallet addresses in the file Wallet id - Sheet1.csv. No live Compound protocol transaction history was available. To demonstrate a scalable risk scoring pipeline, mock wallet features were generated synthetically within the code, simulating the process as if we had queried real on-chain activity from Compound (using Web3, The Graph, or a DeFi analytics API). The pipeline is structured so real data can be swapped in without changing the analysis steps.

Feature Selection Rationale
The following features were engineered for each wallet, based on widely accepted DeFi risk modeling:

Number of Liquidations: Indicates the wallet's history of failing to maintain adequate collateral (major risk marker).

Total Borrowed: The total value borrowed (in USD), as higher borrowings increase exposure.

Total Supplied: The total value supplied, used to derive collateralization.

Collateralization Ratio: Supplied divided by borrowed value; a core DeFi protocol risk metric.

Active Days: Duration of account activity, as longer tenure is typically correlated with more reliable user behavior.

These features reflect both the scale of user activity and behavioral risk, aligning with best practices used in DeFi protocol research.

Scoring Method
All features are normalized via min-max scaling to ensure comparability.

A weighted risk index is calculated for each wallet, emphasizing key risk facets:

40%: Number of liquidations (more weight for higher risk)

25%: (1 - Collateralization ratio) (lower ratio = greater risk)

20%: Total borrowed (greater borrowing drives risk up)

15%: (1 - Active days normalized) (newer wallets slightly riskier)

The final risk score is computed as:

score
=
(
1
−
Risk Index
)
×
1000
score=(1−Risk Index)×1000
This yields a score between 0 (high risk) and 1000 (low risk).

Justification of Risk Indicators
The selected indicators are standard in on-chain lending:

Liquidation events are a direct and reliable indicator of past protocol risk.

Collateralization is foundational to prevent bad debt in lending systems—protocols like Compound and Aave use this as a primary measure.

Borrowing behavior affects exposure and protocol systemic risk.

Account age is a well-known credit predictor: longer-lived wallets statistically behave more reliably.

Weights were chosen to provide transparency, favoring interpretability and compatibility with more complex or real data sources in the future.

Scalability
The pipeline is modular—when real on-chain wallet histories from Compound V2/V3 are available, feature assignment can simply be replaced by actual metric computation. The risk scoring logic, normalization, and output steps will remain unchanged, ensuring the approach’s scalability and future-proofing.

