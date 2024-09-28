# Text to SQL App

Welcome to the Text to SQL App! This application enables users to convert natural language queries into SQL statements using advanced natural language processing techniques. Built with Streamlit, the app provides a user-friendly interface to interact with databases.

## Features

- **Natural Language Processing:** Utilizes Google Gemini for interpreting user queries.
- **SQL Generation:** Converts natural language input into valid SQL statements.
- **CSV Support:** Incorporates CSV handling using LangChain, allowing users to interact with CSV data.
- **Smart Dataframe Integration:** Leverages PandasAI for advanced data manipulation and querying.

## Requirements

- Python 3.7 or higher
- Streamlit
- Google Gemini API
- LangChain (including `langchain_experimental` and `langchain_community`)
- PandasAI
- Other dependencies listed in `requirements.txt`

Text to SQL:

Enter your natural language query in the input box and click "Generate SQL" to see the corresponding SQL statement.
CSV Interaction:

Use the CSV upload feature to load your CSV files and query them using natural language.
Smart Dataframe Queries:

Enter queries that utilize the SmartDataframe from PandasAI for enhanced data manipulation.

Examples
Text to SQL:

Input: "Show me all users from the database."
Output: SELECT * FROM users;
CSV Interaction:

Input: "What is the average sales from the uploaded CSV?"
Output: Generated query based on the CSV data.
Smart Dataframe:

Input: "Get the top 5 products by sales from the Smart Dataframe."
Output: Query executed on the SmartDataframe.

Contributing
Contributions are welcome! If you have suggestions for improvements or want to report issues, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to Google Gemini for their powerful NLP capabilities.
Special thanks to the LangChain and PandasAI communities for their valuable tools and resources.
Thanks to the Streamlit community for building such an amazing platform.
Contact
For questions or feedback, please reach out to lav.sandy30@gmail.com
