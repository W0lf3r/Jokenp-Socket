import socket
import random

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
        except ConnectionRefusedError:
            print("Não foi possível conectar ao servidor. Iniciando modo singleplayer.")
            self.play_singleplayer()

    def play_singleplayer(self):
        print("Bem-vindo ao modo singleplayer!")
        while True:
            print("Escolha:")
            print("1 - Pedra")
            print("2 - Papel")
            print("3 - Tesoura")
            print("0 - Sair")

            choice = input("Digite o número da sua escolha: ")

            if choice == '0':
                break

            moves = {'1': 'pedra', '2': 'papel', '3': 'tesoura'}

            if choice in moves:
                result = self.play_round(choice, str(random.randint(1, 3)))
                print(result)
            else:
                print("Escolha inválida. Tente novamente.")

    def play_multiplayer(self):
        print("Bem-vindo ao modo multiplayer!")
        while True:
            print("Escolha:")
            print("1 - Pedra")
            print("2 - Papel")
            print("3 - Tesoura")
            print("0 - Sair")

            choice = input("Digite o número da sua escolha: ")

            if choice == '0':
                break

            moves = {'1': 'pedra', '2': 'papel', '3': 'tesoura'}

            if choice in moves:
                self.client_socket.send(choice.encode())
                result = self.client_socket.recv(1024).decode()
                print(result)
            else:
                print("Escolha inválida. Tente novamente.")

    def play_round(self, move1, move2):
        choices = {'1': 'pedra', '2': 'papel', '3': 'tesoura'}
        ganhador = None

        if (int(move1) - int(move2)) % 3 == 1:
            ganhador = 'Você'
        elif (int(move2) - int(move1)) % 3 == 1:
            ganhador = 'Computador'
        else:
            ganhador = 'Empate'

        return f"Escolhas: Você - {choices[move1]}, Computador - {choices[move2]}, Resultado: {ganhador}"

if __name__ == "__main__":
    client = Client('127.0.0.1', 12345)
    client.connect()

    while True:
        print("Escolha o modo de jogo:")
        print("1 - Singleplayer")
        print("2 - Multiplayer")
        print("0 - Sair")

        mode_choice = input("Digite o número do modo de jogo desejado: ")

        if mode_choice == '0':
            break
        elif mode_choice == '1':
            client.play_singleplayer()
        elif mode_choice == '2':
            client.play_multiplayer()
        else:
            print("Escolha inválida. Tente novamente.")
