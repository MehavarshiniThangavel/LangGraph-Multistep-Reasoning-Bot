import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def step3_answer(state):
    print("✅ Step 3: Answering...")
    research = state["research"]
    question = state["question"]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that gives final answers based on research."},
            {"role": "user", "content": f"Using the following research:\n\n{research}\n\nAnswer the question:\n\n{question}"}
        ]
    )
    answer = response.choices[0].message.content
    return {**state, "answer": answer}
