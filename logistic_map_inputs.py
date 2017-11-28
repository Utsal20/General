from random import uniform

def get_input(n):
    """ Generate the input sequence along with the coefficient 'r'
    Args:
        param1: length of the sequence to feed
    Returns:
        tuple with a list of lists containing the sequence and associated coefficient
    """
    x_dad_list = []
    r_list = []

    for input_size in range(0,1000):
        # Generating a random coefficient 'r'
        r = uniform(3.,4.)
        r_list.append(r)
        # Generating a random starting value
        x = uniform(0.,1.)
        x_list = []
        for i in range(0,n):
            x_list.append(x)
            x = r * x * (1-x)
        x_dad_list.append(x_list)

    return x_dad_list, r_list
