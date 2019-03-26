from api.to_do_service import ToDoService


# def test_create_user():
#     headers = ToDoService().login_user()
#     a = ToDoService().get_todos(headers)
#     print(a.content)

def test_create_to_do():
    headers = ToDoService().login_user()
    json = {"content": "TEEEEEEEEEEST"}
    a = ToDoService().add_todo(json, headers)
    assert a.status_code == 200
    print(a.content)
