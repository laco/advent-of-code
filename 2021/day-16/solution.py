# DAY 16
from typing import List
import math
from dataclasses import dataclass


@dataclass
class Packet:
    version: int
    type_: int
    length_in_bits: int


@dataclass
class LiteralValue(Packet):
    value: int


@dataclass
class Operator(Packet):
    packets: List[Packet]



def read_input():
    with open("./input.txt", "r", encoding="utf-8") as f:
        return parse_input(f.read())


def convert_to_bits(hexa_str: str) -> str:
    hexa_to_bits = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    return "".join([hexa_to_bits[hexa] for hexa in hexa_str])


def _bits_to_number(bits: str) -> int:
    return int(bits, 2)


def parse_input(input_str: str):
    return convert_to_bits(input_str)


def parse_packet(bits: str) -> Packet:
    version, type_ = _bits_to_number(bits[0:3]), _bits_to_number(bits[3:6])
    # print("PP", version, type_, bits)
    if type_ == 4:  # literal value
        value_bits = ""
        pointer = 6
        while True:
            is_last = bits[pointer] == "0"
            value_bits += bits[pointer + 1 : pointer + 5]
            if is_last:
                break
            else:
                pointer += 5
        return LiteralValue(
            version,
            type_,
            length_in_bits=pointer + 5,
            value=_bits_to_number(value_bits),
        )
    else:  # operator
        length_type = bits[6]
        sub_packets = []
        if length_type == "0":  # total length in bits
            total_length_of_bits = _bits_to_number(bits[7 : 7 + 15])
            start_of_sub_packets = 7 + 15
            end_of_operator_packets = start_of_sub_packets + total_length_of_bits
            sub_packet_pointer = start_of_sub_packets
            while True:
                sub_packet = parse_packet(
                    bits[sub_packet_pointer:end_of_operator_packets]
                )
                sub_packets.append(sub_packet)
                all_sub_packet_bits = sum(sp.length_in_bits for sp in sub_packets)
                if all_sub_packet_bits < total_length_of_bits:
                    sub_packet_pointer = start_of_sub_packets + all_sub_packet_bits
                else:
                    break
            return Operator(
                version,
                type_,
                length_in_bits=end_of_operator_packets,
                packets=sub_packets,
            )
        elif length_type == "1":  # number of sub-packets immediately contained
            number_of_sub_packets = _bits_to_number(bits[7 : 7 + 11])
            start_of_sub_packets = 7 + 11
            sub_packet_pointer = start_of_sub_packets
            while True:
                sub_packet = parse_packet(bits[sub_packet_pointer:])
                sub_packets.append(sub_packet)
                if len(sub_packets) < number_of_sub_packets:
                    sub_packet_pointer = sub_packet_pointer + sub_packet.length_in_bits
                else:
                    break
            return Operator(
                version,
                type_,
                length_in_bits=7 + 11 + sum(sp.length_in_bits for sp in sub_packets),
                packets=sub_packets,
            )


assert parse_packet("110100101111111000101000") == LiteralValue(6, 4, 21, 2021)

assert parse_packet(convert_to_bits("38006F45291200")) == Operator(
    version=1,
    type_=6,
    length_in_bits=49,
    packets=[
        LiteralValue(version=6, type_=4, length_in_bits=11, value=10),
        LiteralValue(version=2, type_=4, length_in_bits=16, value=20),
    ],
)

assert parse_packet(convert_to_bits("EE00D40C823060")) == Operator(
    version=7,
    type_=3,
    length_in_bits=51,
    packets=[
        LiteralValue(version=2, type_=4, length_in_bits=11, value=1),
        LiteralValue(version=4, type_=4, length_in_bits=11, value=2),
        LiteralValue(version=1, type_=4, length_in_bits=11, value=3),
    ],
)

assert parse_packet(convert_to_bits("8A004A801A8002F478")) == Operator(
    version=4,
    type_=2,
    length_in_bits=69,
    packets=[
        Operator(
            version=1,
            type_=2,
            length_in_bits=51,
            packets=[
                Operator(
                    version=5,
                    type_=2,
                    length_in_bits=33,
                    packets=[
                        LiteralValue(version=6, type_=4, length_in_bits=11, value=15)
                    ],
                )
            ],
        )
    ],
)

assert parse_packet(convert_to_bits("A0016C880162017C3686B18A3D4780")) == Operator(
    version=5,
    type_=0,
    length_in_bits=113,
    packets=[
        Operator(
            version=1,
            type_=0,
            length_in_bits=91,
            packets=[
                Operator(
                    version=3,
                    type_=0,
                    length_in_bits=73,
                    packets=[
                        LiteralValue(version=7, type_=4, length_in_bits=11, value=6),
                        LiteralValue(version=6, type_=4, length_in_bits=11, value=6),
                        LiteralValue(version=5, type_=4, length_in_bits=11, value=12),
                        LiteralValue(version=2, type_=4, length_in_bits=11, value=15),
                        LiteralValue(version=2, type_=4, length_in_bits=11, value=15),
                    ],
                )
            ],
        )
    ],
)

def version_sum(packet: Packet) -> int:
    if isinstance(packet, LiteralValue):
        return packet.version
    elif isinstance(packet, Operator):

        return packet.version + sum(version_sum(p) for p in packet.packets)

# print(read_input())
assert version_sum(parse_packet(convert_to_bits("A0016C880162017C3686B18A3D4780"))) == 31

print("Part 1")
v_sum = version_sum(parse_packet(read_input()))
print(v_sum)


def packet_value(packet: Packet) -> int:
    match packet.type_:
        case 0: # sum
            return sum(packet_value(p) for p in packet.packets)
        case 1: # product
            return math.prod([packet_value(p) for p in packet.packets])
        case 2: # minimum
            return min(packet_value(p) for p in packet.packets)
        case 3: # maximum
            return max(packet_value(p) for p in packet.packets)
        case 4: # literal value
            return packet.value
        case 5: # greater than
            return 1 if packet_value(packet.packets[0]) > packet_value(packet.packets[1]) else 0
        case 6: # less than
            return 1 if packet_value(packet.packets[0]) < packet_value(packet.packets[1]) else 0
        case 7: # equal to
            return 1 if packet_value(packet.packets[0]) == packet_value(packet.packets[1]) else 0


assert packet_value(parse_packet(convert_to_bits("C200B40A82"))) == 3
assert packet_value(parse_packet(convert_to_bits("04005AC33890"))) == 54
assert packet_value(parse_packet(convert_to_bits("880086C3E88112"))) == 7
assert packet_value(parse_packet(convert_to_bits("CE00C43D881120"))) == 9
assert packet_value(parse_packet(convert_to_bits("D8005AC2A8F0"))) == 1
assert packet_value(parse_packet(convert_to_bits("F600BC2D8F"))) == 0
assert packet_value(parse_packet(convert_to_bits("9C005AC2F8F0"))) == 0
assert packet_value(parse_packet(convert_to_bits("9C0141080250320F1802104A08"))) == 1

print("Part 2")
input_value = packet_value(parse_packet(read_input()))
print(input_value)