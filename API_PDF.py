import PyPDF2
from openai import OpenAI

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        # Read all pages of the PDF
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text

pdf_path = "document.pdf"
try:
    # Attempt to extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)
except FileNotFoundError:
    print(f"Error: The file PDF '{pdf_path}' was not found.")
    exit(1)

# Create the prompt to send to the language model
prompt = f"""
Write 10 multiple choice questions on Artificial Intelligence and steepest descent according to the text below. 
Each question should have 5 possible answers and only one of them should be correct. 
The audience answering the questions is at the university level.
The questions and answers must be in Greek. 
The difficulty level of each question is on a Likert scale of 1 to 5 (1 = very easy and 5 = very difficult).
Of the 10 questions, one should have difficulty level 1, two difficulty level 2, three difficulty level 3, 
two difficulty level 4, and the rest difficulty level 5.

Text:
{pdf_text[:3000]}
"""

# Initialize OpenAI client (insert your API key)
client = OpenAI(
    api_key="enter your API key"
)

# Request the model to generate the questions
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Extract the output text from the model's response
output_message = completion.choices[0].message.content

# Save the generated questions to a text file
with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(output_message)

print("The questions were saved to the file 'output.txt'")
