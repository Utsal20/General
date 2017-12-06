from sklearn.neural_network import MLPRegressor
from logistic_map_inputs import get_input

# Parameters
# n_sequences = 500000

# Network parameters
n_input = 4
n_layers = (4,)

# Get the input sequence and associated 'r'
features, labels = get_input(n_input)

# Model
reg = MLPRegressor(hidden_layer_sizes = n_layers, activation = 'relu', solver = 'adam',
                   alpha = 0.001, learning_rate = 'constant',
                   learning_rate_init = 0.001)
reg.fit(features, labels)

