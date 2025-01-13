from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from meme_generator_flow.tools.GenerateImageTool import GenerateImageTool

@CrewBase
class MemeGeneratorCrew:
    """Meme Generator Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    @agent
    def meme_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["meme_generator"],
            tools=[GenerateImageTool()]
        )

    @task
    def generate_meme(self) -> Task:
        return Task(
            config=self.tasks_config["generate_meme"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Meme Generator Crew"""


        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
