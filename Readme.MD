# IBTROS

## Overview
IBTROS is an advanced AI-driven Telegram bot that provides real-time information retrieval and transportation assistance. The system leverages the **Azure OpenAI GPT-40 API**, **Azure Cognitive Services**, and a **robust backend** to process user queries and deliver precise results efficiently.

[Try now](https://t.me/IBmeal_bot)

## Features
- **Multi-modal AI Processing**: Integrates text, speech, image, and avatar functionalities powered by Azure AI.
- **Database Support**: Uses SQLite or Azure PostgreSQL to retrieve real-time location-based information.
- **Seamless User Interaction**: Telegram bot interface for easy access and query submission.
- **Optimized Query Handling**: Utilizes OpenAI's GPT-40 API for natural language understanding.

## Installation
To get started with IBTROS, clone the repository and install dependencies:

```sh
# Clone the repository
git clone https://github.com/Jerryblessed/IBTROS.git
cd IBTROS

# Install dependencies
pip install -r requirements.txt
```

## Usage
To launch the bot, execute the following command:

```sh
python core.py
```

Ensure you have set up the necessary **API keys** and **database connections** before running the bot.

## Architectural Diagram
```
                 IBTROS ARCHITECTURAL DIAGRAM

               +-----------------------+
               | 🤖 Telegram Bot UI     |  <------ Optional ------>  +----------------------+
               +-----------------------+                            | ❓ Users choose to ask |
                           |                                        |      a question      |
                           v                                        +----------------------+
               +----------------------------------+                            |
               |  🔍 Query Processing            |                            v
               |   (Azure OpenAI GPT-40 API)     |      +----------------------------------------------+
               +----------------------------------+      | 🧠 Uses Cognitive Services Live Avatar       |
                           |                           |   (🗣️ SST, 🔊 TTS, 🖼️ Image, and 📜 Text GPT-4o)  |
                           v                           |   (Powered by Azure OpenAI GPT-40 API)        |
+------------------------------------------------------|----------------------------------------------+
|  📦 Returns:                                         |
|    • 💰 Price                                        |
|    • 📍 Location (from DB: 🗄️ SQLite or Azure Postgres)  |
+------------------------------------------------------+
                           |
                           v
               +-----------------------+
               | 🚗 Users choose and enjoy |
               |       the ride         |
               +-----------------------+
```

## Credits
This project was inspired by and utilizes components from the open-source project [this](https://github.com/Steffo99/greed). Many thanks to its contributors for their invaluable work!

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

