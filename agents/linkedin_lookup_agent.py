from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType
import re
from tools.tools import get_profile_url
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["PROXYCURL_API_KEY"]=os.getenv("PROXYCURL_API_KEY")
os.environ["SERPAPI_API_KEY"]=os.getenv("SERPAPI_API_KEY")

def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                               Your answer should contain only a URL"""
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedIn profile page",
            func=get_profile_url,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linked_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    modified_url = linked_profile_url.replace(
        "https://il.linkedin.com", "https://www.linkedin.com"
    )

    url_pattern = r"https?://\S+"

    match = re.search(url_pattern, modified_url)
    print(match.group())

    return match.group()
