import fire


nome = 'Gabriel'


def hello(name: str = 'world'):
    """hello _summary_

    Args:
        name (str, optional): _description_. Defaults to 'world'.

    Returns:
        _type_: _description_
    """
    return f'Hello, {name}!'


fire.Fire()
