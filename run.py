from bar_model import BarModel
import seaborn as sea
import matplotlib.pyplot as plt

# Initialize program
model = BarModel(50)
model.step() # Initialize actors

# Run program
model.step() 

# Data analysis
agent_data = model.datacollector.get_agent_vars_dataframe()
admits = agent_data.xs(1, level="Step") # get from first step

g = sea.countplot(x="admitted", data=admits, hue="legal")
g.set(
    title="Admittance by Legal Drinking Status", xlabel="Admitted to Bar", ylabel="Number of agents"
);
plt.show()
