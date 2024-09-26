import mesa as mesa
import random

# CONSTANTS
MIN_AGE = 18
MAX_AGE = 22
DRINKING_AGE = 21

FAKE_ID_PCT = 0.5

# FUNCTIONS
def request_entry_1(self):
    """Entry determined by being legal or having a fake ID."""
    return (self.legal | self.fake_id)
      
def request_entry_0(self):
    """Entry determined only by legal drinking age status."""
    return (self.age >= 21)
     
# AGENTS
class Patron(mesa.Agent):
    # Bar patron
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # Set characteristics:
        self.age = random.randint(MIN_AGE, MAX_AGE)
        self.admit = 0
        self.legal = (self.age >= DRINKING_AGE)
        self.fake_id = False if self.legal else (random.random() < FAKE_ID_PCT)

    def step(self):
        self.admit = request_entry_1(self)
          

# ENVIRONMENT MODEL
class BarModel(mesa.Model):
    def __init__(self, n_patrons):
        super().__init__()
        # Set up environment
        self.num_patrons = n_patrons
        self.schedule = mesa.time.RandomActivation(self)
        self.datacollector = mesa.DataCollector(
             agent_reporters= {"legal": "legal", "admitted": "admit"}
        )

        # Create patron agents
        for i in range(self.num_patrons):
            a = Patron(i, self)
            self.schedule.add(a)


    def step(self):
            self.datacollector.collect(self)
            self.schedule.step()