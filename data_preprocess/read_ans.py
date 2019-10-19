import pandas as pd
csv_input = pd.read_csv(filepath_or_buffer="answer.txt", encoding="ms932", sep=",")
print(csv_input.values[0])