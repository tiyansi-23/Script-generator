from llm.gemini import get_gemini_llm

def hook_agent(state):
    llm = get_gemini_llm()

    prompt = f"""
SYSTEM:
You are a professional ad copywriter.

TONE STRATEGY:
{state['tone']}

TASK:
Write 3 short hooks.

RULES:
- Max 12 words
- No exaggeration
- No false promises

OUTPUT (JSON):
{{
  "hooks": ["...", "...", "..."]
}}
"""

    response = llm.invoke(prompt)
    state["hook"] = response.content
    return state
