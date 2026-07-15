import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
<<<<<<< HEAD
from langdetect import detect
from deep_translator import GoogleTranslator

=======
from sklearn.model_selection import train_test_split          # ← ADD
from sklearn.metrics import classification_report, confusion_matrix  # ← ADD
from langdetect import detect
from deep_translator import GoogleTranslator


>>>>>>> f36f5b7d3817ef6c49a4ac12405051899e1f77ca
# 🔹 Preprocess function
def preprocess_text(text):
    try:
        if detect(text) != 'en':
            text = GoogleTranslator(source='auto', target='en').translate(text)
    except:
        pass
    return text.lower()

# 🔹 Load dataset
df = pd.read_excel("../dataset/kdmc_data.xlsx")

<<<<<<< HEAD
# 🔹 Rename columns (IMPORTANT)
=======
# 🔹 Rename columns
>>>>>>> f36f5b7d3817ef6c49a4ac12405051899e1f77ca
df.rename(columns={
    "Complaint Description": "complaint",
    "Complaint Type": "category"
}, inplace=True)

# 🔹 Remove nulls
df = df[['complaint', 'category']].dropna()

# 🔹 Clean text
<<<<<<< HEAD
df['clean_text'] = df['complaint'].astype(str).apply(preprocess_text)
=======
df['clean_text'] = df['complaint'].astype(str).str.lower()
>>>>>>> f36f5b7d3817ef6c49a4ac12405051899e1f77ca

# 🔹 Features & labels
X = df['clean_text']
y = df['category']

<<<<<<< HEAD
# 🔹 Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

# 🔹 Model
model = LogisticRegression(max_iter=200)
model.fit(X_vec, y)

# 🔹 Save
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained successfully on KDMC dataset")
=======
# ─────────────────────────────────────────────
# 🔹 CHANGED: Split into train and test sets
# ─────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 🔹 Vectorization — fit ONLY on training data
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec  = vectorizer.transform(X_test)    # ← transform only, no fit

# 🔹 Model — train ONLY on training data
model = LogisticRegression(max_iter=200)
model.fit(X_train_vec, y_train)

# ─────────────────────────────────────────────
# 🔹 NEW: Evaluate on test set
# ─────────────────────────────────────────────
y_pred = model.predict(X_test_vec)

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

print("🔲 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 🔹 Save model and vectorizer (trained on full data for production)
# Re-train on full data before saving
X_full_vec = vectorizer.fit_transform(X)
model.fit(X_full_vec, y)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\n✅ Model trained and saved successfully on KDMC dataset")
>>>>>>> f36f5b7d3817ef6c49a4ac12405051899e1f77ca
