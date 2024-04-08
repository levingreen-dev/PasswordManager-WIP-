import json
from difflib import get_close_matches


print("Enter your password...")
check_input: str = input("Password_Check:")


if check_input.lower() == '123':
    print("Welcome to your Password Manager, type quit to exit.")

else:
    print("wrong")


def load_Knowledgebase(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def save_KnowledgeBase(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(
        user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledgeBase: dict) -> str | None:
    for q in knowledgeBase["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None


def load_KnowledgeBase(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def chat_bot():
    KnowledgeBase: dict = load_KnowledgeBase('KnowledgeBase.json')

    while True:
        user_input: str = input("You:")

        if user_input.lower() == 'quit':

            break

       # if user_input.lower() == '123':
       #     pass

      #  else:
      #      break

        best_match: str | None = find_best_match(
            user_input, [q["question"] for q in KnowledgeBase["questions"]])

        if best_match:
            answer: str | None = get_answer_for_question(
                best_match, KnowledgeBase)
            if answer:
                print(f'Bot: {answer}')
            else:
                print('Bot: I don\'t know this info, enter here:')
                new_answer: str = input('Type the answer or "skip" to skip:')

                if new_answer.lower() != 'skip':
                    KnowledgeBase["questions"].append(
                        {"question": user_input, "answer": new_answer})
                    save_KnowledgeBase('KnowledgeBase.json', KnowledgeBase)
                    print('Bot: Thank you, I learned a new response.')
        else:
            print('Bot: I don\'t know this info, enter here:')
            new_answer: str = input('Type the answer or "skip" to skip:')

            if new_answer.lower() != 'skip':
                KnowledgeBase["questions"].append(
                    {"question": user_input, "answer": new_answer})
                save_KnowledgeBase('KnowledgeBase.json', KnowledgeBase)
                print('Bot: Thank you, I learned a new response.')


if __name__ == '__main__':
    chat_bot()
