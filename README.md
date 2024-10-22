# ICE BREAKER

A repository for generating interesting facts, ice breakers, and summaries about individuals using Large Language Models (LLMs) and API integrations.

This web application extracts insightful details about people based on their names using OpenAI's LLM, SerpAPI, and Proxycurl APIs, creating a unique ice-breaker experience. 

![ezgif-5-122dc103a6](https://github.com/user-attachments/assets/5bd6bc12-17a5-4386-a3ee-f81c64c8fd1b)



## Tech Stack
Client: Flask

API Integrations: LangChain 🦜🔗, OpenAI, SerpAPI, Proxycurl

Data Validation: Pydantic

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`
`SERPAPI_API_KEY`
`PROXYCURL_API_KEY`

## Run Locally

1. Clone the project

```bash
  git clone https://github.com/ManishSharma1609/documentation-helper.git
```

2. Go to the project directory

```bash
  cd ice-breaker
```

3. Install dependencies

Create a new virtual environment using pipenv:

```bash
  pipenv shell
```

This will activate the environment.

Next, install the required dependencies:

```bash
  pipenv install
```

4. Start the flask server

```bash
  python app.py
```
or

```bash
  pipenv run flask run

```
The server should now be running on http://127.0.0.1:5000.

## Running Tests

To run tests, run the following command

```bash
  pipenv run pytest .
```
