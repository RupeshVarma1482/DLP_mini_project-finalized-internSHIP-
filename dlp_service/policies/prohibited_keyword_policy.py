import zipfile
import csv

# valid_file_types = [".txt", ".doc", ".docx", ".csv", ".xlsx", ".pdf"]
prohibited_words = ["apple", "banana", "orange"]

def check_policy(metadata, file):
    print(f"metadata: {metadata}")
    global valid_file_types
    file.seek(0)
    data = file.read(10)
    print(f"data: {data}")
    if data.startswith(b"%PDF-"):
        print(f"file is PDF")
        file.seek(0)
    elif zipfile.is_zipfile(file):
        file.seek(0)
        with zipfile.ZipFile(file) as z:
            names = z.namelist()
            if any(name.startswith("word/") for name in names):
                print(f"file is DOCX")
                file.seek(0)
            elif any(name.startswith("xl/") for name in names):
                print(f"file is XLSX")
                file.seek(0)
    else:
        file.seek(0)
        try:
            text = data.decode("utf-8");
            print(f"text: {text}")
            print(f"prolly file is TXT or CSV")
            if any(word in text for word in prohibited_words):
                return {
                    "allowed": true,
                    "reason": "prohibited word not found in TXT/CSV file"
                }
        except UnicodeDecodeError:
            print(f"file is NOT TXT")
            print(f"file might be of non registered types")