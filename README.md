## Twitter Bot Readme

This repository contains code for a Twitter bot that generates tweets using [ChatGPT](https://openai.com/blog/dall-e-2-openai/) language model.

### Files

- `chatGPT.py`: Is used to generate text for the tweet from the bot
- `mail.py`: Is used to get the verification code from the inbox during creating a bot
- `tweet.py`: Is used to post a tweet using selenium

### Requirements

- Python 3.6 or later
- OpenAI API key
- Selenium WebDriver
- ChromeDriver (or other WebDriver executable)

### Usage

1. Clone the repository to your local machine.
2. Install the required dependencies listed in `requirements.txt`.
3. Replace the placeholder values in `config.py` with your own Twitter and OpenAI API credentials.
4. Run `mail.py` to retrieve the verification code sent by Twitter to your email inbox.
5. Paste the verification code into `config.py`.
6. Modify the prompt in `chatGPT.py` to generate your desired tweet.
7. Run `tweet.py` to post the generated tweet to your Twitter account.

### License

This project is licensed under the [MIT License](https://github.com/<username>/<repository>/blob/main/LICENSE). Feel free to use and modify the code as per your requirements.
