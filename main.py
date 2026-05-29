def simulate_llm_response(prompt: str) -> str:
    """
    Simulates an LLM's response based on prompt clarity and specificity.
    This function demonstrates how vague prompts lead to generic/unhelpful
    responses, while clear, specific prompts yield better results.
    """
    prompt_lower = prompt.lower()

    # --- Illustrates a common prompt error: vagueness and lack of context ---
    # If the prompt is too generic and lacks a clear subject.
    if "it" in prompt_lower and not any(keyword in prompt_lower for keyword in ["product x", "shipping", "return policy", "features"]):
        return "I need more context. What 'it' are you referring to? Please be more specific."

    # --- Illustrates a slightly improved but still ambiguous prompt ---
    # If the prompt mentions 'product' but doesn't specify which one.
    if "product" in prompt_lower and "product x" not in prompt_lower and "product y" not in prompt_lower:
        return "Which product are you interested in? To get the best answer, please specify the product name."

    # --- Illustrates a prompt that is specific about the subject, but general in query ---
    # The product is specified, but the question is still broad.
    if "product x" in prompt_lower and not any(keyword in prompt_lower for keyword in ["features", "price", "return policy", "compare"]):
        return "Product X is a high-performance device known for its durability. What specific aspects of Product X are you curious about?"

    # --- Illustrates a good, specific prompt leading to a helpful response ---
    # Clear subject and specific information requested.
    if "features of product x" in prompt_lower:
        return "Product X key features include: 1. Long-lasting battery, 2. Water-resistant design, 3. High-resolution display, 4. Fast processor. It's ideal for outdoor use."

    # --- Illustrates another good, specific prompt with a clear intent ---
    # Clear subject and specific policy requested.
    if "return policy" in prompt_lower and "product x" in prompt_lower:
        return "Our return policy for Product X allows returns within 30 days of purchase, provided the item is in its original packaging and condition. A full refund will be issued."

    # --- Illustrates a prompt requiring comparison, demonstrating specific intent ---
    # Clear intent to compare two specific items.
    if "compare product x and product y" in prompt_lower:
        return "Product X excels in battery life and ruggedness, while Product Y offers a superior camera and lighter design. Your choice depends on your primary use case."

    # Default fallback for unhandled cases
    return "I'm sorry, I couldn't understand your request. Could you please rephrase it with more details?"

# --- Demonstration of different prompt qualities ---

print("--- Demonstrating Prompt Quality Impact ---")
print("\nScenario: Asking about 'Product X' or general policies.")

# Example 1: Vague prompt - common error
prompt1 = "Tell me about it."
print(f"\nPrompt 1 (Vague): '{prompt1}'")
print(f"Response: {simulate_llm_response(prompt1)}")
# This prompt is too generic, lacking any specific subject or context.
# The simulated LLM correctly identifies the lack of context.

# Example 2: Slightly better, but still ambiguous - common error
prompt2 = "What about the product?"
print(f"\nPrompt 2 (Ambiguous Product): '{prompt2}'")
print(f"Response: {simulate_llm_response(prompt2)}")
# This prompt mentions "product" but doesn't specify which one, leading to a request for clarification.

# Example 3: Specific product, but still general - improved but could be better
prompt3 = "Tell me about Product X."
print(f"\nPrompt 3 (Specific Product, General Query): '{prompt3}'")
print(f"Response: {simulate_llm_response(prompt3)}")
# This prompt identifies the product but doesn't ask for specific information,
# so the LLM provides a general overview and asks for more detail.

# Example 4: Good prompt - clear, specific, and detailed
prompt4 = "What are the key features of Product X?"
print(f"\nPrompt 4 (Good - Specific Features): '{prompt4}'")
print(f"Response: {simulate_llm_response(prompt4)}")
# This prompt is clear and asks for specific information ("key features"),
# allowing the simulated LLM to provide a direct and helpful answer.

# Example 5: Another good prompt - clear intent for a policy
prompt5 = "What is the return policy for Product X?"
print(f"\nPrompt 5 (Good - Specific Policy): '{prompt5}'")
print(f"Response: {simulate_llm_response(prompt5)}")
# This prompt clearly states the product and the specific policy requested,
# resulting in a precise and relevant response.

# Example 6: Prompt requiring comparison - good if all info is available
prompt6 = "Compare Product X and Product Y."
print(f"\nPrompt 6 (Good - Comparison Request): '{prompt6}'")
print(f"Response: {simulate_llm_response(prompt6)}")
# This prompt clearly asks for a comparison, and the LLM provides one based on its "knowledge."
