import json

from rest_framework.views import APIView
from rest_framework.response import Response


class UsersListCreateView(APIView):
    def get(*args, **kwargs):

        try:
            with open('users.json', 'r') as file:
                users = json.load(file)
                return Response(users)
        except FileNotFoundError:
            Response('FileNotFoundError')
        except Exception as err:
            Response(err)

    def post(self, *args, **kwargs):
        user = self.request.data

        try:
            with open('users.json', 'r+') as users_list:
                users = json.load(users_list)
                users.append(user)
                users_list.seek(0)
                json.dump(users, users_list)
                return Response('Created')
        except Exception as err:
            Response(err)


class EmailListCreateView(APIView):
    def get(self, *args, **kwargs):
        response = []

        try:
            with open('newEmails.txt') as file:
                emails = file.readlines()
                for line in emails:
                    items = line.split('\t')
                    mail = items[3].split('\n')
                    response.append(f'{items[0]} - {mail[0]}')
        except Exception as err:
            Response(err)

        return Response(response)

    def post(self, *args, **kwargs):
        gmail = 'gmail.com'
        new_list = []

        try:
            with open('emails.txt') as emails:
                for line in emails:
                    if gmail in line:
                        new_list.append(line)
                with open('newEmails.txt', 'w') as file:
                    file.writelines(new_list)
            return Response('ok')
        except FileNotFoundError:
            Response('FileNotFoundError')
        except Exception as err:
            Response(err)
