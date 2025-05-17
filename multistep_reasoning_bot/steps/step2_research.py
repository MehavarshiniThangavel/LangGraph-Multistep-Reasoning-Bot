import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def step2_research(state):
    print("🔍 Step 2: Researching...")
    thought = state["thought"]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert researcher."},
            {"role": "user", "content": f"Do some focused research based on this reasoning:\n\n{thought}"}
        ]
    )
    research = response.choices[0].message.content
    return {**state, "research": research}



