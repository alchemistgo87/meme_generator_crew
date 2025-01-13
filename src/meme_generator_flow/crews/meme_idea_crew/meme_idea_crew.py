from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class MemeIdeaCrew:
    """Meme Idea Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    @agent
    def meme_idea_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["meme_idea_generator"],
        )

    @task
    def generate_meme_idea(self) -> Task:
        return Task(
            config=self.tasks_config["generate_meme_idea"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Meme Idea Generator Crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
