'''
file:       OUActionNoise.py
context:    Noise is a disruption of signal in any medium. It is used in deep 
            learning (DL) so that learning modules don't reach their conclusion prematurely.
            This code is from the domain https://keras.io/examples/rl/ddpg_pendulum/.
            A better explaination of noise in DL can be found here:
            https://medium.com/autonomous-agents/mathematical-foundation-for-noise-bias-and-variance-in-neuralnetworks-4f79ee801850
'''
import numpy as np

class OUActionNoise:
    def __init__(self, mean, std_deviation, theta=0.15, dt=1e-2, x_initial=None):
        self.theta = theta
        self.mean = mean
        self.std_dev = std_deviation
        self.dt = dt
        self.x_initial = x_initial
        self.reset()

    def __call__(self):
        # Formula taken from https://www.wikipedia.org/wiki/Ornstein-Uhlenbeck_process.
        x = (
            self.x_prev
            + self.theta * (self.mean - self.x_prev) * self.dt
            + self.std_dev * np.sqrt(self.dt) * np.random.normal(size=self.mean.shape)
        )
        # Store x into x_prev
        # Makes next noise dependent on current one
        self.x_prev = x
        return x

    def reset(self):
        if self.x_initial is not None:
            self.x_prev = self.x_initial
        else:
            self.x_prev = np.zeros_like(self.mean)