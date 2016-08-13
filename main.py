from redstone.logger.SystemLogger import SystemLogger
from redstone.network.NetworkFactory import NetworkFactory
import __builtin__

def main():
    __builtin__.systemLogger = SystemLogger()
    __builtin__.server = NetworkFactory()
    server.run_forever(25565)

main()