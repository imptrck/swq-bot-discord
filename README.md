## Description

The Discord bot periodically crawls a specified website, extracts codes from it, and publishes them to subscribed channels on different Discord servers. It keeps track of existing codes and only publishes new codes found during each crawl. Users can also interact with the bot to retrieve the latest code or a list of the last 10 codes. It gets it's code from swq.jp.

## Usage

1. Clone the repository and install the necessary dependencies:

    git clone [https://github.com/your-repository.git](https://github.com/imptrck/swq-bot-discord.git)
    cd discord-bot
    pip install -r requirements.txt
    
2. Obtain a Discord bot token:
- Create a new bot application on the Discord Developer Portal.
- Copy the bot token.

3. Configure the bot:
- Set `DISCORD_TOKEN` with your Discord bot token in your environment variable.
- Set the `CHROME_DRIVER_PATH` constant to the path where your ChromeDriver executable is located.

4. Start the bot:

    python main.py


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



