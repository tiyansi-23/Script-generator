from langgraph.graph import StateGraph, END
from utils.state import AdState

from agents.product_agent import product_agent
from agents.audience_agent import audience_agent
from agents.tone_agent import tone_agent
from agents.hook_agent import hook_agent
from agents.script_agent import script_agent
from agents.cta_agent import cta_agent
from agents.polish_agent import polish_agent

def create_ad_graph():
    graph = StateGraph(AdState)

    graph.add_node("product", product_agent)
    graph.add_node("audience", audience_agent)
    graph.add_node("tone", tone_agent)
    graph.add_node("hook", hook_agent)
    graph.add_node("script", script_agent)
    graph.add_node("cta", cta_agent)
    graph.add_node("polish", polish_agent)

    graph.set_entry_point("product")

    graph.add_edge("product", "audience")
    graph.add_edge("audience", "tone")
    graph.add_edge("tone", "hook")
    graph.add_edge("hook", "script")
    graph.add_edge("script", "cta")
    graph.add_edge("cta", "polish")
    graph.add_edge("polish", END)

    return graph.compile()
