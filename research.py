import tensorflow as tf
from logistic_map_inputs import get_input

# Parameters
learning_rate = 0.001
epochs = 15
n_sequences = 10 #10 only for the sake of debugging purposes

# Get the input sequence and associated 'r'
features, labels = get_input(n_sequences)

# Network parameters
n_input = 4
n_h1 = 4
n_h2 = 8

# Graph inputs
X = tf.placeholder('float64', [None, n_input])
Y = tf.placeholder('float32', [None, 1])

# Weights and bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_h1])),
    'h2': tf.Variable(tf.random_normal([n_h1, n_h2])),
    'out': tf.Variable(tf.random_normal([n_h2, 1]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_h1])),
    'b2': tf.Variable(tf.random_normal([n_h2])),
    'out': tf.Variable(tf.random_normal([1]))
}

# Tentative model
# 2 hidden layers and 1 output layer
l1 = tf.nn.relu(tf.add(tf.matmul(X, weights['h1']), biases['b1']))
l2 = tf.nn.relu(tf.add(tf.matmul(l1, weights['h2']), biases['b2']))
out_layer = tf.add(tf.matmul(l2, weights['out']), biases['out'])

# Define loss
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = out_layer, labels = Y))

# Define optimizer
optimizer = tf.train.AdamOptimizer(learning_rate)
train_op = optimizer.minimize(loss_op)

# Initializing the variables
init = tf.global_variables_initializer()

# Test function
def test():
    global features
    global labels
    # Using the features and labels with indices 10-50 for test
    test_input = features[10:50]
    true_output = labels[10:50]
    out1 = sess.run(out_layer, feed_dict={X:test_input})
    accuracy = sum(abs(true_output - out1))/sum(true_output)
    return accuracy
    
    

with tf.Session() as sess:
    sess.run(init)
    # Training
    for epoch in range(epochs):
        avg_cost = 0.
        for i in range(n_sequences):
            # Backpropagation and cost op
            a, c = sess.run([train_op, loss_op], feed_dict={X: features[i]
                                                            Y: labels[i]})
            # Average loss for each
            avg_cost += c/n_sequences
        print("Epoch:", epoch, "\nCost:", avg_cost)
    print("Training complete...")
    print("Accuracy: ", test())
    
