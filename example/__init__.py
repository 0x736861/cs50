import check50

@check50.check()
def hello_world():
    """hello world"""
    check50.run("python3 hello.py").stdout("Hello, world!", regex=False).exit(0)

@check50.check()
def multiline_hello_world():
    """multiline hello world"""
    check50.run("python3 multi_hello.py").stdout("Hello\nWorld!\n", regex=False).exit(0)