class PlannerAgent:
    def execute(self, task):
        return {
            'goal': task,
            'steps': ['Analyze', 'Code', 'Test', 'Review']
        }
