# Student Performance Index Prediction  

This project leverages machine learning techniques to predict academic scores of students based on a variety of features. The goal is to provide an intuitive and accurate model for evaluating student performance, helping educators and institutions gain insights for better academic planning and resource allocation.  

---

## Features  

- **Accurate Prediction Model**: Implements machine learning algorithms like XGBoost and Ridge Regressor for high-accuracy predictions. Achieved an R-squared score of 88.59%.  
- **User-Friendly Web Application**: Developed using Flask for real-time predictions.  
- **Cloud Deployment**: Hosted on AWS EC2 for robust and scalable access.  
- **Automation Integration**: Deployed via GitHub Actions for seamless CI/CD.  
- **Interactive Visualization**: Provides data-driven insights with visualization support.  

---

## Tech Stack  

- **Programming Languages**: Python  
- **Machine Learning Frameworks**: XGBoost, Scikit-learn, CatBoost  
- **Web Framework**: Flask  
- **Deployment**: Docker, AWS EC2  
- **CI/CD Tools**: GitHub Actions  
- **Data Visualization**: Matplotlib, Seaborn  

---

## File Structure  

```plaintext
performance_index_project/
│
├── notebook/
│   ├── data/
│   │   └── stud.csv                 # Public Dataset
│   ├── EDA STUDENT.ipynb            # EDA and visualization of the data
│   └── MODELTRAINING.ipynb          # Model Training Notebook
│
├── artifacts/                 
│   ├── model.pkl                    # Pretrained model for prediction
│   ├── test.csv                     # Dataset used for testing
│   ├── train.csv                    # Dataset used for training
│   └── processor.pkl                # Preprocessor used during prediction stage
│
├── src/                             # Main scripts
│   ├── components/         
│   │    ├── data_ingestion.py       # Data Ingestion file
│   │    ├── data_transformation.py  # Data transformation file
│   │    └── model_trainer.py        # Model Training file
│   │
│   ├── pipeline/       
│   │    └── predict_pipeline.py     # Prediction Pipeline file
│   │
│   ├── exception.py                 # Exception Handling file
│   ├── logger.py                    # Logger file to log activities
│   └── utils.py                     # Utility script
│
├── templates/                       # HTML templates for the web app
│   ├── index.html                   # Welcome page
│   └── home.html                    # Results page
│
├── app.py                           # Main Flask application script
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker file 
└── README.md                        # Project documentation