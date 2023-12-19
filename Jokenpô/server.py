import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)
        print(f"Servidor escutando na porta {self.port}")

    def start(self):
        player1, addr1 = self.server_socket.accept()
        print(f"Conexão recebida de {addr1}")
        player2, addr2 = self.server_socket.accept()
        print(f"Conexão recebida de {addr2}")

        self.play_game(player1, player2)

    def play_game(self, player1, player2):
        choices = {'1': 'pedra', '2': 'papel', '3': 'tesoura'}

        while True:
            move1 = player1.recv(1024).decode()
            move2 = player2.recv(1024).decode()

            if not move1 or not move2:
                break

            if move1 not in choices or move2 not in choices:
                result = "Escolha inválida! Tente novamente."
            else:
                result = self.calculate_result(move1, move2)

            player1.send(result.encode())
            player2.send(result.encode())

    def calculate_result(self, move1, move2):
        choices = {'1': 'pedra', '2': 'papel', '3': 'tesoura'}
        ganhador = None

        if (int(move1) - int(move2)) % 3 == 1:
            ganhador = 'Jogador 1 vence'
        elif (int(move2) - int(move1)) % 3 == 1:
            ganhador = 'Jogador 2 vence'
        else:
            ganhador = 'Empate'

        return f"Escolhas: Jogador 1 - {choices[move1]}, Jogador 2 - {choices[move2]}, Resultado: {ganhador}"

if __name__ == "__main__":
    server = Server('127.0.0.1', 12345)
    server.start()
