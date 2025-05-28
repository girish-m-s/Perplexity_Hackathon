# AI Trading Assistant
This AI Trading Assistant empowers you to manage your stock portfolio and receive real-time alerts through a user-friendly interface. It's built with Python and leverages advanced AI to understand your natural language commands, execute trades, and provide timely insights by proactively monitoring your investments.

Getting Started
Follow these steps to set up and run the application.

Prerequisites
Before running the application, you'll need to set up your environment and install the necessary Python libraries.

Python Environment: Ensure you have Python 3.8+ installed on your system.
API Keys:
Alpaca API Keys: You will need your Alpaca API Key and Secret. These are used to connect to your Alpaca trading account (paper trading is supported by default for safe experimentation).
Perplexity AI API Key: You will need a Perplexity AI API Key to enable the AI capabilities of the assistant.
WhatsApp Setup: For real-time notifications, ensure you have WhatsApp configured on the phone number specified in the kit.sendwhatmsg_instantly calls within the code (currently +919535880047). pywhatkit requires Chromium or Chrome to be installed for sending messages.
Install the required Python packages by creating a requirements.txt file in your project directory with the following content:

alpaca-py
pywhatkit
requests
streamlit
schedule
Then, install them using pip:

Bash

## pip install -r requirements.txt
Running the Application
To launch the AI Trading Assistant, navigate to the directory containing your Streamlit-adapted stock_trade_app.py file in your terminal and execute the following command:

Bash

## streamlit run stock_trade_app.py
This will open the application in your default web browser (usually at http://localhost:8501), where you can interact with the AI assistant through a chat interface and trigger portfolio monitoring.

# About the Project
The Spark of Inspiration
Our inspiration for this AI Trading Assistant stemmed from a desire to empower everyday investors with sophisticated, intelligent tools previously reserved for financial institutions. We saw a gap between complex market data and accessible, actionable insights. We wanted to build something that could not only execute trades but also understand the nuances of a user's intent, monitor their portfolio proactively, and deliver critical information directly to them. The idea of a personal, vigilant financial co-pilot that could understand natural language and act on it was incredibly compelling.

## Our Learning Journey
This project was a significant learning experience, pushing us to delve deeper into several cutting-edge technologies. We gained a profound understanding of Large Language Model (LLM) orchestration, particularly how to integrate them for specific tool-use cases beyond simple chatbots. Learning to effectively prompt LLMs to output structured data (like JSON for trading commands) and then process that output programmatically was a key takeaway. We also honed our skills in API integration, managing authentication, error handling, and data parsing across diverse platforms like Alpaca for trading and advanced AI services for AI capabilities. Furthermore, we gained practical experience in multi-threading and task scheduling in Python, crucial for building a responsive application that can simultaneously handle user commands and background monitoring tasks. The importance of robust error handling and user-friendly notifications also became very clear throughout the development process.

## Crafting the Assistant
We built this AI Trading Assistant primarily using Python as our core development language due to its versatility and rich ecosystem, alongside the Streamlit framework for creating an interactive web-based user interface. For the brains of the operation, we leveraged advanced AI models to understand natural language commands. A key innovation in our design was the implementation of a dynamic AI model selection mechanism. We use one AI model to first assess the user's query and then intelligently decide which more specialized and powerful AI model is best suited to handle the request. This approach optimizes both performance and efficiency.

Our assistant integrates seamlessly with the Alpaca Trading API to execute real-time market orders (buy/sell) and retrieve comprehensive portfolio information. When a user issues a command like "buy 5 shares of AAPL," the AI interprets this intent, generates a structured command, which our Python backend then translates into an Alpaca API call. After the trade, the system feeds the Alpaca response back to the AI to generate a clear, conversational confirmation for the user.

A standout feature we developed is the "Watch My Stocks" functionality. Using Python's schedule library and threading for background execution, the assistant periodically checks the user's portfolio. It then uses advanced AI to scour recent news and identify any potential negative impacts on their holdings. If a significant risk is detected, the system sends a WhatsApp notification directly to the user's phone, providing a concise summary and a recommendation.

## Navigating the Challenges
Building this project presented its share of challenges. One of the primary hurdles was ensuring consistent and reliable structured data output from the AI models for tool execution. Despite clear system prompts, AI models can sometimes deviate or include extraneous text, requiring robust parsing and error handling on our end. We iterated on our prompting strategies to minimize these occurrences.

Another challenge was managing conversation context effectively. Maintaining the conversation history accurately and ensuring that previous turns informed subsequent AI responses was critical for a natural user experience, especially when multiple steps were involved (e.g., user query -> tool execution -> AI explaining tool output).

Finally, integrating the background scheduling and WhatsApp notifications required careful consideration of execution environments and potential rate limits, ensuring the system remained stable and delivered timely alerts without disruption. Overcoming these challenges strengthened our understanding of building reliable, AI-powered applications.
