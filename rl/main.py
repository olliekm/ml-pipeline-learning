"""
Trying out RL fundamentals from scratch.
Video: https://www.youtube.com/watch?v=psDlXfbe6ok
"""

import numpy as np
from collections import namedtuple

"""
States:
- 0: Empty
- 1: Goal
- -1: Wall
"""

class Agent():
    """
    Represents an agent in the maze.
    """
    def __init__(self, i=0, j=0):
        self.i = i # Row position
        self.j = j # Column position

    def vmove(self, di):
        """
        Moves the agent vertically.
        """
        di = -1 if di > 0 else 1
        return Agent(self.i + di, self.j)    

    def hmove(self, di):
        """
        Moves the agent horizontally.
        """
        di = -1 if di > 0 else 1
        return Agent(self.i, self.j + di)    

    def __repr__(self):
        return f"Agent({self.i}, {self.j})"

class Maze():
    """
    A simple maze environment for reinforcement learning.
    """
    def __init__(self, rows=4, cols=4):
        self.env = np.zeros((rows, cols), dtype=int)
        self.agent = Agent(0, 0)

    def in_bounds(self, i, j) -> bool:
        """
        Checks if the agent is within the bounds of the maze.
        """
        return 0 <= i < self.env.shape[0] and 0 <= j < self.env.shape[1] and self.env[i, j] != -1

    def agent_in_bounds(self, a: Agent) -> bool:
        """
        Checks if the agent is within the bounds of the maze.
        """
        return self.in_bounds(a.i, a.j)

    def get_possible_actions(self) -> list:
        """
        Returns a list of possible actions for the agent.
        Actions are represented as (di, dj) tuples.
        """
        a = self.agent
        actions = [a.hmove(-1), a.hmove(1), a.vmove(-1), a.vmove(1)]
        return [action for action in actions if self.agent_in_bounds(action)]

    def visualize(self) -> None:
        """
        Visualizes the maze.
        """
        assert self.in_bounds(self.agent.i, self.agent.j), "Agent is out of bounds"
        e = self.env.copy()
        e[self.agent.i, self.agent.j] = 8
        print(e)




def test_maze() -> Maze:
    maze = Maze()
    e = maze.env
    e[-1, -1] = 1  # Goal
    e[1, 1] = -1 # Wall
    e[2, 2] = -1 # Wall
    e[0, 1] = -1
    e[3, 0] = -1
    return maze

if __name__ == "__main__":
    m = test_maze()
    m.agent = m.agent.vmove(-1) 
    m.visualize()
    print(m.get_possible_actions())