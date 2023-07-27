from langchain.tools import YouTubeSearchTool
import ast
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import openai
import os

class PersonalTrainer:
	def __init__(self):
		openai.api_key = os.getenv("OPENAI_API_KEY")

	def find_youtube_video(self, description, trainer_type):
		print(description)
		tool = YouTubeSearchTool()
		videos = tool.run(f"{description} with {trainer_type} very high definition, 1")
		parsed_list = ast.literal_eval(videos)
		if parsed_list:
			return f'https://www.youtube.com{parsed_list[0]}'

	def build_training_plan(self, personal_information):
		llm = OpenAI(temperature=0, max_tokens=1000)

		template = """Build a training plan based on my personal info from Monday to Friday, and put them in a json array in the format of [{{"day": day, "activity": activity, "focus_area": focus_area, "duration:" duration,"calorie": estimated_calorie_for_this_activity}}]: {personal_information}"""
		training_plan_prompt_template = PromptTemplate(input_variables=["personal_information"], template=template)
		chain = LLMChain(llm=llm, prompt=training_plan_prompt_template, output_key="table")
		results = chain.run({'personal_information': personal_information})
		print(results)
		return ast.literal_eval(results)

	def add_youtube_video_link(self, results):
		trainer_type = "young female trainer"
		for result in results:
			duration = result['duration']
			activity = result['activity']
			query = f'{duration} minutes {activity}'
			youtube_link = self.find_youtube_video(query, trainer_type)
			if youtube_link:
				result['youtube_link'] = youtube_link

