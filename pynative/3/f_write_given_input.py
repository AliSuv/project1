def questions():
    n = int(input("Enter how many students are there: "))
    q = [
        "What is your name?: ",
        "What is your surname?: ",
        "What is you grade from the exam?: "]
    
    with open("form.txt", "w") as file:
        for i in range (n):
            file.write(f"Student {i + 1}: \n")
            for question in q:
                answers = input(f"{question} \n")
            file.write(f"\n{q} {answers}")
            file.write("-------------------------- \n")

questions()