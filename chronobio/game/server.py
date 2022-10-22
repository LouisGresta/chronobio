import argparse
import json
from pprint import pprint
from time import sleep

from chronobio.game.constants import MAX_NB_PLAYERS, SERVER_CONNECTION_TIMEOUT
from chronobio.game.game import Game
from chronobio.network.server import Server


class GameServer(Server):
    def __init__(self: "GameServer", host: str, port: int):
        super().__init__(host, port)
        self.game = Game()

    def _turn(self: "GameServer"):
        self.game.new_day()
        state = json.dumps(self.game.state()) + "\n"
        print("Sending current state")
        pprint(state)
        for client in self.clients:
            client.network.write(state)

    def run(self: "GameServer") -> None:
        while not [client for client in self.clients if not client.spectator]:
            print("Waiting for player clients")
            sleep(1)

        for second in range(1, SERVER_CONNECTION_TIMEOUT + 1):
            print(f"Waiting other players ({second}/{SERVER_CONNECTION_TIMEOUT})")
            if (
                len([client for client in self.clients if not client.spectator])
                == MAX_NB_PLAYERS
            ):
                break
            sleep(1)

        for player_name in {
            client.name for client in self.clients if not client.spectator
        }:
            self.game.add_player(player_name)
        while True:
            print("New game turn", self.game.day + 1)
            self._turn()
            sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game server.")
    parser.add_argument(
        "-a",
        "--address",
        type=str,
        help="name of server on the network",
        default="localhost",
    )
    parser.add_argument(
        "-p", "--port", type=int, help="location where server listens", default=16210
    )
    args = parser.parse_args()

    GameServer(args.address, args.port).run()
