def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    #print(title)
    return title

# Don't touch below this line


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")

""""
def main():
    print("Fantasy Quest is booting up...")
    print("Game is running!")
  
main() #---------------->this is correct!!
""""
