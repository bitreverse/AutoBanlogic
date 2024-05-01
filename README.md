# Automation of Burrows-Abadi-Needham logic leveraging ChatGPT
- Automate the Burrows-Abadi-Needham logic process using the ChatGPT API. by Dowon Kim

## Introduction
### autobanlogic.py, instructions.md
- autobanlogic.py: You need to download and install Python 3 to run it.
- instructions.md: File for training BAN logic on ChatGPT.

## .env setting
- You need to register with the OpenAI developer platform and create your API key.
- You have to replace the following YourKey with your actual API key.
```
OPENAI_API_KEY="YourKey"
```

## Local Environment Setting (Install the required libraries)
```
pip install -r requirements.txt
```

### Pulling a repository from GitHub
```
git clone https://github.com/bitreverse/AutoBanlogic.git
```

### Running the program
```
python autotrade.py query.md result.md
```
- query.md: Write \<Messages\>, \[\<Idealization\>\], and \[\<Goals\>\] on this file.
- result.md
    - Since the results are output in Markdown format, it is recommended to use the .md extension.
    - If you view the output file through a Markdown viewer, it will be easier to check.
