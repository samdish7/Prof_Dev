#!/usr/bin/env python
import asyncio
from basic_coroutine import lazy_print


def main():
    loop = asyncio.get_event_loop()

    loop.run_until_complete(lazy_print('Hello World'))


if __name__ == '__main__':
    main()
