import sys
import bisect
from typing import (
    List,
    Set,
    Tuple,
    Union,
)
if sys.version_info >= (3, 9):
    from collections.abc import (
        Generator,
        Iterable,
    )
else:
    from typing import (
        Generator,
        Iterable,
    )


_MAX_WIDTH: int = 78
_INDENT: str = "   " # + 1


def is_valid(identifier: str) -> bool:
    """Determine if `identifier` can be used as a Python identifier."""
    seen: Set[str] = set()
    for i, c in enumerate(identifier):
        if c in seen:
            continue

        o = ord(c)
        idx = bisect.bisect_right(START_VALUES, o) - 1
        if idx < 0:
            return False

        # ensure valid starter
        if not i and not VALID_STARTERS[idx]:
            return False

        # ensure valid non-starter
        if o > STOP_VALUES[idx]:
            return False

        seen.add(c)

    return True


def list_all() -> Generator[Tuple[int, bool], None, None]:
    """Generate all valid unicode code points that can be used in Python
    identifiers. Values are generated as tuples of `int` (the code
    point) and `bool` (whether or not it can be used as the first
    value of an identifier).

    """
    for start, stop, valid_starter in zip(
        START_VALUES, STOP_VALUES, VALID_STARTERS
    ):
        for i in range(start, stop + 1):
            yield (i, valid_starter)


def list_starters() -> Generator[int, None, None]:
    """Generate all valid unicode code points that can be used as the
    first value in a Python identifier (or in any other position).

    """
    for start, stop, valid_starter in zip(
        START_VALUES, STOP_VALUES, VALID_STARTERS
    ):
        if valid_starter:
            yield from range(start, stop + 1)


def list_non_starters() -> Generator[int, None, None]:
    """Generate all valid unicode code points that cannot be used as the
    first value in a Python identifier (but may be used in any other
    position).

    """
    for start, stop, valid_starter in zip(
        START_VALUES, STOP_VALUES, VALID_STARTERS
    ):
        if not valid_starter:
            yield from range(start, stop + 1)


def _build() -> List[Tuple[int, int, bool]]:
    """Build the ranges used by the primary functions."""
    # build range values
    ranges: List[Tuple[int, int, bool]] = list()
    start: Union[int, None] = None
    starter: bool = False

    for i in range(0x110000):
        if i == 35:
            # comment character inherantly won't cause issue
            continue

        # try as starter
        try:
            exec(f"{chr(i)}=0")

            # push range into ranges and update values (i/a)
            if start is None:
                start = i
                starter = True
            elif starter is False:
                ranges.append((start, i - 1, False))
                start = i
                starter = True

            continue
        except Exception:
            pass

        # try as non-starter
        try:
            exec(f"_{chr(i)}=0")

            # push range into ranges and update values (i/a)
            if start is None:
                start = i
                starter = False
            elif starter is True:
                ranges.append((start, i - 1, True))
                start = i
                starter = False

            continue
        except Exception:
            pass

        # invalid character
        if start is not None:
            ranges.append((start, i - 1, starter))
            start = None

    if start is not None:
        ranges.append((start, i, starter))

    return ranges


def _fmt_tuple(
    header: str, values: Iterable[str]
) -> Generator[str, None, None]:
    yield f"{header} = ("
    current_line: str = _INDENT
    for v in values:
        if len(current_line) + len(v) + 2 > _MAX_WIDTH:
            yield current_line
            current_line = _INDENT
        current_line += f" {v},"
    if current_line.strip():
        yield current_line
    yield ")"


def _update() -> None:
    with open(__file__, "r") as infile:
        data = infile.read().splitlines()

    for i, line in enumerate(data):
        if line.startswith("#! RANGES"):
            data = data[:i + 1]
            break

    start_values, stop_values, valid_starters = tuple(zip(*_build()))

    # start values
    data.extend(_fmt_tuple(
        header="START_VALUES: Tuple[int, ...]",
        values=(f"0x{v:06x}" for v in start_values)
    ))

    # stop values
    data.extend(_fmt_tuple(
        header="STOP_VALUES: Tuple[int, ...]",
        values=(f"0x{v:06x}" for v in stop_values)
    ))

    # valid starters
    data.extend(_fmt_tuple(
        header="VALID_STARTERS: Tuple[bool, ...]",
        values=map(str, valid_starters)
    ))

    # empty last line
    data.append("")

    # write
    with open(__file__, "w") as outfile:
        outfile.write("\n".join(data))


def _test() -> None:
    for i in range(0x110000):
        if i == 35:
            # comment character inherantly won't cause issue
            continue

        assert_msg = f"chr={i:06x} @ {{}}".format

        # try as starter
        try:
            exec(f"{chr(i)}=0")
            assert is_valid(chr(i)), assert_msg(1)
            continue
        except Exception:
            pass

        # try as non-starter
        try:
            exec(f"_{chr(i)}=0")
            assert is_valid(f"_{chr(i)}"), assert_msg(2)
            assert not is_valid(chr(i)), assert_msg(3)
            continue
        except Exception:
            pass

        assert not is_valid(chr(i)), assert_msg(4)
        assert not is_valid(f"_{chr(i)}"), assert_msg(5)


#! RANGES
START_VALUES: Tuple[int, ...] = (
    0x000009, 0x00000c, 0x000020, 0x000026, 0x00002a, 0x00002d, 0x000030,
    0x00003c, 0x000041, 0x00005e, 0x00005f, 0x000061, 0x00007c, 0x0000aa,
    0x0000b5, 0x0000b7, 0x0000ba, 0x0000c0, 0x0000d8, 0x0000f8, 0x0002c6,
    0x0002e0, 0x0002ec, 0x0002ee, 0x000300, 0x000370, 0x000376, 0x00037b,
    0x00037f, 0x000386, 0x000387, 0x000388, 0x00038c, 0x00038e, 0x0003a3,
    0x0003f7, 0x000483, 0x00048a, 0x000531, 0x000559, 0x000560, 0x000591,
    0x0005bf, 0x0005c1, 0x0005c4, 0x0005c7, 0x0005d0, 0x0005ef, 0x000610,
    0x000620, 0x00064b, 0x00066e, 0x000670, 0x000671, 0x0006d5, 0x0006d6,
    0x0006df, 0x0006e5, 0x0006e7, 0x0006ea, 0x0006ee, 0x0006f0, 0x0006fa,
    0x0006ff, 0x000710, 0x000711, 0x000712, 0x000730, 0x00074d, 0x0007a6,
    0x0007b1, 0x0007c0, 0x0007ca, 0x0007eb, 0x0007f4, 0x0007fa, 0x0007fd,
    0x000800, 0x000816, 0x00081a, 0x00081b, 0x000824, 0x000825, 0x000828,
    0x000829, 0x000840, 0x000859, 0x000860, 0x0008a0, 0x0008b6, 0x0008d3,
    0x0008e3, 0x000904, 0x00093a, 0x00093d, 0x00093e, 0x000950, 0x000951,
    0x000958, 0x000962, 0x000966, 0x000971, 0x000981, 0x000985, 0x00098f,
    0x000993, 0x0009aa, 0x0009b2, 0x0009b6, 0x0009bc, 0x0009bd, 0x0009be,
    0x0009c7, 0x0009cb, 0x0009ce, 0x0009d7, 0x0009dc, 0x0009df, 0x0009e2,
    0x0009e6, 0x0009f0, 0x0009fc, 0x0009fe, 0x000a01, 0x000a05, 0x000a0f,
    0x000a13, 0x000a2a, 0x000a32, 0x000a35, 0x000a38, 0x000a3c, 0x000a3e,
    0x000a47, 0x000a4b, 0x000a51, 0x000a59, 0x000a5e, 0x000a66, 0x000a72,
    0x000a75, 0x000a81, 0x000a85, 0x000a8f, 0x000a93, 0x000aaa, 0x000ab2,
    0x000ab5, 0x000abc, 0x000abd, 0x000abe, 0x000ac7, 0x000acb, 0x000ad0,
    0x000ae0, 0x000ae2, 0x000ae6, 0x000af9, 0x000afa, 0x000b01, 0x000b05,
    0x000b0f, 0x000b13, 0x000b2a, 0x000b32, 0x000b35, 0x000b3c, 0x000b3d,
    0x000b3e, 0x000b47, 0x000b4b, 0x000b56, 0x000b5c, 0x000b5f, 0x000b62,
    0x000b66, 0x000b71, 0x000b82, 0x000b83, 0x000b85, 0x000b8e, 0x000b92,
    0x000b99, 0x000b9c, 0x000b9e, 0x000ba3, 0x000ba8, 0x000bae, 0x000bbe,
    0x000bc6, 0x000bca, 0x000bd0, 0x000bd7, 0x000be6, 0x000c00, 0x000c05,
    0x000c0e, 0x000c12, 0x000c2a, 0x000c3d, 0x000c3e, 0x000c46, 0x000c4a,
    0x000c55, 0x000c58, 0x000c60, 0x000c62, 0x000c66, 0x000c80, 0x000c81,
    0x000c85, 0x000c8e, 0x000c92, 0x000caa, 0x000cb5, 0x000cbc, 0x000cbd,
    0x000cbe, 0x000cc6, 0x000cca, 0x000cd5, 0x000cde, 0x000ce0, 0x000ce2,
    0x000ce6, 0x000cf1, 0x000d00, 0x000d05, 0x000d0e, 0x000d12, 0x000d3b,
    0x000d3d, 0x000d3e, 0x000d46, 0x000d4a, 0x000d4e, 0x000d54, 0x000d57,
    0x000d5f, 0x000d62, 0x000d66, 0x000d7a, 0x000d82, 0x000d85, 0x000d9a,
    0x000db3, 0x000dbd, 0x000dc0, 0x000dca, 0x000dcf, 0x000dd6, 0x000dd8,
    0x000de6, 0x000df2, 0x000e01, 0x000e31, 0x000e32, 0x000e33, 0x000e40,
    0x000e47, 0x000e50, 0x000e81, 0x000e84, 0x000e86, 0x000e8c, 0x000ea5,
    0x000ea7, 0x000eb1, 0x000eb2, 0x000eb3, 0x000ebd, 0x000ec0, 0x000ec6,
    0x000ec8, 0x000ed0, 0x000edc, 0x000f00, 0x000f18, 0x000f20, 0x000f35,
    0x000f37, 0x000f39, 0x000f3e, 0x000f40, 0x000f49, 0x000f71, 0x000f86,
    0x000f88, 0x000f8d, 0x000f99, 0x000fc6, 0x001000, 0x00102b, 0x00103f,
    0x001040, 0x001050, 0x001056, 0x00105a, 0x00105e, 0x001061, 0x001062,
    0x001065, 0x001067, 0x00106e, 0x001071, 0x001075, 0x001082, 0x00108e,
    0x00108f, 0x0010a0, 0x0010c7, 0x0010cd, 0x0010d0, 0x0010fc, 0x00124a,
    0x001250, 0x001258, 0x00125a, 0x001260, 0x00128a, 0x001290, 0x0012b2,
    0x0012b8, 0x0012c0, 0x0012c2, 0x0012c8, 0x0012d8, 0x001312, 0x001318,
    0x00135d, 0x001369, 0x001380, 0x0013a0, 0x0013f8, 0x001401, 0x00166f,
    0x001681, 0x0016a0, 0x0016ee, 0x001700, 0x00170e, 0x001712, 0x001720,
    0x001732, 0x001740, 0x001752, 0x001760, 0x00176e, 0x001772, 0x001780,
    0x0017b4, 0x0017d7, 0x0017dc, 0x0017dd, 0x0017e0, 0x00180b, 0x001810,
    0x001820, 0x001880, 0x0018a9, 0x0018aa, 0x0018b0, 0x001900, 0x001920,
    0x001930, 0x001946, 0x001950, 0x001970, 0x001980, 0x0019b0, 0x0019d0,
    0x001a00, 0x001a17, 0x001a20, 0x001a55, 0x001a60, 0x001a7f, 0x001a90,
    0x001aa7, 0x001ab0, 0x001b00, 0x001b05, 0x001b34, 0x001b45, 0x001b50,
    0x001b6b, 0x001b80, 0x001b83, 0x001ba1, 0x001bae, 0x001bb0, 0x001bba,
    0x001be6, 0x001c00, 0x001c24, 0x001c40, 0x001c4d, 0x001c50, 0x001c5a,
    0x001c80, 0x001c90, 0x001cbd, 0x001cd0, 0x001cd4, 0x001ce9, 0x001ced,
    0x001cee, 0x001cf4, 0x001cf5, 0x001cf7, 0x001cfa, 0x001d00, 0x001dc0,
    0x001dfb, 0x001e00, 0x001f18, 0x001f20, 0x001f48, 0x001f50, 0x001f59,
    0x001f5b, 0x001f5d, 0x001f5f, 0x001f80, 0x001fb6, 0x001fbe, 0x001fc2,
    0x001fc6, 0x001fd0, 0x001fd6, 0x001fe0, 0x001ff2, 0x001ff6, 0x00203f,
    0x002054, 0x002071, 0x00207f, 0x002090, 0x0020d0, 0x0020e1, 0x0020e5,
    0x002102, 0x002107, 0x00210a, 0x002115, 0x002118, 0x002124, 0x002126,
    0x002128, 0x00212a, 0x00213c, 0x002145, 0x00214e, 0x002160, 0x002c00,
    0x002c30, 0x002c60, 0x002ceb, 0x002cef, 0x002cf2, 0x002d00, 0x002d27,
    0x002d2d, 0x002d30, 0x002d6f, 0x002d7f, 0x002d80, 0x002da0, 0x002da8,
    0x002db0, 0x002db8, 0x002dc0, 0x002dc8, 0x002dd0, 0x002dd8, 0x002de0,
    0x003005, 0x003021, 0x00302a, 0x003031, 0x003038, 0x003041, 0x003099,
    0x00309d, 0x0030a1, 0x0030fc, 0x003105, 0x003131, 0x0031a0, 0x0031f0,
    0x003400, 0x004e00, 0x00a000, 0x00a4d0, 0x00a500, 0x00a610, 0x00a620,
    0x00a62a, 0x00a640, 0x00a66f, 0x00a674, 0x00a67f, 0x00a69e, 0x00a6a0,
    0x00a6f0, 0x00a717, 0x00a722, 0x00a78b, 0x00a7c2, 0x00a7f7, 0x00a802,
    0x00a803, 0x00a806, 0x00a807, 0x00a80b, 0x00a80c, 0x00a823, 0x00a840,
    0x00a880, 0x00a882, 0x00a8b4, 0x00a8d0, 0x00a8e0, 0x00a8f2, 0x00a8fb,
    0x00a8fd, 0x00a8ff, 0x00a90a, 0x00a926, 0x00a930, 0x00a947, 0x00a960,
    0x00a980, 0x00a984, 0x00a9b3, 0x00a9cf, 0x00a9d0, 0x00a9e0, 0x00a9e5,
    0x00a9e6, 0x00a9f0, 0x00a9fa, 0x00aa00, 0x00aa29, 0x00aa40, 0x00aa43,
    0x00aa44, 0x00aa4c, 0x00aa50, 0x00aa60, 0x00aa7a, 0x00aa7b, 0x00aa7e,
    0x00aab0, 0x00aab1, 0x00aab2, 0x00aab5, 0x00aab7, 0x00aab9, 0x00aabe,
    0x00aac0, 0x00aac1, 0x00aac2, 0x00aadb, 0x00aae0, 0x00aaeb, 0x00aaf2,
    0x00aaf5, 0x00ab01, 0x00ab09, 0x00ab11, 0x00ab20, 0x00ab28, 0x00ab30,
    0x00ab5c, 0x00ab70, 0x00abe3, 0x00abec, 0x00abf0, 0x00ac00, 0x00d7b0,
    0x00d7cb, 0x00f900, 0x00fa70, 0x00fb00, 0x00fb13, 0x00fb1d, 0x00fb1e,
    0x00fb1f, 0x00fb2a, 0x00fb38, 0x00fb3e, 0x00fb40, 0x00fb43, 0x00fb46,
    0x00fbd3, 0x00fc64, 0x00fd50, 0x00fd92, 0x00fdf0, 0x00fe00, 0x00fe20,
    0x00fe33, 0x00fe4d, 0x00fe71, 0x00fe73, 0x00fe77, 0x00fe79, 0x00fe7b,
    0x00fe7d, 0x00fe7f, 0x00ff10, 0x00ff21, 0x00ff3f, 0x00ff41, 0x00ff66,
    0x00ff9e, 0x00ffa0, 0x00ffc2, 0x00ffca, 0x00ffd2, 0x00ffda, 0x010000,
    0x01000d, 0x010028, 0x01003c, 0x01003f, 0x010050, 0x010080, 0x010140,
    0x0101fd, 0x010280, 0x0102a0, 0x0102e0, 0x010300, 0x01032d, 0x010350,
    0x010376, 0x010380, 0x0103a0, 0x0103c8, 0x0103d1, 0x010400, 0x0104a0,
    0x0104b0, 0x0104d8, 0x010500, 0x010530, 0x010600, 0x010740, 0x010760,
    0x010800, 0x010808, 0x01080a, 0x010837, 0x01083c, 0x01083f, 0x010860,
    0x010880, 0x0108e0, 0x0108f4, 0x010900, 0x010920, 0x010980, 0x0109be,
    0x010a00, 0x010a01, 0x010a05, 0x010a0c, 0x010a10, 0x010a15, 0x010a19,
    0x010a38, 0x010a3f, 0x010a60, 0x010a80, 0x010ac0, 0x010ac9, 0x010ae5,
    0x010b00, 0x010b40, 0x010b60, 0x010b80, 0x010c00, 0x010c80, 0x010cc0,
    0x010d00, 0x010d24, 0x010d30, 0x010f00, 0x010f27, 0x010f30, 0x010f46,
    0x010fe0, 0x011000, 0x011003, 0x011038, 0x011066, 0x01107f, 0x011083,
    0x0110b0, 0x0110d0, 0x0110f0, 0x011100, 0x011103, 0x011127, 0x011136,
    0x011144, 0x011145, 0x011150, 0x011173, 0x011176, 0x011180, 0x011183,
    0x0111b3, 0x0111c1, 0x0111c9, 0x0111d0, 0x0111da, 0x0111dc, 0x011200,
    0x011213, 0x01122c, 0x01123e, 0x011280, 0x011288, 0x01128a, 0x01128f,
    0x01129f, 0x0112b0, 0x0112df, 0x0112f0, 0x011300, 0x011305, 0x01130f,
    0x011313, 0x01132a, 0x011332, 0x011335, 0x01133b, 0x01133d, 0x01133e,
    0x011347, 0x01134b, 0x011350, 0x011357, 0x01135d, 0x011362, 0x011366,
    0x011370, 0x011400, 0x011435, 0x011447, 0x011450, 0x01145e, 0x01145f,
    0x011480, 0x0114b0, 0x0114c4, 0x0114c7, 0x0114d0, 0x011580, 0x0115af,
    0x0115b8, 0x0115d8, 0x0115dc, 0x011600, 0x011630, 0x011644, 0x011650,
    0x011680, 0x0116ab, 0x0116b8, 0x0116c0, 0x011700, 0x01171d, 0x011730,
    0x011800, 0x01182c, 0x0118a0, 0x0118e0, 0x0118ff, 0x0119a0, 0x0119aa,
    0x0119d1, 0x0119da, 0x0119e1, 0x0119e3, 0x0119e4, 0x011a00, 0x011a01,
    0x011a0b, 0x011a33, 0x011a3a, 0x011a3b, 0x011a47, 0x011a50, 0x011a51,
    0x011a5c, 0x011a8a, 0x011a9d, 0x011ac0, 0x011c00, 0x011c0a, 0x011c2f,
    0x011c38, 0x011c40, 0x011c50, 0x011c72, 0x011c92, 0x011ca9, 0x011d00,
    0x011d08, 0x011d0b, 0x011d31, 0x011d3a, 0x011d3c, 0x011d3f, 0x011d46,
    0x011d47, 0x011d50, 0x011d60, 0x011d67, 0x011d6a, 0x011d8a, 0x011d90,
    0x011d93, 0x011d98, 0x011da0, 0x011ee0, 0x011ef3, 0x012000, 0x012400,
    0x012480, 0x013000, 0x014400, 0x016800, 0x016a40, 0x016a60, 0x016ad0,
    0x016af0, 0x016b00, 0x016b30, 0x016b40, 0x016b50, 0x016b63, 0x016b7d,
    0x016e40, 0x016f00, 0x016f4f, 0x016f50, 0x016f51, 0x016f8f, 0x016f93,
    0x016fe0, 0x016fe3, 0x017000, 0x018800, 0x01b000, 0x01b150, 0x01b164,
    0x01b170, 0x01bc00, 0x01bc70, 0x01bc80, 0x01bc90, 0x01bc9d, 0x01d165,
    0x01d16d, 0x01d17b, 0x01d185, 0x01d1aa, 0x01d242, 0x01d400, 0x01d456,
    0x01d49e, 0x01d4a2, 0x01d4a5, 0x01d4a9, 0x01d4ae, 0x01d4bb, 0x01d4bd,
    0x01d4c5, 0x01d507, 0x01d50d, 0x01d516, 0x01d51e, 0x01d53b, 0x01d540,
    0x01d546, 0x01d54a, 0x01d552, 0x01d6a8, 0x01d6c2, 0x01d6dc, 0x01d6fc,
    0x01d716, 0x01d736, 0x01d750, 0x01d770, 0x01d78a, 0x01d7aa, 0x01d7c4,
    0x01d7ce, 0x01da00, 0x01da3b, 0x01da75, 0x01da84, 0x01da9b, 0x01daa1,
    0x01e000, 0x01e008, 0x01e01b, 0x01e023, 0x01e026, 0x01e100, 0x01e130,
    0x01e137, 0x01e140, 0x01e14e, 0x01e2c0, 0x01e2ec, 0x01e800, 0x01e8d0,
    0x01e900, 0x01e944, 0x01e94b, 0x01e950, 0x01ee00, 0x01ee05, 0x01ee21,
    0x01ee24, 0x01ee27, 0x01ee29, 0x01ee34, 0x01ee39, 0x01ee3b, 0x01ee42,
    0x01ee47, 0x01ee49, 0x01ee4b, 0x01ee4d, 0x01ee51, 0x01ee54, 0x01ee57,
    0x01ee59, 0x01ee5b, 0x01ee5d, 0x01ee5f, 0x01ee61, 0x01ee64, 0x01ee67,
    0x01ee6c, 0x01ee74, 0x01ee79, 0x01ee7e, 0x01ee80, 0x01ee8b, 0x01eea1,
    0x01eea5, 0x01eeab, 0x020000, 0x02a700, 0x02b740, 0x02b820, 0x02ceb0,
    0x02f800, 0x0e0100,
)
STOP_VALUES: Tuple[int, ...] = (
    0x000009, 0x00000c, 0x000021, 0x000026, 0x00002b, 0x00002d, 0x000039,
    0x00003e, 0x00005a, 0x00005e, 0x00005f, 0x00007a, 0x00007c, 0x0000aa,
    0x0000b5, 0x0000b7, 0x0000ba, 0x0000d6, 0x0000f6, 0x0002c1, 0x0002d1,
    0x0002e4, 0x0002ec, 0x0002ee, 0x00036f, 0x000374, 0x000377, 0x00037d,
    0x00037f, 0x000386, 0x000387, 0x00038a, 0x00038c, 0x0003a1, 0x0003f5,
    0x000481, 0x000487, 0x00052f, 0x000556, 0x000559, 0x000588, 0x0005bd,
    0x0005bf, 0x0005c2, 0x0005c5, 0x0005c7, 0x0005ea, 0x0005f2, 0x00061a,
    0x00064a, 0x000669, 0x00066f, 0x000670, 0x0006d3, 0x0006d5, 0x0006dc,
    0x0006e4, 0x0006e6, 0x0006e8, 0x0006ed, 0x0006ef, 0x0006f9, 0x0006fc,
    0x0006ff, 0x000710, 0x000711, 0x00072f, 0x00074a, 0x0007a5, 0x0007b0,
    0x0007b1, 0x0007c9, 0x0007ea, 0x0007f3, 0x0007f5, 0x0007fa, 0x0007fd,
    0x000815, 0x000819, 0x00081a, 0x000823, 0x000824, 0x000827, 0x000828,
    0x00082d, 0x000858, 0x00085b, 0x00086a, 0x0008b4, 0x0008bd, 0x0008e1,
    0x000903, 0x000939, 0x00093c, 0x00093d, 0x00094f, 0x000950, 0x000957,
    0x000961, 0x000963, 0x00096f, 0x000980, 0x000983, 0x00098c, 0x000990,
    0x0009a8, 0x0009b0, 0x0009b2, 0x0009b9, 0x0009bc, 0x0009bd, 0x0009c4,
    0x0009c8, 0x0009cd, 0x0009ce, 0x0009d7, 0x0009dd, 0x0009e1, 0x0009e3,
    0x0009ef, 0x0009f1, 0x0009fc, 0x0009fe, 0x000a03, 0x000a0a, 0x000a10,
    0x000a28, 0x000a30, 0x000a33, 0x000a36, 0x000a39, 0x000a3c, 0x000a42,
    0x000a48, 0x000a4d, 0x000a51, 0x000a5c, 0x000a5e, 0x000a71, 0x000a74,
    0x000a75, 0x000a83, 0x000a8d, 0x000a91, 0x000aa8, 0x000ab0, 0x000ab3,
    0x000ab9, 0x000abc, 0x000abd, 0x000ac5, 0x000ac9, 0x000acd, 0x000ad0,
    0x000ae1, 0x000ae3, 0x000aef, 0x000af9, 0x000aff, 0x000b03, 0x000b0c,
    0x000b10, 0x000b28, 0x000b30, 0x000b33, 0x000b39, 0x000b3c, 0x000b3d,
    0x000b44, 0x000b48, 0x000b4d, 0x000b57, 0x000b5d, 0x000b61, 0x000b63,
    0x000b6f, 0x000b71, 0x000b82, 0x000b83, 0x000b8a, 0x000b90, 0x000b95,
    0x000b9a, 0x000b9c, 0x000b9f, 0x000ba4, 0x000baa, 0x000bb9, 0x000bc2,
    0x000bc8, 0x000bcd, 0x000bd0, 0x000bd7, 0x000bef, 0x000c04, 0x000c0c,
    0x000c10, 0x000c28, 0x000c39, 0x000c3d, 0x000c44, 0x000c48, 0x000c4d,
    0x000c56, 0x000c5a, 0x000c61, 0x000c63, 0x000c6f, 0x000c80, 0x000c83,
    0x000c8c, 0x000c90, 0x000ca8, 0x000cb3, 0x000cb9, 0x000cbc, 0x000cbd,
    0x000cc4, 0x000cc8, 0x000ccd, 0x000cd6, 0x000cde, 0x000ce1, 0x000ce3,
    0x000cef, 0x000cf2, 0x000d03, 0x000d0c, 0x000d10, 0x000d3a, 0x000d3c,
    0x000d3d, 0x000d44, 0x000d48, 0x000d4d, 0x000d4e, 0x000d56, 0x000d57,
    0x000d61, 0x000d63, 0x000d6f, 0x000d7f, 0x000d83, 0x000d96, 0x000db1,
    0x000dbb, 0x000dbd, 0x000dc6, 0x000dca, 0x000dd4, 0x000dd6, 0x000ddf,
    0x000def, 0x000df3, 0x000e30, 0x000e31, 0x000e32, 0x000e3a, 0x000e46,
    0x000e4e, 0x000e59, 0x000e82, 0x000e84, 0x000e8a, 0x000ea3, 0x000ea5,
    0x000eb0, 0x000eb1, 0x000eb2, 0x000ebc, 0x000ebd, 0x000ec4, 0x000ec6,
    0x000ecd, 0x000ed9, 0x000edf, 0x000f00, 0x000f19, 0x000f29, 0x000f35,
    0x000f37, 0x000f39, 0x000f3f, 0x000f47, 0x000f6c, 0x000f84, 0x000f87,
    0x000f8c, 0x000f97, 0x000fbc, 0x000fc6, 0x00102a, 0x00103e, 0x00103f,
    0x001049, 0x001055, 0x001059, 0x00105d, 0x001060, 0x001061, 0x001064,
    0x001066, 0x00106d, 0x001070, 0x001074, 0x001081, 0x00108d, 0x00108e,
    0x00109d, 0x0010c5, 0x0010c7, 0x0010cd, 0x0010fa, 0x001248, 0x00124d,
    0x001256, 0x001258, 0x00125d, 0x001288, 0x00128d, 0x0012b0, 0x0012b5,
    0x0012be, 0x0012c0, 0x0012c5, 0x0012d6, 0x001310, 0x001315, 0x00135a,
    0x00135f, 0x001371, 0x00138f, 0x0013f5, 0x0013fd, 0x00166c, 0x00167f,
    0x00169a, 0x0016ea, 0x0016f8, 0x00170c, 0x001711, 0x001714, 0x001731,
    0x001734, 0x001751, 0x001753, 0x00176c, 0x001770, 0x001773, 0x0017b3,
    0x0017d3, 0x0017d7, 0x0017dc, 0x0017dd, 0x0017e9, 0x00180d, 0x001819,
    0x001878, 0x0018a8, 0x0018a9, 0x0018aa, 0x0018f5, 0x00191e, 0x00192b,
    0x00193b, 0x00194f, 0x00196d, 0x001974, 0x0019ab, 0x0019c9, 0x0019da,
    0x001a16, 0x001a1b, 0x001a54, 0x001a5e, 0x001a7c, 0x001a89, 0x001a99,
    0x001aa7, 0x001abd, 0x001b04, 0x001b33, 0x001b44, 0x001b4b, 0x001b59,
    0x001b73, 0x001b82, 0x001ba0, 0x001bad, 0x001baf, 0x001bb9, 0x001be5,
    0x001bf3, 0x001c23, 0x001c37, 0x001c49, 0x001c4f, 0x001c59, 0x001c7d,
    0x001c88, 0x001cba, 0x001cbf, 0x001cd2, 0x001ce8, 0x001cec, 0x001ced,
    0x001cf3, 0x001cf4, 0x001cf6, 0x001cf9, 0x001cfa, 0x001dbf, 0x001df9,
    0x001dff, 0x001f15, 0x001f1d, 0x001f45, 0x001f4d, 0x001f57, 0x001f59,
    0x001f5b, 0x001f5d, 0x001f7d, 0x001fb4, 0x001fbc, 0x001fbe, 0x001fc4,
    0x001fcc, 0x001fd3, 0x001fdb, 0x001fec, 0x001ff4, 0x001ffc, 0x002040,
    0x002054, 0x002071, 0x00207f, 0x00209c, 0x0020dc, 0x0020e1, 0x0020f0,
    0x002102, 0x002107, 0x002113, 0x002115, 0x00211d, 0x002124, 0x002126,
    0x002128, 0x002139, 0x00213f, 0x002149, 0x00214e, 0x002188, 0x002c2e,
    0x002c5e, 0x002ce4, 0x002cee, 0x002cf1, 0x002cf3, 0x002d25, 0x002d27,
    0x002d2d, 0x002d67, 0x002d6f, 0x002d7f, 0x002d96, 0x002da6, 0x002dae,
    0x002db6, 0x002dbe, 0x002dc6, 0x002dce, 0x002dd6, 0x002dde, 0x002dff,
    0x003007, 0x003029, 0x00302f, 0x003035, 0x00303c, 0x003096, 0x00309a,
    0x00309f, 0x0030fa, 0x0030ff, 0x00312f, 0x00318e, 0x0031ba, 0x0031ff,
    0x004db5, 0x009fef, 0x00a48c, 0x00a4fd, 0x00a60c, 0x00a61f, 0x00a629,
    0x00a62b, 0x00a66e, 0x00a66f, 0x00a67d, 0x00a69d, 0x00a69f, 0x00a6ef,
    0x00a6f1, 0x00a71f, 0x00a788, 0x00a7bf, 0x00a7c6, 0x00a801, 0x00a802,
    0x00a805, 0x00a806, 0x00a80a, 0x00a80b, 0x00a822, 0x00a827, 0x00a873,
    0x00a881, 0x00a8b3, 0x00a8c5, 0x00a8d9, 0x00a8f1, 0x00a8f7, 0x00a8fb,
    0x00a8fe, 0x00a909, 0x00a925, 0x00a92d, 0x00a946, 0x00a953, 0x00a97c,
    0x00a983, 0x00a9b2, 0x00a9c0, 0x00a9cf, 0x00a9d9, 0x00a9e4, 0x00a9e5,
    0x00a9ef, 0x00a9f9, 0x00a9fe, 0x00aa28, 0x00aa36, 0x00aa42, 0x00aa43,
    0x00aa4b, 0x00aa4d, 0x00aa59, 0x00aa76, 0x00aa7a, 0x00aa7d, 0x00aaaf,
    0x00aab0, 0x00aab1, 0x00aab4, 0x00aab6, 0x00aab8, 0x00aabd, 0x00aabf,
    0x00aac0, 0x00aac1, 0x00aac2, 0x00aadd, 0x00aaea, 0x00aaef, 0x00aaf4,
    0x00aaf6, 0x00ab06, 0x00ab0e, 0x00ab16, 0x00ab26, 0x00ab2e, 0x00ab5a,
    0x00ab67, 0x00abe2, 0x00abea, 0x00abed, 0x00abf9, 0x00d7a3, 0x00d7c6,
    0x00d7fb, 0x00fa6d, 0x00fad9, 0x00fb06, 0x00fb17, 0x00fb1d, 0x00fb1e,
    0x00fb28, 0x00fb36, 0x00fb3c, 0x00fb3e, 0x00fb41, 0x00fb44, 0x00fbb1,
    0x00fc5d, 0x00fd3d, 0x00fd8f, 0x00fdc7, 0x00fdf9, 0x00fe0f, 0x00fe2f,
    0x00fe34, 0x00fe4f, 0x00fe71, 0x00fe73, 0x00fe77, 0x00fe79, 0x00fe7b,
    0x00fe7d, 0x00fefc, 0x00ff19, 0x00ff3a, 0x00ff3f, 0x00ff5a, 0x00ff9d,
    0x00ff9f, 0x00ffbe, 0x00ffc7, 0x00ffcf, 0x00ffd7, 0x00ffdc, 0x01000b,
    0x010026, 0x01003a, 0x01003d, 0x01004d, 0x01005d, 0x0100fa, 0x010174,
    0x0101fd, 0x01029c, 0x0102d0, 0x0102e0, 0x01031f, 0x01034a, 0x010375,
    0x01037a, 0x01039d, 0x0103c3, 0x0103cf, 0x0103d5, 0x01049d, 0x0104a9,
    0x0104d3, 0x0104fb, 0x010527, 0x010563, 0x010736, 0x010755, 0x010767,
    0x010805, 0x010808, 0x010835, 0x010838, 0x01083c, 0x010855, 0x010876,
    0x01089e, 0x0108f2, 0x0108f5, 0x010915, 0x010939, 0x0109b7, 0x0109bf,
    0x010a00, 0x010a03, 0x010a06, 0x010a0f, 0x010a13, 0x010a17, 0x010a35,
    0x010a3a, 0x010a3f, 0x010a7c, 0x010a9c, 0x010ac7, 0x010ae4, 0x010ae6,
    0x010b35, 0x010b55, 0x010b72, 0x010b91, 0x010c48, 0x010cb2, 0x010cf2,
    0x010d23, 0x010d27, 0x010d39, 0x010f1c, 0x010f27, 0x010f45, 0x010f50,
    0x010ff6, 0x011002, 0x011037, 0x011046, 0x01106f, 0x011082, 0x0110af,
    0x0110ba, 0x0110e8, 0x0110f9, 0x011102, 0x011126, 0x011134, 0x01113f,
    0x011144, 0x011146, 0x011172, 0x011173, 0x011176, 0x011182, 0x0111b2,
    0x0111c0, 0x0111c4, 0x0111cc, 0x0111d9, 0x0111da, 0x0111dc, 0x011211,
    0x01122b, 0x011237, 0x01123e, 0x011286, 0x011288, 0x01128d, 0x01129d,
    0x0112a8, 0x0112de, 0x0112ea, 0x0112f9, 0x011303, 0x01130c, 0x011310,
    0x011328, 0x011330, 0x011333, 0x011339, 0x01133c, 0x01133d, 0x011344,
    0x011348, 0x01134d, 0x011350, 0x011357, 0x011361, 0x011363, 0x01136c,
    0x011374, 0x011434, 0x011446, 0x01144a, 0x011459, 0x01145e, 0x01145f,
    0x0114af, 0x0114c3, 0x0114c5, 0x0114c7, 0x0114d9, 0x0115ae, 0x0115b5,
    0x0115c0, 0x0115db, 0x0115dd, 0x01162f, 0x011640, 0x011644, 0x011659,
    0x0116aa, 0x0116b7, 0x0116b8, 0x0116c9, 0x01171a, 0x01172b, 0x011739,
    0x01182b, 0x01183a, 0x0118df, 0x0118e9, 0x0118ff, 0x0119a7, 0x0119d0,
    0x0119d7, 0x0119e0, 0x0119e1, 0x0119e3, 0x0119e4, 0x011a00, 0x011a0a,
    0x011a32, 0x011a39, 0x011a3a, 0x011a3e, 0x011a47, 0x011a50, 0x011a5b,
    0x011a89, 0x011a99, 0x011a9d, 0x011af8, 0x011c08, 0x011c2e, 0x011c36,
    0x011c3f, 0x011c40, 0x011c59, 0x011c8f, 0x011ca7, 0x011cb6, 0x011d06,
    0x011d09, 0x011d30, 0x011d36, 0x011d3a, 0x011d3d, 0x011d45, 0x011d46,
    0x011d47, 0x011d59, 0x011d65, 0x011d68, 0x011d89, 0x011d8e, 0x011d91,
    0x011d97, 0x011d98, 0x011da9, 0x011ef2, 0x011ef6, 0x012399, 0x01246e,
    0x012543, 0x01342e, 0x014646, 0x016a38, 0x016a5e, 0x016a69, 0x016aed,
    0x016af4, 0x016b2f, 0x016b36, 0x016b43, 0x016b59, 0x016b77, 0x016b8f,
    0x016e7f, 0x016f4a, 0x016f4f, 0x016f50, 0x016f87, 0x016f92, 0x016f9f,
    0x016fe1, 0x016fe3, 0x0187f7, 0x018af2, 0x01b11e, 0x01b152, 0x01b167,
    0x01b2fb, 0x01bc6a, 0x01bc7c, 0x01bc88, 0x01bc99, 0x01bc9e, 0x01d169,
    0x01d172, 0x01d182, 0x01d18b, 0x01d1ad, 0x01d244, 0x01d454, 0x01d49c,
    0x01d49f, 0x01d4a2, 0x01d4a6, 0x01d4ac, 0x01d4b9, 0x01d4bb, 0x01d4c3,
    0x01d505, 0x01d50a, 0x01d514, 0x01d51c, 0x01d539, 0x01d53e, 0x01d544,
    0x01d546, 0x01d550, 0x01d6a5, 0x01d6c0, 0x01d6da, 0x01d6fa, 0x01d714,
    0x01d734, 0x01d74e, 0x01d76e, 0x01d788, 0x01d7a8, 0x01d7c2, 0x01d7cb,
    0x01d7ff, 0x01da36, 0x01da6c, 0x01da75, 0x01da84, 0x01da9f, 0x01daaf,
    0x01e006, 0x01e018, 0x01e021, 0x01e024, 0x01e02a, 0x01e12c, 0x01e136,
    0x01e13d, 0x01e149, 0x01e14e, 0x01e2eb, 0x01e2f9, 0x01e8c4, 0x01e8d6,
    0x01e943, 0x01e94a, 0x01e94b, 0x01e959, 0x01ee03, 0x01ee1f, 0x01ee22,
    0x01ee24, 0x01ee27, 0x01ee32, 0x01ee37, 0x01ee39, 0x01ee3b, 0x01ee42,
    0x01ee47, 0x01ee49, 0x01ee4b, 0x01ee4f, 0x01ee52, 0x01ee54, 0x01ee57,
    0x01ee59, 0x01ee5b, 0x01ee5d, 0x01ee5f, 0x01ee62, 0x01ee64, 0x01ee6a,
    0x01ee72, 0x01ee77, 0x01ee7c, 0x01ee7e, 0x01ee89, 0x01ee9b, 0x01eea3,
    0x01eea9, 0x01eebb, 0x02a6d6, 0x02b734, 0x02b81d, 0x02cea1, 0x02ebe0,
    0x02fa1d, 0x0e01ef,
)
VALID_STARTERS: Tuple[bool, ...] = (
    False, False, False, False, False, False, False, False, True, False, True,
    True, False, True, True, False, True, True, True, True, True, True, True,
    True, False, True, True, True, True, True, False, True, True, True, True,
    True, False, True, True, True, True, False, False, False, False, False,
    True, True, False, True, False, True, False, True, True, False, False,
    True, False, False, True, False, True, True, True, False, True, False,
    True, False, True, False, True, False, True, True, False, True, False,
    True, False, True, False, True, False, True, False, True, True, True,
    False, False, True, False, True, False, True, False, True, False, False,
    True, False, True, True, True, True, True, True, False, True, False,
    False, False, True, False, True, True, False, False, True, True, False,
    False, True, True, True, True, True, True, True, False, False, False,
    False, False, True, True, False, True, False, False, True, True, True,
    True, True, True, False, True, False, False, False, True, True, False,
    False, True, False, False, True, True, True, True, True, True, False,
    True, False, False, False, False, True, True, False, False, True, False,
    True, True, True, True, True, True, True, True, True, True, False, False,
    False, True, False, False, False, True, True, True, True, True, False,
    False, False, False, True, True, False, False, True, False, True, True,
    True, True, True, False, True, False, False, False, False, True, True,
    False, False, True, False, True, True, True, False, True, False, False,
    False, True, True, False, True, False, False, True, False, True, True,
    True, True, True, False, False, False, False, False, False, True, False,
    True, False, True, False, False, True, True, True, True, True, True,
    False, True, False, True, True, True, False, False, True, True, False,
    False, False, False, False, False, True, True, False, False, True, False,
    False, False, True, False, True, False, True, False, True, False, True,
    False, True, False, True, False, True, False, True, False, True, True,
    True, True, True, True, True, True, True, True, True, True, True, True,
    True, True, True, True, True, True, False, False, True, True, True, True,
    True, True, True, True, True, True, False, True, False, True, False, True,
    True, False, True, False, True, True, False, False, False, False, True,
    True, False, True, True, True, False, False, False, True, True, True,
    True, False, True, False, True, False, False, False, False, True, False,
    False, True, False, True, False, False, False, True, False, True, False,
    True, False, True, False, False, True, False, True, True, True, True,
    False, False, True, False, True, False, True, False, True, True, False,
    False, True, True, True, True, True, True, True, True, True, True, True,
    True, True, True, True, True, True, True, True, False, False, True, True,
    True, False, False, False, True, True, True, True, True, True, True, True,
    True, True, True, True, True, True, True, True, True, False, True, True,
    True, True, True, True, False, True, True, True, True, True, True, True,
    True, True, False, True, True, False, True, True, True, False, True, True,
    True, True, True, True, True, True, True, True, True, True, True, False,
    True, True, False, False, True, False, True, False, True, True, True,
    True, True, False, True, False, True, False, True, False, True, False,
    True, False, False, False, True, True, True, False, True, False, True,
    False, True, False, True, False, True, False, True, False, True, False,
    True, True, False, True, False, True, False, False, True, True, False,
    True, False, True, False, True, False, True, False, True, False, True,
    True, True, False, True, False, True, True, True, True, True, True, True,
    True, False, False, False, True, True, True, True, True, True, True, True,
    False, True, True, True, True, True, True, True, True, True, True, True,
    True, False, False, False, False, True, True, True, True, True, True,
    True, False, True, False, True, True, False, True, True, True, True, True,
    True, True, True, True, True, True, True, True, False, True, True, False,
    True, True, True, False, True, True, True, True, True, False, True, True,
    True, True, True, True, True, True, True, True, True, True, True, True,
    True, True, True, True, True, True, True, True, False, False, False, True,
    True, True, False, False, True, True, True, True, False, True, True, True,
    True, True, True, True, True, False, False, True, True, True, False, True,
    False, True, False, False, False, True, False, True, False, False, True,
    False, False, True, False, True, False, True, False, True, False, True,
    False, False, True, True, True, True, False, False, True, True, True,
    True, True, True, False, False, False, True, True, True, True, True, True,
    False, True, False, False, False, True, False, True, False, False, False,
    True, False, True, False, False, True, True, False, True, True, False,
    True, False, False, True, False, True, False, True, False, True, False,
    True, False, True, False, False, True, False, True, False, True, True,
    True, False, False, True, True, False, True, False, True, False, True,
    False, False, True, False, True, False, True, True, True, True, False,
    False, True, False, True, False, False, True, True, True, False, False,
    False, False, True, False, False, True, True, True, False, False, False,
    True, False, True, False, True, True, True, True, True, True, True, False,
    True, False, True, False, True, False, True, True, True, True, False,
    True, False, False, True, True, True, True, True, True, True, True, True,
    True, True, True, True, False, False, False, False, False, False, False,
    True, True, True, True, True, True, True, True, True, True, True, True,
    True, True, True, True, True, True, True, True, True, True, True, True,
    True, True, True, True, True, True, False, False, False, False, False,
    False, False, False, False, False, False, False, True, False, True, False,
    True, True, False, True, False, True, False, True, False, True, True,
    True, True, True, True, True, True, True, True, True, True, True, True,
    True, True, True, True, True, True, True, True, True, True, True, True,
    True, True, True, True, True, True, True, True, True, True, True, True,
    True, False,
)
