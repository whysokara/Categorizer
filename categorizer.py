## Import Modules
import ollama
import os

model = "llama3.2"
input_file = "./data/list.txt"
output_file = "./data/categorizedlist.txt"

## Check if file exsists or not
if not os.path.exists(input_file):
    print(f"Input file {input_file} not found")
    exit()

## Read the file
with open(input_file, "r") as f:
    items = f.read().strip()
    print(items)

## Prompt

prompt = f"""
You are an assistant that categories and sorts the grocerry items.

Here is a list of grocerry items:
{items}

Please:

1. Categories these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, Stationary etc
2. Sort items alphabetically within each category
3. Present the categorized list in a clear and organised manner, using bullet points or numbering
"""



try:
    response = ollama.generate(model=model,prompt=prompt)
    generated_text = response.get("response","")

    ## write categorized list to output file

    with open(output_file,'w') as f:
        f.write(generated_text.strip())

    print(f"Categorized grocery list has been saved to {output_file}")

except Exception as e:
    print("An error occured:", str(e) )
