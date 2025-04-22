
# 💳 Detecting Financial Fraud with Machine Learning

Welcome! In this module, you'll take on the role of a data scientist working to detect fraud in mobile money transactions. Fraud is rare, but costly — and catching it requires more than just good accuracy. We'll walk through a full machine learning workflow using a realistic, imbalanced dataset and modern tools.

---

## 📚 Learning Goals

By the end of this session, you will be able to:

- ✅ Explain why class imbalance is a common and critical issue in real-world decision-making.
- 🔍 Evaluate classification models with appropriate metrics (e.g., precision, recall, ROC-AUC).
- 🧪 Apply techniques like SMOTE and ensemble models to improve detection of rare events.
- 📈 Understand the role of score calibration and probability thresholds in business decisions.
- 💼 Design a fraud detection policy that reflects resource constraints and cost trade-offs.

---

## 🗂️ Project Structure

| File | Description |
|------|-------------|
| `data/imbl_fraud.csv` | Pre-sampled PaySim dataset (fraud rate ~6%) |
| `notebooks/01_baseline_model_ex.ipynb` | 📝 Exercise – EDA + baseline model with metrics |
| `notebooks/01_baseline_model_sol.ipynb` | ✅ Solution – EDA + baseline model completed |
| `notebooks/02_imbalance_handling_ex.ipynb` | 📝 Exercise – SMOTE + balanced ensemble models |
| `notebooks/02_imbalance_handling_sol.ipynb` | ✅ Solution – SMOTE + balanced ensemble models |
| `notebooks/03_calibration_thresholds_ex.ipynb` | 📝 Exercise – Score calibration, top-k targeting |
| `notebooks/03_calibration_thresholds_sol.ipynb` | ✅ Solution – Score calibration, top-k targeting |
| `notebooks/04_bonus_cost_sensitive_ex.ipynb` | 📝 (Optional) Exercise – Custom thresholds + costs |
| `notebooks/04_bonus_cost_sensitive_sol.ipynb` | ✅ (Optional) Solution – Custom thresholds + costs |
| `utils/metrics_helpers.py` | Reusable functions: PR@k, calibration plot, confusion matrix |
| `activities/decision_policy_prompt.md` | In-class discussion prompt: How would *you* deploy a model? |
| `problem_generation/` | Code to generate the imbalanced dataset (you can ignore it) |


---

## 🎥 Slides

📽️ **[Intro Slides — Real-World Fraud Detection & Class Imbalance](https://your-slides-link.com)**  
*(Make a copy in your Google Drive if you'd like to take notes.)*

---

## 🚀 Getting Started

You can run this project on your local machine or in Google Colab.

### Option 1: Jupyter Lab
If you have Jupyter set up:

```bash
jupyter lab
```

Then open any notebook inside the `notebooks/` folder.

### Option 2: Google Colab
Just drag and drop a notebook into [Google Colab](https://colab.research.google.com/), then upload `data/imbl_fraud.csv` when prompted.

---

## 💡 Tips

- The dataset is **imbalanced** — don't trust accuracy!
- Focus on **recall** if you're trying to catch as much fraud as possible.
- Focus on **precision** if investigations are costly and you want fewer false alarms.
- There’s no single "best" threshold — it depends on your business case.

---

## 🛠️ Tools & Libraries

- `pandas`, `matplotlib`, `seaborn`
- `scikit-learn`
- `imbalanced-learn` (for SMOTE, balanced models)

No environment file needed — just make sure these are installed, or use Colab.

---

## 📄 License

MIT — feel free to remix and reuse this for your own learning or teaching.

---

👩‍🏫 Developed for an Intro to Machine Learning course (Econ & Management undergraduate level).
