import os
import sys
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
# Setup
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_instructions(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            instructions = file.read()
        return instructions
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred while reading the file:", e)

def get_messages(queryfilename):
    try:
        print('messages...')
        with open(queryfilename, "r", encoding="utf-8") as file:
            megs = file.read()
        print(megs)
        return megs
    except:
        print('Exit')

def analyze_data_with_gpt4(queryfilename):
    instructions_path = "instructions.md"
    try:
        instructions = get_instructions(instructions_path)
        if not instructions:
            print("No instructions found.")
            return None
        megs = get_messages(queryfilename)
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": megs}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in analyzing data with GPT-4: {e}")
        return None
    
def get_result(outputfilename, result):
    print(result)
    file = open(outputfilename, "w", encoding="utf-8")
    file.write(result)
    file.close()


def transform_process(queryfilename, outputfilename):
    print("BAN Logic Transformation Process Starting...")
    result = analyze_data_with_gpt4(queryfilename)
    get_result(outputfilename, result)


if __name__ == "__main__":
    print("python autobanlogic.py queryfile outputfile[markdown file]")
    try:
        if sys.argv[1]:
            queryfilename = sys.argv[1]
        if sys.argv[2]:
            outputfilename = sys.argv[2]
    except:
        print('Wrong... Exit')
    transform_process(queryfilename, outputfilename)
