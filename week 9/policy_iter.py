import numpy as np

class GridWorldMDP:
    def __init__(self, size, goal, trap):
        self.size = size
        self.goal = goal
        self.trap = trap
        self.state_space = [(i, j) for i in range(size) for j in range(size)]
        self.action_space = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.transitions = self.build_transitions()
        self.rewards = self.build_rewards()

    def build_transitions(self):
        transitions = {}
        for state in self.state_space:
            transitions[state] = {}
            for action in self.action_space:
                transitions[state][action] = self.calculate_transitions(state, action)
        return transitions

    def calculate_transitions(self, state, action):
        i, j = state
        if action == 'UP':
            return self.validate_state(i - 1, j)
        elif action == 'DOWN':
            return self.validate_state(i + 1, j)
        elif action == 'LEFT':
            return self.validate_state(i, j - 1)
        elif action == 'RIGHT':
            return self.validate_state(i, j + 1)

    def validate_state(self, i, j):
        i = max(0, min(i, self.size - 1))
        j = max(0, min(j, self.size - 1))
        if (i, j) == self.goal or (i, j) == self.trap:
            return [(1.0, (i, j))]
        else:
            return [(1.0, (i, j))]

    def build_rewards(self):
        rewards = {}
        for state in self.state_space:
            rewards[state] = -1.0
        rewards[self.goal] = 0.0
        rewards[self.trap] = -10.0
        return rewards
def policy_iteration(mdp, gamma=0.9):
    policy = {
        state: np.random.choice(mdp.action_space)
        for state in mdp.state_space
        if state != mdp.goal and state != mdp.trap
    }

    state_values = {state: 0.0 for state in mdp.state_space}

    while True:
        # Policy Evaluation
        while True:
            delta = 0
            for state in mdp.state_space:
                if state == mdp.goal or state == mdp.trap:
                    contdef policy_iteration(mdp, gamma=0.9):
    policy = {
        state: np.random.choice(mdp.action_space)
        for state in mdp.state_space
        if state != mdp.goal and state != mdp.trap
    }

    state_values = {state: 0.0 for state in mdp.state_space}

    while True:
        # Policy Evaluatinue

                v = state_values[state]
                action = policy[state]

                state_values[state] = sum([
                    p * (mdp.rewards[next_state] + gamma * state_values[next_state])
                    for p, next_state in mdp.transitions[state][action]
                ])

                delta = max(delta, abs(v - state_values[state]))

            if delta < 0.01:
                break

        # Policy Improvement
        policy_stable = True

        for state in mdp.state_space:
            if state == mdp.goal or state == mdp.trap:
                continue

            old_action = policy[state]

            policy[state] = max(
                mdp.action_space,
                key=lambda a: sum([
                    p * (mdp.rewards[next_state] + gamma * state_values[next_state])
                    for p, next_state in mdp.transitions[state][a]
                ])
            )

            if old_action != policy[state]:
                policy_stable = False

        if policy_stable:
            break

    return policy, state_values
mdp = GridWorldMDP(3, (2, 2), (1, 1))

policy, values = policy_iteration(mdp)

print("Policy Iteration Results:")
for state in policy:
    print(f"State: {state}, Action: {policy[state]}, Value: {values[state]}")
