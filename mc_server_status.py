import requests


class MCServerStatus:
    __url_api = "https://api.mcsrvstat.us"

    def __init__(self, server_address: str, bedrock=False):
        self.server_address = server_address
        self.bedrock = bedrock
        self.get_api_url = self.__url_api
        self.__api_version = 3
        self.__request_exception = requests.RequestException
        if bedrock:
            self.__server_status_access = f"{self.get_api_url}/bedrock/{self.__api_version}/{self.server_address}"
            self.__simple_status_access = f"{self.get_api_url}/bedrock/simple/{self.server_address}"
        else:
            self.__server_status_access = f"{self.get_api_url}/{self.__api_version}/{self.server_address}"
            self.__simple_status_access = f"{self.get_api_url}/simple/{self.server_address}"

    def get_api_address_complete(self, simple=False):
        return self.__simple_status_access if simple else self.__server_status_access

    def get_info_server(self, simple=False):
        try:
            return requests.get(self.__simple_status_access) if simple else (requests.get(self.__server_status_access)
                                                                             .json())
        except requests.RequestException as e:
            print("Erreur lors de la connexion au serveur : ", e)
            return
        except KeyError as e:
            print("Erreur lors de la récupération des données : ", e)
            return None

    def get_online(self, simple=False):
        try:
            return self.get_info_server(True) if simple else self.get_info_server()["online"]
        except self.__request_exception as e:
            print("Erreur lors de la récupération des données : ", e)
            return False
        except KeyError as e:
            print("Erreur lors de la récupération des données : ", e)
            return None

    def get_ip(self):
        try:
            return self.get_info_server()["ip"]
        except self.__request_exception as e:
            print("Erreur lors de la récupération des données : ", e)
            return None
        except KeyError as e:
            print("Erreur lors de la récupération des données : ", e)
            return None

    def get_port(self):
        try:
            return self.get_info_server()["port"]
        except self.__request_exception as e:
            print("Erreur lors de la récupération des données : ", e)
            return None
        except KeyError as e:
            print("Erreur lors de la récupération des données : ", e)
            return None

    def get_hostname(self):
        try:
            return self.get_info_server()["hostname"]
        except self.__request_exception as e:
            print("Erreur lors de la récupération des données : ", e)
            return None
        except KeyError as e:
            print("Erreur lors de la récupération des données : ", e)
            return None

    def get_debug(self, option):
        try:
            return self.get_info_server()["debug"][option]
        except self.__request_exception as e:
            print("Erreur lors de la récupération des données : ", e)
            return None
        except KeyError as e:
            print("Erreur lors de la récupération des données : ", e)
            return None

    def get_version(self):
        try:
            return self.get_info_server()["version"]
        except self.__request_exception as e:
            print("Erreur lors de la récupération des données : ", e)
            return None
        except KeyError as e:
            print("Erreur lors de la récupération des données : ", e)
            return None


if __name__ == "__main__":
    test = MCServerStatus("hypixel.net")
    print(test.get_ip(), test.get_version(), test.get_online())