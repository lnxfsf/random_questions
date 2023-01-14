
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com/'
})

# Get a random question from the database
def get_random_question():
    ref = db.reference("questions")
    questions = ref.get()
    if questions:
        # Select a random question from the list
        question = random.choice(list(questions.values()))
        return question["question"]
    else:
        return None

# Example usage
question = get_random_question()
if question:
    print(question)
else:
    print("No questions found in the database.")





# replace the databaseURL with appropriate values for your Firebase project
# make sure you have the firebase-admin python package installed and you should have the proper access credentials to the database
