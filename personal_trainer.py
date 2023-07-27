from langchain.tools import YouTubeSearchTool
import ast
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import openai
import os


def find_youtube_video(query):
	tool = YouTubeSearchTool()	
	trainer_type = "young female trainer"
	videos = tool.run(f"{query} with {trainer_type} very high definition, 1")
	parsed_list = ast.literal_eval(videos)
	for video in parsed_list:
		return f'youtube.com{video}'

class PersonalTrainer:
	def __init__(self):
		openai.api_key = os.getenv("OPENAI_API_KEY")

	def build_training_plan(self, personal_information):

		llm = OpenAI(temperature=0)

		template = """Build a training plan based on my personal info from Monday to Friday, and put them in a json array in the format of [{{"day": day, "activity": activity, "focus_area": focus_area, "duration:" duration,"calorie": estimated_calorie_for_this_activity}}]: {personal_information}"""
		training_plan_prompt_template = PromptTemplate(input_variables=["personal_information"], template=template)
		chain = LLMChain(llm=llm, prompt=training_plan_prompt_template, output_key="table")
		print("running chain")
		result = chain.run({'personal_information': personal_information})
		print(result)
		return ast.literal_eval(result)
