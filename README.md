**AutoJudge – Programming Problem Difficulty Prediction**

    # 1. Project Overview

        Online competitive programming platforms (such as Codeforces, CodeChef, Kattis) classify problems into difficulty levels like Easy, Medium, and Hard, often accompanied by a numerical difficulty score.
        This process is typically based on human judgment and user feedback.

        AutoJudge is a machine learning–based system project that automatically predicts the difficulty of a programming problem using only its textual description, without relying on solution code or user statistics.

        The system predicts:
        . Difficulty Class → Easy / Medium / Hard (classification)
        . Difficulty Score → Numerical value between 1 and 10 (regression)

        A simple web interface is provided for real-time predictions using trained models.

    # 2. Dataset Used

        File: data/problems_data.jsonl

        Each problem contains:
        . title
        . description
        . input description
        . output description
        . examples
        . problem class
        . problem score
        . url

    # 3. Project Structure

        AUTOJUDGE WINTER PROJECT/
        │
        ├── data/
        │ ├── problems_data.jsonl
        │ └── preprocessed_data.csv
        │
        ├── trained_models/
        │ ├── classification_model.joblib
        │ └── regression_model.joblib
        |
        ├── data_preprocessing.ipynb
        ├── model1.ipynb (Classification model)
        ├── model2.ipynb (Regression model)
        ├── app.py (Web interface)
        ├── requirements.txt
        ├── README.md
        └── Demo video

    # 4. Approach and Models Used

        i. Data Preprocessing

            Combined all text fields into a single full_text

            Handled missing values

            Engineered numeric features:
                . Text length
                . Count of mathematical symbols

            Saved processed data for reuse

        ii. Feature Extraction (included in the file model1.ipynb and model2.ipynb)

            TF-IDF vectorization (max_features = 5000)

            Numeric features concatenated with TF-IDF vectors

        iii. Model 1: Difficulty Classification

            Model: Random Forest Classifier

            Input: TF-IDF + numeric features

            Output: Easy / Medium / Hard

        iv. Model 2: Difficulty Score Prediction

            Model: Random Forest Regressor

            Input: TF-IDF + numeric features (Same features as classification model)

            Output: Difficulty score (1–10)

    # 5. Evaluation Metrics and Results

        i. Classification Performance

            Random Forest accuracy: 0.5455650060753341

            Confusion matrix:
                [[ 30  66  40]
                [  8  376  41]
                [ 14  205  43]]

            Most errors occur between Medium and Hard classes due to similar textual patterns

        ii. Regression Performance

            MAE: ~1.69

            RMSE: ~2.04

            R² Score: ~0.13

    # 6. Web Interface

        Web interface built using Streamlit:

        Paste the complete problem statement into a single text box (unprocessed data)

        Click the Predict button

        View:
        . Predicted difficulty score
        . Predicted difficulty class

        Note: Class and score are predicted independently with different models and may not always agree.

        The application loads pre-trained models.

    # 7. Steps to Run the Project Locally

        Note: If the required libraries (requirements.txt) are already installed on your system, you can skip creating a virtual environment and run the project directly.

        Step 1: Creat and Activate Virtual Environment (Optinal)
        python -m venv mylib
        mylib\Scripts\activate

        Step 2: Install Required Libraries
        pip install -r requirements.txt

        Step 3: Run the Web Application
        streamlit run app.py

        Open the local URL shown in the terminal

    # 8. Demo Video

        Included in repository

    # 9. My Details

        Name: Dinesh Sunda
        Project: AutoJudge – Programming Problem Difficulty Prediction
        Enrollment no. 24117044
        Mobile no. 7852066006
        2nd year, mech
