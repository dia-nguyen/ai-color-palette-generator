# AI Color Generator

Exercise with Open AI's Completion API (now deprecated) using the davinci-003 model.
Enter a prompt to generate your very own color palette.

![Screen Shot 2023-12-14 at 3 05 21 PM](https://github.com/dia-nguyen/ai-color-palette-generator/assets/40869031/c60df5e0-05cb-4f3a-aac1-a1ebfd3b56e3)

## Set Up
1. Create virtual environment and install dependencies
```py
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
```

2. Create .env file and set up environment variables
```py
  OPENAI_API_KEY=[YOUR OPENAI_API_KEY]
```

3. Run server `flask run -p 5001`
