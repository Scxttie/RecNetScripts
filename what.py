import requests

headers = {
    'Content-Type': 'text/plain; charset=utf-8',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImljMVpGMXJ2dXYtbU9SMnBPX214dWNJcHpTOCIsInR5cCI6ImF0K2p3dCIsIng1dCI6ImljMVpGMXJ2dXYtbU9SMnBPX214dWNJcHpTOCJ9.eyJuYmYiOjE3MjUwNjQwMDEsImV4cCI6MTcyNTA2NzYwMSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnJlYy5uZXQiLCJjbGllbnRfaWQiOiJyZWNyb29tLm1vYmlsZWhvbWUiLCJyb2xlIjoiZ2FtZUNsaWVudCIsInJuLnBsYXQiOiI1Iiwicm4ucGxhdGlkIjoiQ0FEQTg5RjYtNTlBNS00MEVCLUE4MEItOTUxRTFDREJEMjk2Iiwicm4uZGV2aWNlY2xhc3MiOiIzIiwicm4udmVyIjoiMjAyNDA4MTUuMDEiLCJybi5hc2lkIjoiMTcyNTA2Mzk5OTQwMyIsInJuLmR1aWQiOiJsd3A4Vy9VZSIsInJuLmNybSI6IkJyYXplIiwicm4uc2siOiIxOTMzMjY2OTUxIiwic3ViIjoiMzg0NDI1MjMxIiwiYXV0aF90aW1lIjoxNzI1MDY0MDAxLCJpZHAiOiJsb2NhbCIsImp0aSI6IjczNUQ4RjNCQjBGODY0QzY1ODM4NUNDMjcwN0ExNEM5IiwiaWF0IjoxNzI1MDY0MDAxLCJzY29wZSI6WyJybi5hY2NvdW50cyIsInJuLmFwaSIsInJuLmF1dGgiLCJybi5idWdyZXBvcnRpbmciLCJybi5jYXJkcyIsInJuLmNoYXQiLCJybi5jbHVicyIsInJuLmNtcyIsInJuLmNvbW1lcmNlIiwicm4uZGF0YWNvbGxlY3Rpb24iLCJybi5kaXNjb3ZlcnkiLCJybi5sZWFkZXJib2FyZCIsInJuLmxpbmsiLCJybi5saXN0cyIsInJuLm1hdGNoLnJlYWQiLCJybi5tYXRjaC53cml0ZSIsInJuLm1vZGVyYXRpb24iLCJybi5ub3RpZnkiLCJybi5wbGF0Zm9ybW5vdGlmaWNhdGlvbnMiLCJybi5wbGF5ZXJzZXR0aW5ncyIsInJuLnJvb21jb21tZW50cyIsInJuLnJvb21zIiwicm4uc3RvcmFnZSIsInJuLnN0cmluZ3MiLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsiY2FjaGVkX2xvZ2luIl19.vv0ttoSktarQDUtOmbfQFl6wcCKdSnkuZmTVOjjEmVjbjlp1JaVE2Vmb4Eh-wj-pbZE2MJzoWQ-6wY8sYVtyLz2MPnafkQunzYKHujAsqz32_ZJPIsgYzNlDI7TKR6Bp7Dq9GhESFwCHBus01Tgqkzo1xq8SXdmruKpdS_5lgC1L8rWxjHy5byfa-cMyJCt7sKUUnuTZD48WSghCPW2pwdL6sf-a9c1z7T5ed1MQQEStJRnej5LKBuR8tFeNIX4dD8W_Bjb925-zZiue7F1XOU70j2AADsp0qVQxA9--avV9cweX7u_aLuvcdaU5js7IN4kvFBsafUTZUlMwlrsNsQ',
}

params = {
    'id': '1502024',
}

response = requests.get('https://api.rec.net/api/relationships/v2/acceptfriendrequest', params=params, headers=headers)