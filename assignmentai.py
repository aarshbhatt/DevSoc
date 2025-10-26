import openai
from openai import OpenAI

file_path_input = input("Enter the file path: ")
file_path_output = input("Enter the file path (should not be pre-existing): ")
check =file_path_input.find("\\")
while check!=-1:
    file_path_input = file_path_input.replace("\\","/")
    check = file_path_input.find("\\")

try:
  with open(file_path_input,"r") as file1:
    content = file1.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")


client = openai.OpenAI(api_key="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",
                       base_url="https://openrouter.ai/api/v1")

chat = client.chat.completions.create(
    model="deepseek/deepseek-r1-0528-qwen3-8b:free",
    messages=[
        {  "role":"user", "content":content } ]
)


check = file_path_output.find("\\")
while check!=-1:
    file_path_output = file_path_output.replace("\\", "/")
    check = file_path_output.find("\\")

with open(file_path_output,"x",encoding="utf-8") as file2:
    file2.writelines(chat.choices[0].message.content)

print("Your output file is created successfully at the provided path")