from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedIn import scrape_linkedin_profile
from output_parser import person_intel_parser, personIntel


def ice_breaker(name: str) -> tuple[personIntel, str]:
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    summary_template = """
           given the LinkedIn information {information} about a person from I want you to create:
           1. a short summary
           2. two interesting facts about them
           3. a topic that may interest them
           4. 2 creative Ice breakers to open a conversation with them
           \n{format_instructions} 

       """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    result = chain.run(information=linkedin_data)

    return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    print("Hello, LangChain!")
    result = ice_breaker(name="Eden Marco")
