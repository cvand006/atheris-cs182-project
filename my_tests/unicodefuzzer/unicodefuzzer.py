import atheris

with atheris.instrument_imports():
    import ujson
    import sys

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    original = fdp.ConsumeUnicode(sys.maxsize)

    try:
        ujson_data = ujson.loads(original)
    except ValueError:
        return

#   Still dump encoded string to trigger any possible errors in decoding.
    dumped = ujson.dumps(ujson_data)
    del dumped

#    Simple comparisons do not work because of different handling of whitespace, etc.

#    if ujson_data != dumped:
#        raise RuntimeError("Decryption error! Input: %s\nJSON: %s\nDumped: %s\n" % (original, ujson_data, dumped))

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
