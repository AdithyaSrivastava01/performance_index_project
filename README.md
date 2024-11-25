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
- **Machine Learning Frameworks**: XGBoost, Ridge Regressor  
- **Web Framework**: Flask  
- **Deployment**: AWS EC2  
- **CI/CD Tools**: GitHub Actions  
- **Data Visualization**: Matplotlib, Seaborn  

---

## File Structure  

```plaintext
performance_index_project/
│
├── app.py                  # Main Flask application script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── static/                 # Static files (CSS, JS, images)
│   └── styles.css          # Styling for the web app
│
├── templates/              # HTML templates for the web app
│   ├── index.html          # Homepage
│   └── result.html         # Results page
│
├── models/                 # Machine learning models
│   └── trained_model.pkl   # Pretrained model for prediction
│
├── data/                   # Data-related files
│   ├── dataset.csv         # Dataset used for training
│   └── processed_data.pkl  # Preprocessed data for the model
│
└── utils/                  # Utility scripts
    ├── preprocess.py       # Data preprocessing functions
    └── visualize.py        # Functions for creating visualizations
