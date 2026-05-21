from agents.planner_agent import PlannerAgent
from agents.coding_agent import CodingAgent
from agents.testing_agent import TestingAgent
from agents.reviewer_agent import ReviewerAgent

class AutonomousCodingAgent:
    def __init__(self):
        self.planner = PlannerAgent()
        self.coder = CodingAgent()
        self.tester = TestingAgent()
        self.reviewer = ReviewerAgent()

    def run(self, task):
        plan = self.planner.execute(task)
        code = self.coder.execute(plan)
        tests = self.tester.execute(code)
        review = self.reviewer.execute(code)
        return {
            'task': task,
            'plan': plan,
            'tests': tests,
            'review': review
        }
