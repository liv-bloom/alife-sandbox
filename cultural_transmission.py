# cultural_transmission.py
# Simulates the transmission of a "meme" (cultural trait) across a population of agents.
# This serves as a foundational model for "Historical Informatics" and cultural emergence.

import random

def simulate_meme_spread(population_size=100, generations=15):
    # 0 = doesn't have meme, 1 = has meme
    population = [0] * population_size
    population[0] = 1  # patient zero
    
    print(f"Starting Cultural Transmission Simulation (Population: {population_size})")
    
    history = [sum(population)]
    for gen in range(1, generations + 1):
        new_population = list(population)
        for i in range(population_size):
            if population[i] == 1:
                # Agent with the meme interacts with a random peer
                target = random.randint(0, population_size - 1)
                new_population[target] = 1
        population = new_population
        infected = sum(population)
        history.append(infected)
        
        bar = "█" * int((infected / population_size) * 50)
        print(f"Gen {gen:02d}: {infected:03d}/{population_size} [{bar.ljust(50)}]")
        
        if infected == population_size:
            print("Meme has saturated the population.")
            break
            
    return history

if __name__ == "__main__":
    simulate_meme_spread()
