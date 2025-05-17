# 🧠 Multi-Step Reasoning Bot using LangGraph

   This project is a Multi-Step Reasoning Bot built using LangGraph. It mimics human-like thinking by breaking down the answering process into three logical steps: generating an initial thought, gathering relevant information, and synthesizing a final answer

---

## 📌 Features

- Modular multi-step reasoning: Thought → Research → Answer  
- Clear intermediate outputs for explainability  
- Built with LangGraph for stateful graph execution  
- Easy to extend and customize  

---

## 🏗️ How It Works

The bot processes user questions through **three sequential steps**, updating a shared state dictionary:

1. **Thought Generation (`step1_thought`)**  
   Interprets the question and formulates an initial approach.  
2. **Research (`step2_research`)**  
   Gathers relevant information or facts based on the thought.  
3. **Answer Synthesis (`step3_answer`)**  
   Combines the previous insights to produce a final answer.



The flow is orchestrated as:

     [step1_thought] → [step2_research] → [step3_answer]



---

## 🧪 Example Session

```
Enter your question: Why is the sky blue?

Final Answer: The sky appears blue because of a phenomenon called Rayleigh scattering. Molecules in the atmosphere scatter shorter wavelengths of light, like blue, more than longer wavelengths like red.



🧾 Full Internal State Example

{
  "question": "Why is the sky blue?",
  "thought": "This seems to be a physics question about light and the atmosphere.",
  "research": "Rayleigh scattering causes shorter blue wavelengths to scatter more than red, making the sky appear blue to our eyes.",
  "answer": "The sky appears blue because of a phenomenon called Rayleigh scattering. Molecules in the atmosphere scatter shorter wavelengths of light, like blue, more than longer wavelengths like red."
}

🧩 Project Structure




├── main.py
├── steps/
│   ├── step1_thought.py
│   ├── step2_research.py
│   └── step3_answer.py
├── .env
└── README.md


🚀 Getting Started

1. Clone the Repository

cd multistep-reasoning-bot


2. Install Dependencies

    pip install -r requirements.txt


3. Configure Environment Variables

    OPENAI_API_KEY=your_openai_key_here


4. Run the Bot

    python main.py

🛠️ Built With
LangGraph
Python
python-dotenv

