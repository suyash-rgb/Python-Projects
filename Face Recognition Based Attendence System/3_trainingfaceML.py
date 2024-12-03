from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pickle
import os

# Initializing the embedding and recognizer file paths
embeddingFile = "output/embeddings.pickle"
recognizerFile = "output/recognizer.pickle"
labelEncFile = "output/le.pickle"

print("Loading face embeddings...")
data = pickle.loads(open(embeddingFile, "rb").read())

print("Encoding labels...")
labelEnc = LabelEncoder()
labels = labelEnc.fit_transform(data["names"])

# Check the unique labels
unique_labels = set(labels)
if len(unique_labels) <= 1:
    raise ValueError(f"The number of classes has to be greater than one; got {len(unique_labels)} class(es)")

print(f"Unique labels: {unique_labels}")

print("Training model")
recognizer = SVC(C=1.0, kernel="linear", probability=True)
recognizer.fit(data["embeddings"], labels)

# Ensure the output directory exists
output_dir = os.path.dirname(recognizerFile)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the recognizer model
with open(recognizerFile, "wb") as f:
    f.write(pickle.dumps(recognizer))

# Save the label encoder
with open(labelEncFile, "wb") as f:
    f.write(pickle.dumps(labelEnc))

print("Recognizer and label encoder saved successfully.")
