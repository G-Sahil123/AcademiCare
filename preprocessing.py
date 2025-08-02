import pandas as pd
import joblib

def preprocess_binary(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Binary mappings (from Yes/No in form)
    binary_cols = ["Displaced Student", "Is Debtor", "Tuition Fees Up-to-Date", "Scholarship Holder"]
    for col in binary_cols:
        df[col] = df[col].map({"Yes": 1, "No": 0})

    # Gender mapping
    df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})

    # Daytime/Evening mapping
    df["Daytime/Evening Attendance"] = df["Daytime/Evening Attendance"].map({
        "Daytime": 0,
        "Evening": 1
    })

    # Marital Status mapping
    df["Marital Status"] = df["Marital Status"].map({
        "Single": 0,
        "Married": 1,
        "Divorced": 2,
        "Facto Union": 3,
        "Legally Separated": 4,
        "Widower": 5
    })

    return df

def transform(df: pd.DataFrame)->pd.DataFrame:

    encoder = joblib.load("catboost_encoder.pkl")

    df_processed = preprocess_binary(df)

    categorical_cols = [
    'Application Mode', 'Previous Qualification',
    "Father's Occupation", 'Course Name'
    ]

    df_processed[categorical_cols] = encoder.transform(df_processed[categorical_cols])

    return df_processed


