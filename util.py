def ask_question(question):
    response = input(question)
    return response

def ask_yes_no(question):
    while True:
        response = input(question).lower()
        if response in ['y', 'yes', 'ja']:
            return True
        elif response in ['n', 'no', 'nein']:
            return False
        else:
            print("Invalid response. Please answer with 'y', 'yes', 'ja', 'n', 'no' or 'nein'.")
