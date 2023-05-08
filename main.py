from loguru import logger

from src.Greeter import Greeter

def main():
    logger.info("Hi there...")
    greeter = Greeter("greeter.sol")

    balance = greeter.get_balance(greeter.user.address)

    logger.info(f"balance: {balance} ethers")

    greeter.deploy()
    greeter.get_contract()
    greeter.set_greet("Hi ...")
    # greeter.last_greet()





if __name__ == "__main__":
    main()
