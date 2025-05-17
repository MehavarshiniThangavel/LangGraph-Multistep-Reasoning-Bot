*Multi-Step Reasoning Bot*

A multi-step reasoning chatbot using LangGraph and OpenAI GPT-3.5 Turbo that mimics human problem-solving by breaking down question answering into sequential reasoning steps.

Overview: 

This bot processes user questions in three stages:

Thought: Understand and plan what information to gather.

Research: Retrieve or simulate collecting relevant data.

Answer: Combine information and generate a final response.

This structured flow leads to more accurate and insightful answers by clearly separating reasoning and action.


Real-Time Example

User Input:

“What are the health benefits of green tea?”

Step 1 – Thought:
The bot thinks:
“I need to find out scientifically proven health benefits of green tea, such as antioxidants, heart health, or weight loss effects.”

Step 2 – Research:
The bot gathers info:
“Green tea contains antioxidants called catechins which can improve brain function, reduce the risk of heart disease, and aid fat burning.”

Step 3 – Answer:
The bot responds:
“Green tea offers several health benefits including improved brain function, heart health support, and weight management due to its rich antioxidant content called catechins.”


Project Structure
 
.
├──  main.py                
├──  steps/
│    ├── step1_thought.py   
│    ├── step2_research.py 
│   └── step3_answer.py    
├── requirements.txt
└── .env





Enter your question when prompted, and the bot will reply after stepwise reasoning.


Thankyou
