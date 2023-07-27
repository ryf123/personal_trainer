from personal_trainer import PersonalTrainer

with open('personal_info', 'r') as file:
	personal_info = file.read()
	ps = PersonalTrainer()
	results = ps.build_training_plan(personal_info)
	ps.add_youtube_video_link(results)
	print(results)