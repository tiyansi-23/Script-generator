from llm.gemini import get_gemini_llm
import json

def product_agent(state):
    llm = get_gemini_llm()

    prompt = f"""
SYSTEM:
You are a detail-oriented product analyst. Your task is to extract and structure all available information about the product.

PRODUCT INPUT:
{state['product_info']}

TASK:
Analyze the product information and provide a detailed, structured output.

OUTPUT FORMAT (JSON):
{{
  "product_name": "[Exact product name from input or generated if not provided]",
  "product_type": "[Specific type/category]",
  "key_ingredients": ["list", "of", "key", "ingredients"],
  "key_features": ["specific", "features", "from", "input"],
  "target_use_cases": ["primary", "use", "cases"],
  "scientific_backing": ["any", "scientific", "claims"],
  "unique_selling_points": ["what", "makes", "it", "unique"]
}}

RULES:
1. ONLY include information explicitly mentioned in the input
2. If information is missing, leave the field as an empty array []
3. Be specific - avoid generic terms
4. Preserve any technical or scientific terms from the input
5. Keep the output as a valid JSON object
"""

    try:
        response = llm.invoke(prompt)
        # Parse the response to ensure it's valid JSON
        product_data = json.loads(response.content)
        
        # Create a more readable summary for the script agent
        summary_parts = []
        if "product_name" in product_data and product_data["product_name"]:
            summary_parts.append(f"Product: {product_data['product_name']}")
        if "product_type" in product_data and product_data["product_type"]:
            summary_parts.append(f"Type: {product_data['product_type']}")
        if "key_ingredients" in product_data and product_data["key_ingredients"]:
            summary_parts.append(f"Key Ingredients: {', '.join(product_data['key_ingredients'])}")
        if "key_features" in product_data and product_data["key_features"]:
            summary_parts.append(f"Features: {', '.join(product_data['key_features'])}")
        if "target_use_cases" in product_data and product_data["target_use_cases"]:
            summary_parts.append(f"Best for: {', '.join(product_data['target_use_cases'])}")
        if "scientific_backing" in product_data and product_data["scientific_backing"]:
            summary_parts.append(f"Backed by: {', '.join(product_data['scientific_backing'])}")
        if "unique_selling_points" in product_data and product_data["unique_selling_points"]:
            summary_parts.append(f"Why it's special: {', '.join(product_data['unique_selling_points'])}")
        
        state["product_summary"] = "\n".join(summary_parts)
        state["product_data"] = product_data  # Store the structured data for other agents
        
    except Exception as e:
        # Fallback to original input if parsing fails
        state["product_summary"] = state['product_info']
        
    return state
