## Discord Bot for SWQ Code Tracking
This Discord bot is specifically designed for Summoners War players who want to easily track and receive notifications about the latest code releases on the SWQ website (swq.jp). It automates the process of crawling the website, extracting codes, and publishing them to subscribed channels on multiple Discord servers.

## Description
The SWQ Code Tracking Discord bot simplifies the code tracking process for Summoners War players by automating the collection and distribution of codes from the SWQ website. With this bot, you can easily stay up to date with the latest codes and make sure you never miss out on any rewards.

The bot periodically crawls the SWQ website, captures new codes, and sends them to subscribed channels on different Discord servers. It keeps track of the existing codes to avoid duplicate notifications and provides commands for users to retrieve the latest code or view a list of the last 10 codes.

## Usage

1. Clone the repository and install the necessary dependencies:

    - git clone [https://github.com/imptrck/swq-bot-discord.git](https://github.com/imptrck/swq-bot-discord.git)
    - cd swq-discord-bot
    - pip install -r requirements.txt
    
2. Obtain a Discord bot token:
    - Create a new bot application on the Discord Developer Portal.
    - Copy the bot token.

3. Configure the bot:
    - Set `DISCORD_TOKEN` with your Discord bot token in your environment variable.
    - Set the `CHROME_DRIVER_PATH` constant to the path where your ChromeDriver executable is located.

4. Start the bot:

    - python main.py


5. Add the bot to your Discord server:
    - Create a new Discord server or choose an existing one.
    - Visit the Discord Developer Portal and navigate to your bot application.
    - Generate an OAuth2 URL with the necessary permissions (bot and message content).
    - Open the URL in your web browser and authorize the bot to join your server.

6. Interact with the bot:
    - Use the following commands in any channel where the bot is present:
      - `/last_code`: Retrieves the latest code.
      - `/last_10_codes`: Retrieves a list of the last 10 codes.
      - `/start_swqbot`: Starts the crawler to publish codes to the current channel.
      - `/stop_swqbot`: Stops the crawler from publishing codes.


## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. Feel free to modify and customize the README.md according to your needs, adding more detailed instructions or any other relevant information.



