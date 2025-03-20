import time

# List of cities in the UK, with 'London' appearing five times
uk_cities = ['London', 'Manchester', 'Birmingham', 'Leeds', 'London', 'Glasgow', 'Manchester', 
             'London', 'London', 'Bristol', 'London']

# Empty list to store checked cities
checked_cities = []

# Loop through the list of UK cities
for city in uk_cities:
    checked_cities.append(city)
    city_count = checked_cities.count(city)
    
    if city_count == 5:
        print(f"{city} has appeared 5 times! Pausing for 4 seconds before removing it...")
        time.sleep(4)  # Wait for 4 seconds
        checked_cities = [c for c in checked_cities if c != city]  # Remove all instances of the city
        print(f"{city} removed from the list.\n")
    else:
        print(f"Added city: {city}")

print("\nFinal checked cities list:", checked_cities)


# b = ["9", "0", "9", "0", "9", "0"]
# c = []
# for a in b:
#     c.append(a)  # Append each element of 'b' to 'c'

# print(len(c))
# print(c)

    
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext

# # Function that runs when the user sends the /start command
# def start(update: Update, context: CallbackContext) -> None:
#     user = update.effective_user  # Get the user who sent the message
    
#     # Extracting user details
#     username = user.username if user.username else "No username"
#     first_name = user.first_name if user.first_name else "No first name"
#     last_name = user.last_name if user.last_name else "No last name"
    
#     # Displaying user details on the terminal
#     print(f"User's details:")
#     print(f"Username: {username}")
#     print(f"First Name: {first_name}")
#     print(f"Last Name: {last_name}")
    
#     # Replying to the user
#     update.message.reply_text(f"Hello {first_name}, I have captured your details.")

# # Main function to run the bot
# def main() -> None:
#     # Your bot's API token from BotFather
#     token = "5244306869:AAFrJqdmrIpAbKx_HuSWBlhhYVsJEeIuShI"

#     # Create the Updater and pass it your bot's token
#     updater = Updater(token)
    
#     # Get the dispatcher to register handlers
#     dispatcher = updater.dispatcher
    
#     # Register the /start command handler
#     dispatcher.add_handler(CommandHandler("start", start))
    
#     # Start the Bot
#     updater.start_polling()
    
#     # Run the bot until you press Ctrl+C
#     updater.idle()

# if __name__ == '__main__':
#     main()
