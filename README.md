

# 🚕 RoutePulse: Scalable Transportation Analytics using a Hadoop-Spark Pipeline on NYC Yellow-Taxi Data

A scalable data engineering and analytics pipeline built on **Apache Hadoop and Apache Spark**, leveraging **NYC Yellow Taxi** data to uncover transportation trends and build predictive models. This project includes data ingestion, preprocessing, clustering, classification, visualization, and model deployment using a modular pipeline.

---

## 📁 Project Structure

| Folder / File             | Description                                                |
|--------------------------|------------------------------------------------------------|
| `data/`                  | Raw or preprocessed dataset (.csv/.parquet) files          |
| `notebook/`              | Jupyter notebooks for exploration and development          |
| `outputs/`               | Output predictions and metrics                             |
| ├── `lr_predictions.parquet/` | Logistic Regression model outputs                   |
| ├── `nb_predictions.parquet/` | Naive Bayes model outputs                        |
| └── `metrics/`           | Performance metrics and evaluation results                 |
| `presentation/`          | Project presentation slides                                |
| `reports/`               | Final project report in PDF format                         |
| `saved_models/`          | Trained ML models (.pkl or folders)                        |
| `screenshots/`           | Screenshots from pipeline, DAGs, visualizations            |
| `scripts/`               | Python scripts, Spark jobs, docker-compose.yaml            |
| `requirements.txt`       | Python dependencies list                                   |
| `README.md`              | You're here!                                               |

---

## 🚀 Features

- ✅ End-to-end Hadoop + Spark ML pipeline
- ✅ Data preprocessing, feature engineering
- ✅ Logistic Regression, Naive Bayes, DBSCAN models
- ✅ Visualized clustering and performance metrics
- ✅ Model serialization and Parquet output
- ✅ Dockerized with `docker-compose.yaml` for easy deployment

---

## 📦 Installation

Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

Ensure Spark and Hadoop are properly installed in your system or container.

To run the Dockerized version:

```bash
docker-compose up
```

---

## 🧪 How to Run

1. **Data Preprocessing:**
   - Check `/data/` for `.csv`, `.parquet`, or Spark `.crc` files
2. **Exploratory Data Analysis:**
   - Use notebooks from `/notebook/`, like `code.ipynb`
3. **Model Execution:**
   - Run `spd.py` from `/scripts/` to execute the pipeline
4. **Model Outputs:**
   - Results saved in `/outputs/` and models in `/saved_models/`

---

## 📊 Models Used

- **Logistic Regression** → Classification of fare ranges
- **Naive Bayes** → Efficient classification for high-dimensional features
- **DBSCAN** → Clustering rides based on spatial/temporal features

---

## 📷 Screenshots

See `/screenshots/` for:
- Spark UI screenshots
- DAGs for workflow orchestration
- Output visualizations and cluster maps

---

## 📄 Reports and Presentation

- 📑 Final report: `reports/report.pdf`
- 📽️ Presentation: `presentation/ppt.pptx`

---

## 📚 Requirements

```txt
pyspark
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
jupyter
```

---
