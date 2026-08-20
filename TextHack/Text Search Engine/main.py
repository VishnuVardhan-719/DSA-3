import os

# Step 1 : Read the document

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sample.txt")

with open(file_path, "r") as file:
    text = file.read()

# Step 2 : Convert text to lowercase

text = text.lower()

# Step 3 : Display the document

print("Document:\n")
print(text)

# Step 4 : Take user input

query = input("\nEnter Search Word : ")

# Step 5 : Convert query to lowercase

query = query.lower()

# Step 6 : Search

if query in text:
    print("\nResult : Word Found")
else:
    print("\nResult : Word Not Found")

