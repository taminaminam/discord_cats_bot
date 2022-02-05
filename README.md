# discord_cats_bot

This is a very simple bot written in [discord.py](https://discordpy.readthedocs.io/en/stable/) that gives you cats if you write the command <code>cat!</code> into chat

## Setting up the .env file

You will need to create a file called <code>.env</code> in the main directory.

Inside the <code>.env</code> file, you will need to add the text <code>DISCORD_TOKEN={your_discord_token}</code> (replace <code>{your_discord_token}</code> with your actual discord bot token).

In a new line inside the <code>.env</code> file, you will need to add the text <code>BOT_OWNER_ID={your_discord_userid}</code> (replace <code>{your_discord_userid}</code> with your actual discord user id)

In the end your <code>.env</code> file should look like this[^1]:

[^1]: The values presented in this example are fake and should not be usable in this state.

```.env
DISCORD_TOKEN=bjyab6sy6NxcLb4GR9a.pqCFFz_F_snPzHhi$q4mhzgob5dR@KBde5
BOT_OWNER_ID=123456789012345678
```

## Inviting the bot to your server
To invite your bot to your server, you will need an oauth2 link.
The permission code needed is <code>5288</code> and the scope is <code>bot%20applications.commands</code>

The link should look like this with <code>{your_application_client_id}</code> replaced with the Oauth2 > client Information > CLIENT ID of your application:

<code>https://discord.com/api/oauth2/authorize?client_id={your_application_client_id}&permissions=52288&scope=bot%20applications.commands</code>