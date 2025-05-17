import os
from dotenv import load_dotenv
from typing import TypedDict, Optional
from langgraph.graph import StateGraph

from steps.step1_thought import step1_thought
from steps.step2_research import step2_research
from steps.step3_answer import step3_answer 

load_dotenv()

# Define state schema
class GraphState(TypedDict):
    question: str
    thought: Optional[str]
    research: Optional[str]
    answer: Optional[str]

# Initialize the graph
graph = StateGraph(GraphState)

# Add steps with unique node names that don’t conflict with state keys
graph.add_node("step1_thought", step1_thought)
graph.add_node("step2_research", step2_research)
graph.add_node("step3_answer", step3_answer)

# Define edges
graph.set_entry_point("step1_thought")
graph.add_edge("step1_thought", "step2_research")
graph.add_edge("step2_research", "step3_answer")
graph.set_finish_point("step3_answer")

# Compile the graph
app = graph.compile()

# Run the graph
if __name__ == "__main__":
    question = input("Enter your question: ")
    result = app.invoke({"question": question})
    print("\nFinal Answer:", result["answer"])
