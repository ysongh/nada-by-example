from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    x = SecretInteger(Input(name="x", party=party_alice))
    y = SecretInteger(Input(name="y", party=party_bob))
    # Comparison: x > y (Greater Than)
    result = x > y
    return [Output(result, "x_greater_than_y", party=party_charlie)]