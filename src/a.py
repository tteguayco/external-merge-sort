import utils.randomint as rndint


if __name__ == "__main__":
    rnd_int_generator = rndint.RandomIntGenerator()
    rnd_int = rnd_int_generator.generate_random_int()

    print(rnd_int)
