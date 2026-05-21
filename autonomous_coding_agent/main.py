from orchestrator import AutonomousCodingAgent
import sys

task = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Build API"
agent = AutonomousCodingAgent()
print(agent.run(task))
