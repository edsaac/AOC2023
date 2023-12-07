# Answer: 6082852
# 
# Performance:
# real    0m59.589s
# user    0m59.588s
# sys     0m0.001s

from dataclasses import dataclass

@dataclass
class Map:
    map_name: str
    destination_range_start: list[int]
    source_range_start: list[int]
    range_len: list[int]

    def track(self, input):
        
        idx = None

        for i, (source, rng) in enumerate(zip(self.source_range_start, self.range_len)):
            
            ## Check which rule applies for the input 
            if input in range(source, source + rng):
                idx = i
                delta = input - source
                break
        
        if type(idx) is int:
            return self.destination_range_start[idx] + delta
        
        else:
            return input

    def uptrack(self, output):

        idx = None

        for i, (destination, rng) in enumerate(zip(self.destination_range_start, self.range_len)):

            if output in range(destination, destination + rng):
                idx = i
                delta = output - destination
                break

        if type(idx) is int:
            return self.source_range_start[idx] + delta
        
        else:
            return output

with open("./day5/input.txt") as f:
    seeds = [int(seed) for seed in f.readline().split(":")[-1].split()]
    seeds_start = seeds[::2]
    seeds_range = seeds[1::2]
    seeds = [range(seed, seed + rng) for seed,rng in zip(seeds_start, seeds_range)]
    
    maps = dict()

    for line in f:
        
        if "map:" in line:

            ## Close up previous map
            try:
                maps[map_id] = Map(
                        map_name = map_id,
                        destination_range_start = destinations,
                        source_range_start= sources,
                        range_len= ranges
                )

            except NameError:
                ...

            ## Initialize a new map
            map_id = line.split()[0]
            maps[map_id] = list()
            destinations = list()
            sources = list()
            ranges = list()

        elif line[0].isdigit():
            d,s,r = line.split()
            destinations.append(int(d))
            sources.append(int(s))
            ranges.append(int(r))

    maps[map_id] = Map(
            map_name = map_id,
            destination_range_start = destinations,
            source_range_start= sources,
            range_len= ranges
    )


loca = 0
stop_look = False

while (not stop_look) and (loca < 10_000_000):

    humi = maps["humidity-to-location"].uptrack(loca)
    temp = maps["temperature-to-humidity"].uptrack(humi)
    ligh = maps["light-to-temperature"].uptrack(temp)
    wate = maps["water-to-light"].uptrack(ligh)
    fert = maps["fertilizer-to-water"].uptrack(wate)
    soil = maps["soil-to-fertilizer"].uptrack(fert)
    seed = maps["seed-to-soil"].uptrack(soil)

    for available_seeds in seeds:
        if seed in available_seeds:
            print("Seed is available!")
            print("seed  <-  soil  <- fert  <-  wate <-  ligh <-  temp <-  humi <-  loca")
            print(f"{seed:>4d}  ->  {soil:>4d}  -> {fert:>4d}  -> {wate:>4d}  ->  {ligh:>4d} ->  {temp:>4d} ->  {humi:>4d} ->  {loca:>4d}".replace("->", "<-"))
            stop_look = True

    loca += 1
