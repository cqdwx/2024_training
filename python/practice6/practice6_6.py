favorite_languages = {
    'alice': 'python',
    'bob': 'java',
    'charlie': 'javascript',
    'david': 'python'
}

survey_participants = ['alice', 'bob', 'emma', 'frank']

for participant in survey_participants:
    if participant in favorite_languages:
        print(f"Thank you, {participant.title()}, for participating in the survey!")
    else:
        print(f"Dear {participant.title()}, we invite you to participate in the survey.")
