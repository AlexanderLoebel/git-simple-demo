def plus_function(var1, var2):

    plus_output = var1 + var2

    return plus_output


def main():

    var1 = 3
    var2 = 4
    sum_of_vars = plus_function(var1, var2)

    print("The sum of the two variables {} and {} is: {}".format(var1, var2, sum_of_vars))


if __name__ == '__main__':
    main()
