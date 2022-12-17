from typing import List, Set, Tuple
from itertools import cycle


def drop(rock: List[Tuple[int, int]], rocks: Set[Tuple[int, int]], jets: cycle) -> int:
    rock_height = 0
    while True:
        landed = False
        # blowing
        blow = True
        jet = next(jets)
        # print(jet)
        if jet == '<':
            for x, y in rock:
                if (x-1, y) in rocks or (x-1) < 0:
                    blow = False
                    break
            if blow:
                rock = [(x-1, y) for x, y in rock]
        elif jet == '>':
            for x, y in rock:
                if (x+1, y) in rocks or 6 < (x+1):
                    blow = False
                    break
            if blow:
                rock = [(x+1, y) for x, y in rock]

        # Falling
        for x, y in rock:
            if (x, y-1) in rocks or (y-1) < 0:
                landed = True
                break
        if not landed:
            rock = [(x, y-1) for x, y in rock]
        else:
            for pos in rock:
                rocks.add(pos)
                rock_height = max(rock_height, pos[1])
            break
    return rock_height


def print_grid(rocks: Set[Tuple[int, int]]):
    max_height = max([pos[1] for pos in rocks])
    grid = []
    for y in range(max_height):
        row = ['#' if (x, y) in rocks else '.' for x in range(0, 7)]
        grid.append(row)
    grid = reversed(grid)
    for row in grid:
        print(''.join(row))


def part1(lines: List[str]):
    jets = cycle(lines[0])
    rock_types = cycle(['-', '+', 'L', 'I', 'o'])

    max_height = -1
    rocks = set()
    for i in range(2022):
        rock_type = next(rock_types)
        # print(rock_type)
        if rock_type == '-':
            rock = [(2, max_height+4), (3, max_height+4), (4, max_height+4), (5, max_height+4)]
        elif rock_type == '+':
            rock = [(3, max_height+4), (2, max_height+5), (3, max_height+5), (4, max_height+5), (3, max_height+6)]
        elif rock_type == 'L':
            rock = [(2, max_height+4), (3, max_height+4), (4, max_height+4), (4, max_height+5), (4, max_height+6)]
        elif rock_type == 'I':
            rock = [(2, max_height+4), (2, max_height+5), (2, max_height+6), (2, max_height+7)]
        elif rock_type == 'o':
            rock = [(2, max_height+4), (3, max_height+4), (2, max_height+5), (3, max_height+5)]

        rock_height = drop(rock, rocks, jets)
        max_height = max(max_height, rock_height)

        # print(i)
        # print_grid(rocks)
        # if i == 4: break

    print('part1:', max_height+1)


def part2(lines: List[str]):
    jets = cycle(lines[0])
    rock_types = cycle(['-', '+', 'L', 'I', 'o'])

    max_height = -1
    rocks = set()
    print(len(lines[0]))
    max_diffs = ''
    for i in range(1_000_000_000_000):
        rock_type = next(rock_types)
        # print(rock_type)
        if rock_type == '-':
            rock = [(2, max_height+4), (3, max_height+4), (4, max_height+4), (5, max_height+4)]
        elif rock_type == '+':
            rock = [(3, max_height+4), (2, max_height+5), (3, max_height+5), (4, max_height+5), (3, max_height+6)]
        elif rock_type == 'L':
            rock = [(2, max_height+4), (3, max_height+4), (4, max_height+4), (4, max_height+5), (4, max_height+6)]
        elif rock_type == 'I':
            rock = [(2, max_height+4), (2, max_height+5), (2, max_height+6), (2, max_height+7)]
        elif rock_type == 'o':
            rock = [(2, max_height+4), (3, max_height+4), (2, max_height+5), (3, max_height+5)]

        rock_height = drop(rock, rocks, jets)
        new_max_height = max(max_height, rock_height)

        max_diffs += str(new_max_height - max_height)
        max_height = new_max_height

        # print(i)
        # print_grid(rocks)
        if i == 100_000:
            with open('max_diffs.out', 'w') as f:
                f.write(max_diffs)

    print('part2:', max_height+1)


if __name__ == '__main__':
    # print('test.txt')
    # with open('test.txt', 'r') as f:
    #     lines = f.readlines()
    #     lines = [line.replace('\n', '') for line in lines]
    #     part1(lines)
    #     part2(lines)

    # print('input.txt')
    # with open('input.txt', 'r') as f:
    #     lines = f.readlines()
    #     lines = [line.replace('\n', '') for line in lines]
    #     part1(lines)
    #     part2(lines)

    s = '3020132221212200310130301232012320133220300112342133201303213242133201212013222130321334013320130101330002322123221234010340132401322213020132001322213300030110321213212012001212213240122401334012200122001303002320132401210113320133021222013340123001332213302123010302013300121221322213340003011234013302003421222003001033400200013020130300332212340133201222213001032001301013300132100332012340101321322010312133001224000122030021222013220123201322002340130321322012140023221031002212023401032213200133421320013322133201324000300133001303003300132101324013320132100332012322003421302213302122100322013220133201332213322133421321213220132201212012300133021230012320020301304013220123220303003320122221322212322113421214212211030301330002342132421230212340133021330213220133401330013322130401324012202130201334003300133401320012302103421212212301013201212012120123221303003300122221230013222030001213200040132221210113222130221013003222130301322213210103421332213320133221301113320133021322212130133020030213320130421232013322133001302213030132200232013320133020030010320022100301200311133001330013320133001322012322133221121201320130121332213220133000220202211112111211012300121011224013320133401334013242003001334200040023400032013200112121212213032022220034213302132400020200240133001303212120133400232013302133201332212120133401332213220133001332213300003011320213202122420300013300133001302213001130220032213012133001330002340121010301113220132401320200300130221303000102130000322013201132201322012220133200230212202130300330002322132011320011212133421214012122003021302010322132221332013200112401332213220132111221111220133401030003340003021230212240130321321213200133001330213320121011322012300021111330013340023201304000300133221'
    s = sum([int(c) for i, c in enumerate(s) if i < 44])
    print(s)
