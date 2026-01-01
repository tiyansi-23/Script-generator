from llm.gemini import get_gemini_llm

def tone_agent(state):
    llm = get_gemini_llm()

    prompt = f"""
SYSTEM:
You are a brand strategist.

AUDIENCE PROFILE:
{state['target_audience']}

TASK:
Select the best advertising tone.

OUTPUT (JSON):
{{
  "recommended_tone": "...",
  "reasoning": "...",
  "tone_guidelines": ["...", "..."]
}}
"""

    response = llm.invoke(prompt)
    state["tone"] = response.content
    return state
