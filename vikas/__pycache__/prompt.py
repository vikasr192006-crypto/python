template = (
    "You are a patient python tutor."
    "Explan {} for a beginners,"
    "Give one example,and keep the explanation within {} words."
    )

prompt = template.format("for loops",80)

print(prompt)