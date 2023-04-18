import gym
import matplotlib.pyplot as plt

# Read CarPole
env = gym.make("CartPole-v1", render_mode="rgb_array")
observation = env.reset()

# Run
for i in range(20):
    # Push right
    action = 1 

    # Get information
    observation, reward, terminated, truncated, info = env.step(action) 
    print("observation = " + str(observation))
    print("reward = " + str(reward))

# Show graph
plt.imshow(env.render())
plt.axis('off')
plt.show()

env.close()