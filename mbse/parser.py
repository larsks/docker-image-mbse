import struct

def read_one(name, spec, fd):
    rsize = struct.calcsize(spec)
    raw = fd.read(rsize)

    if not len(raw):
        raise EOFError()
    if len(raw) != rsize:
        raise ValueError('read %d bytes, expected %d' % (len(raw), rsize))

    data = struct.unpack(spec, raw)[0]

    return data

def parse_struct(spec, fd):
    parsed = {}

    for fldspec in spec:
        try:
            fld, spec, sub = fldspec
        except ValueError:
            sub = None
            fld, spec = fldspec

        if sub:
            data = parse_struct(sub, fd)
        elif isinstance(spec, tuple):
            data = [read_one(fld, s, fd) for s in spec]
        else:
            data = read_one(fld, spec, fd)

        parsed[fld] = data

    return parsed
