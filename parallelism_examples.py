import multiprocessing
import random
import string

if __name__ == '__main__':
    random.seed(123)

    # Define an output queue
    output = multiprocessing.Queue()

    # define a example function
    def rand_string(length, output1):
        """ Generates a random string of numbers, lower- and uppercase chars. """
        rand_str = ''.join(random.choice(
            string.ascii_lowercase
            + string.ascii_uppercase
            + string.digits)
                           for _ in range(length))
        output1.put(rand_str)


    # Setup a list of processes that we want to run
    processes = [multiprocessing.Process(target=rand_string, args=(5, output)) for x in range(4)]

    # Run processes
    for p in processes:
        p.start()

    # Exit the completed processes
    for p in processes:
        p.join()

    # Get process results from the output queue
    results = [output.get() for p in processes]

    print(results)
