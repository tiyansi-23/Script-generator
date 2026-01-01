from llm.gemini import get_gemini_llm

def cta_agent(state):
    llm = get_gemini_llm()

    prompt = f"""
SYSTEM:
You are a conversion optimization expert.

SCRIPT:
{state['script']}

TASK:
Create 3 CTA options.

OUTPUT (JSON):
{{
  "primary_cta": "...",
  "alternative_cta_1": "...",
  "alternative_cta_2": "..."
}}
"""

    response = llm.invoke(prompt)
    state["cta"] = response.content
    return state
