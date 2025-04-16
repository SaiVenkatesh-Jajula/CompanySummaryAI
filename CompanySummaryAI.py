from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama
from WebScraping import get_company_info

load_dotenv()
api_key=os.getenv('OPENAI_API_KEY')

title,info=get_company_info(input("Enter url of website : "))

summary_template="""
given the Title {title} and information {information} about a company, I want to create:
1.Company CEO
2.About Company facts in short
"""

summary_prompt_template = PromptTemplate(input_variables=["title","information"], template=summary_template)
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=api_key)
# llm=ChatOllama(model="llama3")

chain= summary_prompt_template | llm
res=chain.invoke(input={"title":title, "information":info})

print(res.content)




