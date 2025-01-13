#!/usr/bin/env python
from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from meme_generator_flow.crews.meme_idea_crew.meme_idea_crew import MemeIdeaCrew
from meme_generator_flow.crews.meme_generator_crew.meme_generator_crew import MemeGeneratorCrew


class MemeState(BaseModel):
    meme_topic: str = ""
    meme_idea: str = ""
    meme: str = ""

class MemeFlow(Flow[MemeState]):

    # @start()
    # def gather_meme_topic(self):
    #     print("Gathering user input")
    #     self.state.meme_topic = input("Enter the topic of meme: ")

    @start()
    def generate_meme_idea(self):
        print("Generating meme idea")
        result = (
            MemeIdeaCrew()
            .crew()
           .kickoff(inputs={"meme_topic": self.state.meme_topic})
        )

        print("Idea generated", result.raw)
        self.state.meme_idea = result.raw

    @listen(generate_meme_idea)
    def generate_meme(self):
        print("Generating meme")
        result = (
            MemeGeneratorCrew()
            .crew()
            .kickoff(inputs={"meme_idea": self.state.meme_idea})
        )

        print("Meme generated", result.raw)
        self.state.meme = result.raw

    # @listen(generate_meme_idea)
    # def save_meme_idea(self):
    #     print("Saving meme idea")
    #     with open("memeidea.txt", "w") as f:
    #         f.write(self.state.meme_idea)


def kickoff(meme_topic: str):
    inputs = {"meme_topic": meme_topic}
    meme_idea_flow = MemeFlow()
    meme_idea_flow.kickoff(inputs=inputs)


def plot():
    meme_idea_flow = MemeFlow()
    meme_idea_flow.plot()


if __name__ == "__main__":
    kickoff()
