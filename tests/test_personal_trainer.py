import unittest
import os
from unittest.mock import patch, Mock, ANY
from personal_trainer import PersonalTrainer
os.environ['OPENAI_API_KEY'] = 'test_api_key'

class TestPersonalTrainer(unittest.TestCase):
    
    @patch("personal_trainer.LLMChain")
    def test_build_training_plan(self, mock_LLMChain):
        expected_result = [
            {"day": "Monday", "activity": "Running", "focus_area": "Cardio", "duration": 30, "calorie": 500},
            {"day": "Tuesday", "activity": "Strength Training", "focus_area": "Upper Body", "duration": 45, "calorie": 400}
        ]

        chain_ret_val = """[{"day": "Monday", "activity": "Running", "focus_area": "Cardio", "duration": 30, "calorie": 500},{"day": "Tuesday", "activity": "Strength Training", "focus_area": "Upper Body", "duration": 45, "calorie": 400}]"""
        import ast
        # Mocking the LLMChain instance and its run method
        mock_chain_instance = mock_LLMChain.return_value
        mock_chain_instance.run.return_value = chain_ret_val
        
        # Calling the method
        ps = PersonalTrainer()
        result = ps.build_training_plan("I want to lose weight")
        
        # Assertions        
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

