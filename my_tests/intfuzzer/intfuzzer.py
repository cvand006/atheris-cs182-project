import atheris

with atheris.instrument_imports():
    import ujson
    import sys

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    original = fdp.ConsumeInt(sys.maxsize)

    try:
        ujson_data = ujson.loads(str(original))
    except ValueError:
        return

    dumped = ujson.dumps(ujson_data)

    if dumped != str(original):
        raise RuntimeError("Input: %s\nJSON: %s\nDumped: %s\n" % (original, ujson_data, dumped))

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
