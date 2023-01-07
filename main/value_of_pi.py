import numpy as np


def get_value_of_pi(exponent = 6):
    '''
    :param exponent: Exponent to generate the random numbers required for pi estimation
    :algorithm: Value of pi is derived from the generated random numbers using the Uniform Distribution and identifying
                how many of them fall within x^2 + y^2 <= 1 out of cartesian area [-1,1] with unit area of 4
    :return: Estimated value of pi
    '''

    random_x = np.random.uniform(-1, 1, 10**exponent)
    random_y = np.random.uniform(-1, 1, 10**exponent)

    random = random_x**2 + random_y**2

    in_circle_elem = [elem for elem in random if elem <= 1]

    return 4 * len(in_circle_elem)/(10**exponent)


if __name__ == '__main__':

    print(f"Estimated Value of pi using exponent = 1 montecarlo is: {get_value_of_pi(1)}")
    print(f"Estimated Value of pi using exponent = 3 montecarlo is: {get_value_of_pi(3)}")
    print(f"Estimated Value of pi using exponent = 6 montecarlo is: {get_value_of_pi(6)}")
    print(f"Estimated Value of pi using exponent = 7 montecarlo is: {get_value_of_pi(7)}")