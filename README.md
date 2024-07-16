# Alma GPT-based Chatbot

This project demonstrates creating a chatbot using the GPT model, leveraging Ex Libris Knowledge Center's web pages for Alma documentation. The chatbot aims to make it easier for users to find information among the numerous web pages.

This project is adapted from the original work by Geraldine Geoffroy, who created a similar chatbot for Primo documentation. The original blog post can be found [here](https://developers.exlibrisgroup.com/blog/create-an-gpt-based-chatbot-on-exlibris-knowledge-center/).

## Technologies Used

- **Backend**: LlamaIndex library with LangChain framework
- **Database**: Deeplake ActiveLoop
- **Frontend**: Chainlit

## Requirements

- Free OpenAI account with an API key
- Free ActiveLoop account with an organization name and a token

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/alma-gpt-chatbot.git
   cd alma-gpt-chatbot
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ACTIVELOOP_TOKEN=your_activeloop_token_here
   ACTIVELOOP_ORGANIZATION=your_activeloop_organization_name_here
   DATASET_NAME=alma_documentation
   ```

4. Run the scraper to collect Alma documentation:
   ```
   python scraper.py
   ```

5. Create embeddings and store them in the database:
   ```
   python embeddings.py
   ```

6. Start the chatbot:
   ```
   chainlit run app.py -w
   ```

7. Access the chatbot interface at `http://localhost:8000`

## Usage

Once the chatbot is running, you can ask questions about Alma documentation, and the chatbot will provide answers based on the information it has been trained on.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

This project is adapted from the original work by Geraldine Geoffroy, who created a similar chatbot for Primo documentation. We are grateful for her innovative approach and sharing of knowledge.

## License

This project is open source and available under the [MIT License](LICENSE).
