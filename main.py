import os

from services.gateway.infrastructures.http.server import create_and_start_server as gateway_service
from services.service1.infrastructures.http.server import create_and_start_server as service1
from services.service2.infrastructures.http.server import create_and_start_server as service2

SERVICE = os.getenv('SERVICE')

services = {
    'gateway': gateway_service,
    'service1': service1,
    'service2': service2
}

if __name__ == '__main__':
    execute = services.get(SERVICE)
    execute()
