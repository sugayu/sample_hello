'''Sample to say hello
'''

__all__ = ['world', 'test_function']


def test_function(
    input_a: int,
    input_b: float,
    input_c: str = 'test',
    input_d: float = 3.0,
    input_e: str = 'test',
) -> None:
    '''[short desc]

    Args:
        input_a (int):
        input_b (float):
        input_c (str, optional): Defaults to 'test'.
        input_d (float, optional): Defaults to 3.0.
        input_e (str, optional): Defaults to 'test'.

    Returns:
        None: [description]

    Examples:
        >>>

    Note:
        [note]
    '''
    print('This is test.')


def world():
    '''Say hello to the world.
    '''
    print('hello, world')


def main():
    world()
    return


if __name__ == '__main__':
    main()
