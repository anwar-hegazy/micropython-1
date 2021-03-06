# Make sure that write operations on io.BytesIO don't
# change original object it was constructed from.
try:
    import uio as io
except ImportError:
    try:
        import io
    except ImportError:
        print('SKIP')
        raise SystemExit

b = b"foobar"

a = io.BytesIO(b)
a.write(b"1")
print(b)
print(a.getvalue())

b = bytearray(b"foobar")

a = io.BytesIO(b)
a.write(b"1")
print(b)
print(a.getvalue())
