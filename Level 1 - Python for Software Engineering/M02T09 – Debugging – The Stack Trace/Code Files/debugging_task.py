# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])  # Fix: corrected variable name (Changed k to key)


# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {
    "lisa": "BAAAAAART!",
    "bart": "Eat My Shorts!",
    "marge": "Mmm~mmmmm",
    "homer": "d'oh!",  # Fix: Changed from single quotes to double quotes
    "maggie": "(Pacifier Suck)",
}

# Fix: Corrected number of inputs
# changed second parameter onwards to be a single list
print_values_of(simpson_catch_phrases, ["lisa", "bart", "homer"])

"""
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

"""
