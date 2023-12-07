# Answer: 3374647

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

with open("./day5/input.txt") as f:
    seeds = [int(seed) for seed in f.readline().split(":")[-1].split()]
    
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

print("i: seed  ->  soil  -> fert  ->  wate ->  ligh ->  temp ->  humi ->  loca")
locations = list()

for i, seed in enumerate(seeds):

    soil = maps["seed-to-soil"].track(seed)
    fert = maps["soil-to-fertilizer"].track(soil)
    wate = maps["fertilizer-to-water"].track(fert)
    ligh = maps["water-to-light"].track(wate)
    temp = maps["light-to-temperature"].track(ligh)
    humi = maps["temperature-to-humidity"].track(temp)
    loca = maps["humidity-to-location"].track(humi)

    print(f"{i}: {seed:>4d}  ->  {soil:>4d}  -> {fert:>4d}  -> {wate:>4d}  ->  {ligh:>4d} ->  {temp:>4d} ->  {humi:>4d} ->  {loca:>4d}")
    
    locations.append(loca)

print("Answer: ", min(locations), "from seed:", seeds[locations.index(min(locations))])