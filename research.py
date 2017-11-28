import tensorflow as tf

# Parameters
learning_rate = 0.001
training_epochs = 15

# Network parameters
n_input = 4

# Graph inputs
X = tf.placeholder('float64', [None, n_input])
Y = tf.placeholder('float32', [None])

# Weights and bias
weights = {
    'h11': tf.Variable(tf.random_normal([])),
    'h12': tf.Variable(tf.random_normal([])),
    'h13': tf.Variable(tf.random_normal([])),
    'h14': tf.Variable(tf.random_normal([])),
    'h21': tf.Variable(tf.random_normal([])),
    'h22': tf.Variable(tf.random_normal([]))    
}
biases = {
    'b11': tf.Variable(tf.random_normal([])),
    'b12': tf.Variable(tf.random_normal([])),
    'b13': tf.Variable(tf.random_normal([])),
    'b14': tf.Variable(tf.random_normal([])),
    'b21': tf.Variable(tf.random_normal([])),
    'b22': tf.Variable(tf.random_normal([]))
}

# Define loss
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = out_layer, labels = Y))

# Define optimizer
optimizer = tf.train.AdamOptimizer(learning_rate)
train_op = optimizer.minimize(loss_op)

# Initializing the variables
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    
