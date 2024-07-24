from llama_cpp import Llama

import os

model =os.environ['MYSTRAL_7B_INSTRUCT']  # instruction model
llm = Llama(model_path=model, n_ctx=8192, n_batch=512, n_threads=7, n_gpu_layers=2, verbose=True, seed=42)
system = """
Follow the instructions below to complete the task.
"""

user = """
Create a PHP script to scan a directory and print the contents of the directory.
"""

message = f"<s>[INST] {system} [/INST]</s>{user}"
output = llm(message, echo=True, stream=False, max_tokens=4096)
print(output['usage'])
output = output['choices'][0]['text'].replace(message, '')
print(output)