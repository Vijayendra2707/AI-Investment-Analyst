from time import sleep

from groq import InternalServerError


def invoke_with_retry(chain, data):

    delays = [1, 2, 4]

    for i, delay in enumerate(delays):

        try:

            return chain.invoke(data)

        except InternalServerError:

            if i == len(delays) - 1:
                raise

            sleep(delay)