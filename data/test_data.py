import data_generator

DATA_CASES={
    "max_255": lambda: data_generator.generate_random_string(255),
    "short": lambda: data_generator.generate_random_string(5),
    "long": lambda: data_generator.generate_random_string(25),
    "noupper": lambda: data_generator.generate_random_string_missing_uppercase(10),
    "nolower": lambda: data_generator.generate_random_string_missing_lowercase(10),
    "nodigit": lambda: data_generator.generate_random_string_no_digits(10),
    "no_special": lambda: data_generator.generate_random_string_no_special(10),
}