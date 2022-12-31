import json
from typing import Iterable, List, Literal, Tuple, Union

Value = Union[List["Value"], int]
Packet = List[Value]
PacketPairs = Iterable[Tuple[Packet, Packet]]
FuzzyBool = Literal[-1, 0, 1]


def parse_lines(lines: Iterable[str]) -> PacketPairs:
    lines = iter(lines)
    for line1 in lines:
        packet1 = json.loads(line1)

        line2 = next(lines)
        packet2 = json.loads(line2)

        next(lines, None) # blank line

        yield packet1, packet2


def compare_ints(int1: int, int2: int) -> FuzzyBool:
    return -1 if int1 > int2 else 1 if int1 < int2 else 0


def compare_lists(list1: List[Value], list2: List[Value]) -> FuzzyBool:
    for val1, val2 in zip(list1, list2):
        cmp = compare_values(val1, val2)
        if cmp != 0:
            return cmp
    return -1 if len(list1) > len(list2) else 1 if len(list1) < len(list2) else 0


def compare_values(value1: Value, value2: Value) -> FuzzyBool:
    if isinstance(value1, int) and isinstance(value2, int):
        return compare_ints(value1, value2)

    if isinstance(value1, int):
        return compare_lists([value1], value2)

    if isinstance(value2, int):
        return compare_lists(value1, [value2])

    return compare_lists(value1, value2)


def compare_packets(packet1: Packet, packet2: Packet) -> bool:
    return compare_values(packet1, packet2) >= 0


def get_correct_packet_indices_sum(packet_pairs: PacketPairs) -> int:
    cumsum = 0
    for i, (packet1, packet2) in enumerate(packet_pairs):
        if compare_packets(packet1, packet2):
            cumsum += i + 1
    return cumsum


def pairs_to_iter(packet_pairs: PacketPairs) -> Iterable[Packet]:
    for p1, p2 in packet_pairs:
        yield p1
        yield p2


def split_on_packet(
    packets: List[Packet], pivot: Packet
) -> Tuple[List[Packet], List[Packet]]:
    left, right = [], []
    for packet in packets:
        if compare_packets(packet, pivot):
            left.append(packet)
        else:
            right.append(packet)
    return left, right


def get_decoder_key(packets: List[Packet]) -> int:
    left, rest = split_on_packet(packets, [[2]])
    mid, right = split_on_packet(rest, [[6]])
    
    first_index = len(left) + 1
    second_index = len(mid) + first_index + 1
    return first_index * second_index


def main(input_path="input"):
    with open(input_path) as f:
        lines = f.read().splitlines()

    packet_pairs = list(parse_lines(lines))
    packets = list(pairs_to_iter(packet_pairs))

    part1 = get_correct_packet_indices_sum(packet_pairs)
    part2 = get_decoder_key(packets)

    return part1, part2


if __name__ == '__main__':
    print(main())
