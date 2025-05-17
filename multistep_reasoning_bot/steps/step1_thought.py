import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def step1_thought(state):
    print("🤔 Step 1: Thinking...")
    question = state["question"]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a thoughtful assistant who reasons through questions."},
            {"role": "user", "content": f"Think step-by-step about the following question:\n\n{question}"}
        ]
    )
    thought = response.choices[0].message.content
    return {**state, "thought": thought}
