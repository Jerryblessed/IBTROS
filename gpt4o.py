# import openai
# from openai import AzureOpenAI

# # Azure OpenAI API details
# api_base = "https://thisisoajo.openai.azure.com/"  # Replace with your Azure OpenAI resource URL
# model = "gpt-4o"
# api_key = "9I4UEJweVUdih04Uv8AXcAxs5H8jSQRfwaugcSQYHcI882wSpFvqJQQJ99BAACL93NaXJ3w3AAABACOGkv4f"  # Replace with your actual API key
# api_version = "2023-06-01-preview"

# def chat_with_gpt(prompt):
#     """Interact with GPT-4o via Azure OpenAI API."""
#     client = AzureOpenAI(
#         api_key=api_key,
#         api_version=api_version,
#         base_url=f"{api_base}/openai/deployments/{model}"
#     )

#     response = client.chat.completions.create(
#         model=model,
#         messages=[
#             {
#                 "role": "system",
#                 "content": (
#                     "Routes List:\n"
#                     "Your roles is "
#                 )
#             },
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=100,
#         temperature=0.7,
#     )
#     return response.choices[0].message.content.strip()

# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             print("Goodbye!")
#             break
#         response = chat_with_gpt(user_input)
#         print("GPT-4o:", response)

from ibtros_check import process_query

# Example user input (even if slightly incomplete or with errors)
 
def my_function():
    user_input = """\
    From: Digital Bridge Institution 
    To: Azzess bank blc Garki Branch
    """
    return user_input

my_varible = my_function()

final_output = process_query(my_varible)
print(final_output)
