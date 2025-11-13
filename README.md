## Depatment of Digital Systems in Sparta, Conference 2025

### *Welcome* to Dept._DS_Sparti_Students_Conference_2025 📜🎓

There are three different codes in this repository:
1) API_Conf_DS_2025.py, which has as a prompt TXT 
2) API_PDF.py, which has as a prompt PDF
3) Steepest_Descent.py, where it describes the Steepest Descent Method in detail with comments ✅

In the **first** code, the following happens: ✅
- The code first imports the openai library and creates a client object that connects to the OpenAI API, using the API key provided by the user.
- It then attempts to open the file prompt.txt in read mode and read its contents. If the file does not exist, an error message is displayed and the program terminates.
- After reading the file content, the program sends this prompt to the OpenAI gpt-4o-mini model via the client.chat.completions.create() method. This method creates a completion response from the model based on the text given to it. The result is stored in the completion variable.
- From this output, the program extracts the content of the model's first response message and stores it in the variable output_message. It then opens or creates a new file named output.txt and writes the model's response into it.
- Finally, it displays the message “Output has been written to output.txt” on the console, informing the user that the process was completed successfully and displaying the queries I asked him to create.


In the **second** code, the following happens: ✅
-
