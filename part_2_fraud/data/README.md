# Bank Account Fraud (BAF) Dataset

**Authors:**  
Sérgio Jesus (Feedzai / Universidade do Porto)  
José Pombal, Duarte Alves, André F. Cruz, Pedro Saleiro, Pedro Bizarro (Feedzai)  
Rita P. Ribeiro, João Gama (Universidade do Porto)  

**Contact:** sergio.jesus@feedzai.com

**License:** [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)

**Repository:** [GitHub - Feedzai Bank Account Fraud](https://github.com/feedzai/bank-account-fraud)

---

## Motivation

- Evaluate ML methods and fairness under dynamic and extreme conditions.
- Stress-test ML models and fair ML interventions.
- Introduce various bias patterns for fairness-performance trade-off analysis.

## Dataset Composition

- **Instances:** 6 datasets × 1M instances each = **6M total instances**.
- **Representation:** Synthetic, feature-engineered bank account applications.
- **Generation:** CTGAN trained on anonymized real-world banking data.
- **Variants:** 5 biased versions + 1 unbiased base dataset.

## Features

| Feature | Type | Description |
|:---|:---|:---|
| `income` | Numeric | Annual income decile [0.1, 0.9] |
| `name_email_similarity` | Numeric | Similarity between email and name [0, 1] |
| `prev_address_months_count` | Numeric | Months at previous address [−1, 380] |
| `current_address_months_count` | Numeric | Months at current address [−1, 429] |
| `customer_age` | Numeric | Age (rounded to decade) [10, 90] |
| `days_since_request` | Numeric | Days since application [0, 79] |
| `intended_balcon_amount` | Numeric | Initial transfer amount [−16, 114] |
| `payment_type` | Categorical | Payment plan (5 anonymized categories) |
| `zip_count_4w` | Numeric | Applications from same zip in 4 weeks [1, 6830] |
| `velocity_6h` | Numeric | Avg. apps/hour in last 6 hours [−175, 16818] |
| `velocity_24h` | Numeric | Avg. apps/hour in last 24 hours [1297, 9586] |
| `velocity_4w` | Numeric | Avg. apps/hour in last 4 weeks [2825, 7020] |
| `bank_branch_count_8w` | Numeric | Applications per branch in 8 weeks [0, 2404] |
| `date_of_birth_distinct_emails_4w` | Numeric | Distinct emails for same DOB in 4 weeks [0, 39] |
| `employment_status` | Categorical | Employment status (7 anonymized values) |
| `credit_risk_score` | Numeric | Internal risk score [−191, 389] |
| `email_is_free` | Binary | Free vs paid email domain |
| `housing_status` | Categorical | Residential status (7 anonymized values) |
| `phone_home_valid` | Binary | Valid home phone |
| `phone_mobile_valid` | Binary | Valid mobile phone |
| `bank_months_count` | Numeric | Months with previous bank account [−1, 32] |
| `has_other_cards` | Binary | Holds other cards with bank |
| `proposed_credit_limit` | Numeric | Proposed credit limit [200, 2000] |
| `foreign_request` | Binary | Origin country ≠ bank's country |
| `source` | Categorical | Application source: browser or app |
| `session_length_in_minutes` | Numeric | Session length [−1, 107] |
| `device_os` | Categorical | OS (Windows, macOS, Linux, X11, other) |
| `keep_alive_session` | Binary | Keep session alive option |
| `device_distinct_emails` | Numeric | Distinct emails from device [−1, 2] |
| `device_fraud_count` | Numeric | Number of frauds from device [0, 1] |
| `month` | Numeric | Month of application [0, 7] |
| `fraud_bool` | Binary | **Target label** (1 = Fraud, 0 = Not fraud) |

## Data Characteristics

- **Sampling:** Stratified to induce or avoid bias.
- **Labels:** Reliable; fraud is confirmed; non-fraud highly trustworthy.
- **Privacy:**  
  - Original data anonymized and privatized (Laplacian noise, categorization).  
  - No real individual's information preserved.

## Recommended Data Splits

- Use **first 6 months** for training, **last 2 months** for validation.
- Temporal cross-validation is encouraged.

## Usage Notes

- Suitable for:  
  - Fairness research  
  - Stress-testing ML models  
  - Temporal evaluation of ML models
- **Not suitable** for deploying real-world fraud detection models.

## Known Limitations

- Synthetic data: Possible artifacts from CTGAN.
- No links between instances (no session/user tracking).
- Ground truth labels have slight selection biases (e.g., regulatory rejections).

## Distribution and Licensing

- Distributed on GitHub and Kaggle.
- **License:** [Creative Commons CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)