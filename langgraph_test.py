from langgraph.graph import StateGraph
# from langgraph.node import Node
# from langgraph.edge import Edge
# from langgraph.graph import Graph
# from langgraph.graph import GraphBuilder
from langchain.messages import AnyMessage, AIMessage, HumanMessage
from typing_extensions import TypedDict

from IPython.display import display, Image


class State(TypedDict):
    messages: list[AnyMessage]
    extra_field: int

def node(state: State):
    messages = state["messages"]
    new_messages = AIMessage(content="Hello, how can I help you?")  # Example AI message
    return {"messages": messages + [new_messages], 
            "extra_field": state["extra_field"] + 1
            }

builder = StateGraph(State)
builder.add_node("node", node)
builder.set_entry_point("node")
graph = builder.compile()

print(graph.get_graph().draw_mermaid())

display(Image(graph.get_graph().draw_mermaid_png))


