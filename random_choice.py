import numpy as np
import timeit


def random_choice(a, size=None, p=None):
    p_cumsum = np.cumsum(p)
    samples = np.random.random(a).reshape(a, 1)
    # boolean_array = p_cumsum < samples
    # choice = (p_cumsum < samples).sum(axis=1)
    return (p_cumsum < samples).sum(axis=1)


def vectorized_random_choice(num_states, num_actions, num_hallucinations, T, S, A):
    """
    Vectorized implementation of random choice
    :return: S_prime
    """
    normalizer = np.sum(T, axis=2, keepdims=True)

    # Compute normalized T where each row sums to one
    T_n = T / normalizer
    # print('T_n = ' + str(T_n))

    # Compute cumulative sums over each entry in each row of T_n
    T_cumsum = np.cumsum(T_n, axis=2)

    # Get random states by using S as an index array to T_cumsum
    random_state_T = T_cumsum[S]

    # Get random actions by using A as an index array to random_state_T
    # We want to index each random state so we use arange to index all rows in random_state_T
    random_action_T = random_state_T[np.arange(num_hallucinations), A]

    # Generate random samples of states to transition to as 2d array with one column
    # Each entry represents a random selection of the next state
    samples = np.random.random_sample(num_hallucinations).reshape(num_hallucinations, 1)

    # Create boolean array where random_action_T less than samples
    boolean_array = random_action_T < samples

    # The boolean array represents the selection of the next state s' based on the probabilities.
    # The trick here is that booleans can be summed!  False = 0 and True = 1
    # The sums reprensent the index for each row which represents the next state s'.
    S_prime = boolean_array.sum(axis=1)
    return S_prime


def looped_random_choice(num_states, num_actions, num_hallucinations, T, S, A):
    """
    The other way would be to use np.random.choice np.random.choice can't be vectorized.
    You have to call random choice for each set of probabilities per transition. This means a for loop!
    :return: S_prime
    """
    p = T[S, A] / T[S, A].sum(axis=1, keepdims=True)

    S_prime = np.zeros(num_hallucinations, dtype=int)
    for i in range(num_hallucinations):
        S_prime[i] = np.random.choice(num_states, p=p[i])
    return S_prime


if __name__ == '__main__':
    # Initialize transition matrix
    num_states = 36
    num_actions = 4
    num_hallucinations = 50

    # Initialize transition matrix
    T = np.arange(num_states * num_actions * num_states).reshape(num_states, num_actions, num_states)

    # Pre-generate random state index array
    S = np.random.randint(num_states, size=num_hallucinations)
    # print('S = ' + str(S))

    # Pre-generate random action index array
    A = np.random.randint(num_actions, size=num_hallucinations)
    # print('A = ' + str(A))

    print(vectorized_random_choice(num_states, num_actions, num_hallucinations, T, S, A))
    print(looped_random_choice(num_states, num_actions, num_hallucinations, T, S, A))

    print(timeit.timeit('vectorized_random_choice(num_states, num_actions, num_hallucinations, T, S, A)', globals=globals()))
    print(timeit.timeit('looped_random_choice(num_states, num_actions, num_hallucinations, T, S, A)', globals=globals()))

