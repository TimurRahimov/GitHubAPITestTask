import dotenv
import os
import requests
import unittest


class GitHubAPI(unittest.TestCase):

    def setUp(self):
        dotenv.load_dotenv()
        self.root_url = "https://api.github.com"
        self.username = os.getenv("GH_API_USERNAME")
        self.access_token = os.getenv("GH_API_TOKEN")
        self.repo_name = os.getenv("GH_API_REPOSITORY_NAME")

    def test_creating_and_deleting_new_public_repo(self):
        self.__creating_new_public_repo()
        self.__getting_added_public_repo()
        self.__deleting_added_public_repo()
        self.__getting_deleted_public_repo()

    def __creating_new_public_repo(self):
        url = f"{self.root_url}/user/repos"
        data = {
            "name": self.repo_name
        }

        response = requests.post(url, headers=self.__get_auth_headers(), json=data)

        self.assertEqual(response.status_code, 201)

    def __getting_added_public_repo(self):
        url = f"{self.root_url}/users/{self.username}/repos"

        response = requests.get(url, headers=self.__get_auth_headers())

        public_repos_list = response.json()
        self.assertEqual(any(repo['name'] == self.repo_name for repo in public_repos_list), True)

    def __deleting_added_public_repo(self):
        url = f"{self.root_url}/repos/{self.username}/{self.repo_name}"
        response = requests.delete(url, headers=self.__get_auth_headers())
        self.assertEqual(response.status_code, 204)

    def __getting_deleted_public_repo(self):
        url = f"{self.root_url}/users/{self.username}/repos"

        response = requests.get(url, headers=self.__get_auth_headers())

        public_repos_list = response.json()
        self.assertEqual(any(repo['name'] == self.repo_name for repo in public_repos_list), False)

    def __get_auth_headers(self):
        return {
            "Authorization": f"token {self.access_token}"
        }

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
