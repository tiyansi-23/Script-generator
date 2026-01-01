from llm.gemini import get_gemini_llm

def polish_agent(state):
    llm = get_gemini_llm()

    prompt = f"""
SYSTEM:
You are a professional editor and compliance reviewer.

SCRIPT:
{state['script']}

CTA OPTIONS:
{state['cta']}

TASK:
Refine language, remove repetition, improve flow,
and merge into one final professional advertisement.

FINAL OUTPUT:
Plain text ad script with CTA at the end.
"""

    response = llm.invoke(prompt)
    state["final_ad"] = response.content
    return state
