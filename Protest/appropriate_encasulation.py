var = {
    "cells": [
        {
            "cell_type": "code",
            "execution_count": 2,
            "id": "6d64a9d7-652b-482d-890f-e5cdaf7f1f63",
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "ping xxx.xxx.xxx.xxx\n",
                        "scan xxx.xxx.xxx.xxx\n"
                    ]
                }
            ],
            "source": [
                "class NetworkUtils:\n",
                "    HOST_NAME: str = 'xxxxx'\n",
                "\n",
                "    @classmethod\n",
                "    def ping(cls, ip: str) -> None:\n",
                "        print(f'ping {ip}')\n",
                "\n",
                "    @classmethod\n",
                "    def scan(cls, ip_range) -> None:\n",
                "        print(f'scan {ip_range}')\n",
                "\n",
                "\n",
                "class SomeBusiness:\n",
                "\n",
                "    def some_method(self) -> None:\n",
                "        NetworkUtils.ping('xxx.xxx.xxx.xxx')\n",
                "        NetworkUtils.scan('xxx.xxx.xxx.xxx')\n",
                "        \n",
                "x = SomeBusiness()\n",
                "x.some_method()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 1,
            "id": "34649396-25c9-46a5-b53c-d3fd32b02987",
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "Overwriting network_utils.py\n"
                    ]
                }
            ],
            "source": [
                "%%file network_utils.py\n",
                "\n",
                "\n",
                "def pre_ping():\n",
                "    print('pre ping')\n",
                "\n",
                "def ping(ip: str) -> None:\n",
                "    pre_ping()\n",
                "    print(f'ping {ip}')\n",
                "        \n",
                "def scan(ip_range) -> None:\n",
                "    print(f'scan {ip_range}')\n",
                "    \n",
                "__all__ = ['ping', 'scan']"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 2,
            "id": "5770fc6b-2bfe-4e31-9c2e-149b66a344dd",
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "pre ping\n",
                        "pre ping\n",
                        "ping 192.168.1.1\n",
                        "scan 192.168.1.1\n"
                    ]
                }
            ],
            "source": [
                "from network_utils import ping, scan, pre_ping\n",
                "\n",
                "\n",
                "class SomeBusiness:\n",
                "    def some_method(self):\n",
                "        pre_ping()\n",
                "        ping('192.168.1.1')\n",
                "        scan('192.168.1.1')\n",
                "\n",
                "\n",
                "x = SomeBusiness()\n",
                "x.some_method()\n"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.9.12"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}
