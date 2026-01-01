from llm.gemini import get_gemini_llm

def audience_agent(state):
    llm = get_gemini_llm()

    prompt = f"""
SYSTEM:
You are a consumer psychology expert.

PRODUCT ANALYSIS:
{state['product_summary']}

TASK:
Identify the most realistic target audience.

OUTPUT (JSON ONLY):
{{
  "primary_audience": {{
    "age_range": "...",
    "lifestyle": "...",
    "pain_points": ["...", "..."],
    "buying_motivation": "..."
  }},
  "secondary_audience": {{
    "age_range": "...",
    "use_case": "..."
  }}
}}

RULE:
Avoid words like "everyone", "all people".
"""

    response = llm.invoke(prompt)
    state["target_audience"] = response.content
    return state
