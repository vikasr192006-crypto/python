import json
quiz = {                                                      
    "question": "what does len() return?",
    "answer": "the number of items"
}
text = json.dumps(quiz)
print(text)
parsed = json.loads(text)
print(parsed["answer"])