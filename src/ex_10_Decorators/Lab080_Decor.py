def before_after_ui_test(func):
    def wrapper():
        print('before test')
        func()
        print('after test')
    return wrapper()

@before_after_ui_test
def ui_test():
    print("I am Testing the UI Things")