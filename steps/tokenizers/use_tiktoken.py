import csv
import tiktoken

embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002

encoding = tiktoken.get_encoding(embedding_encoding)

with open('input_output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['input', 'output'])
    while True:
        user_input = input("Enter a sentence: ")
        output = encoding.encode(user_input)
        writer.writerow([user_input, output])
        print(output)