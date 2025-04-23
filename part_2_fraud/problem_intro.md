
# 💸 Synthetic Fraud Detection Dataset: PaySim Overview

## 📚 Problem Context

Access to real-world financial transaction data, especially from mobile money platforms in emerging markets, is exceptionally rare due to the intrinsic privacy and security concerns surrounding personal and corporate finance. However, detecting fraud in these financial systems is a growing research and operational need, particularly in regions like sub-Saharan Africa where mobile payments are the backbone of financial inclusion.

To address this data gap, researchers developed **PaySim**, a simulation framework that produces realistic synthetic data mimicking the structure and behavior of real mobile money transaction logs. The resulting dataset provides a public benchmark for developing and testing fraud detection systems.

## 🌍 Domain and Data Origin

The **PaySim** dataset simulates **mobile money transactions**, modeled on actual transactional behavior in an African country where a major multinational telecommunications company provides financial services. Mobile money systems, such as M-Pesa, have revolutionized access to financial services in regions with limited traditional banking infrastructure.

Key characteristics of this domain:
- High volume of **peer-to-peer (P2P)** and **merchant** transactions.
- Varied transaction types: **CASH-IN**, **CASH-OUT**, **TRANSFER**, **PAYMENT**, and **DEBIT**.
- Exposure to unique **fraud risks**, including social engineering, account takeovers, and rapid money laundering techniques.

The original dataset was a month’s worth of real mobile money transaction logs. PaySim uses this data to simulate agent-based behavior, injecting fraudulent actions based on known fraud strategies.

## 🧪 The Simulation: How PaySim Works

PaySim is a **Multi-Agent Based Simulation (MABS)** built using the MASON framework. It models user behaviors over a 30-day period, generating synthetic transactions hour-by-hour, preserving the temporal and behavioral structure of real-world data.

Simulation Steps:
1. **Client Generation**: Clients are assigned transaction profiles and behavioral rules based on statistical analysis of the real dataset.
2. **Transaction Execution**: Clients perform actions (e.g., transfer, cash-out) probabilistically, interacting with other agents.
3. **Fraud Injection**: A subset of clients are simulated as fraudsters, performing illicit behaviors such as draining accounts via fake transfers and cash-outs.
4. **Logging and Output**: The simulator outputs structured records that resemble real transaction data, including fraud labels.

## 📦 Dataset Overview

Each row in the dataset represents a **single transaction**, with these key features:

| Column | Description |
|--------|-------------|
| `step` | Hourly time step (1 to 744 = 31 days) |
| `type` | Transaction type (CASH-IN, CASH-OUT, DEBIT, PAYMENT, TRANSFER) |
| `amount` | Amount of money moved |
| `nameOrig` | Origin account/customer ID |
| `oldbalanceOrg` | Balance of origin account before transaction (do not use in fraud prediction) |
| `newbalanceOrig` | Balance of origin account after transaction (do not use in fraud prediction) |
| `nameDest` | Destination account/customer ID |
| `oldbalanceDest` | Destination balance before transaction (only for non-merchants) |
| `newbalanceDest` | Destination balance after transaction (only for non-merchants) |
| `isFraud` | **Target variable** – was the transaction fraudulent? |
| `isFlaggedFraud` | Was it flagged by internal threshold systems? (e.g., >200K transfer) |

⚠️ **Important Note**: Certain balance fields (like `oldbalanceOrg`) are known to leak the fraud label due to how fraud is simulated. For realistic modeling, avoid using these features directly.

## 🧠 Fraudulent Behavior Modeled

In PaySim, fraudulent activity typically follows this pattern:
- A fraudster **gains control** of a legitimate user account.
- They **transfer funds** to a secondary account.
- They then **cash out** the stolen funds.

This mimics real-world attack vectors in mobile financial systems, where speed and automation are crucial for fraud detection.

## 📈 Why This Dataset Matters

PaySim offers a rare opportunity to study:
- **Fraud detection** in under-represented financial environments.
- The dynamics of agent-based financial ecosystems.
- Machine learning in **class-imbalanced** scenarios (fraud is very rare).
- Ethical and effective fraud detection systems for financial inclusion.

## 🧾 Citation and Further Reading

If using this dataset in your work, please cite:

> **Lopez-Rojas, E. A., Elmir, A., & Axelsson, S.** (2016). *PaySim: A financial mobile money simulator for fraud detection*. EMSS 2016. [ResearchGate](https://www.researchgate.net/publication/313138956_PAYSIM_A_FINANCIAL_MOBILE_MONEY_SIMULATOR_FOR_FRAUD_DETECTION)
