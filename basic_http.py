import socket
import json
from dice import Dice

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8081))
server_socket.listen(1)
print("Server is listening on port 8081...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established.")

    request = client_socket.recv(4096).decode('utf-8')
    print(f"Request received ({len(request)}):")
    print("*" * 50)
    print(request)
    print("*" * 50)

    if request.startswith("GET /roll_dice"):
        try:
            body = request.split("\r\n\r\n", 1)[1] if "\r\n\r\n" in request else "{}"
            payload = json.loads(body) if body.strip() else {}

            probabilities = payload.get("probabilities", [1/6] * 6)
            number_of_random = payload.get("number_of_random", 1)

            dice = Dice(probabilities)
            results = dice.roll_many(number_of_random)

            response_data = {
                "status": "success",
                "probabilities": probabilities,
                "number_of_random": number_of_random,
                "results": results
            }
            response_json = json.dumps(response_data)
            response = f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{response_json}"

        except (ValueError, KeyError, json.JSONDecodeError) as e:
            error_data = {"status": "error", "message": str(e)}
            response_json = json.dumps(error_data)
            response = f"HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n\r\n{response_json}"

    elif request.startswith("GET /myjson"):
        response_data = {
            "status": "success",
            "message": "Hello, KU!"
        }
        response_json = json.dumps(response_data)
        response = f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{response_json}"

    elif request.startswith("GET"):
        response = f"""HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
                        <html><body><h1>Hello, World!</h1><hr>{request}</body></html>"""
    else:
        response = "HTTP/1.1 405 Method Not Allowed\r\n\r\n"

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()
    print("Waiting for the next TCP request...")
