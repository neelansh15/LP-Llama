import logging
import sys

logger = logging.getLogger(__name__)


def main():
    pass


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO)
    main()
