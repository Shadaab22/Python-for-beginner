from Issue_Track_System import *
class Issue:
    def __init__(self, id, title, description, status):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

class IssueTracker:
    def __init__(self, filename="Issue_store.txt"):
        self.issues=[]
        self.filename=filename
        try:
            self.load_issues_from_file()
            print("Issues loaded successfully")
        except FileNotFoundError:
            print("No existing issues file found")

    def create_issue(self, id, title, description):
        for issue in self.issues:
            if issue.id == id:
                print(f"Issue {id} already exists")
                issue.status = "Resolved"
                self.save_issues_to_file()
                return
        issue = Issue(id, title, description, "Pending")
        self.issues.append(issue)
        self.save_issues_to_file()
        print("New issue added successfully")

    def save_issues_to_file(self):
        with open(self.filename, "w") as file:
            for issue in self.issues:
                file.write(f"{issue.id},{issue.title},{issue.description},{issue.status}\n")

    def load_issues_from_file(self):
        with open(self.filename, "r") as file:
            for line in file:
                id, title, description, status = line.strip().split(",")
                self.issues.append(Issue(id, title, description, status))

    def remove_issue(self, id):
        for issue in self.issues:
            if issue.id == id and issue.status == "Resolved":
                self.issues.remove(issue)
                self.save_issues_to_file()
                return True
        return False

    def resolve_issue(self, id):
        issue = self.get_issue(id)
        if issue:
            issue.status = "Resolved"
            print(f"Issue {id} resolved successfully")
            self.save_issues_to_file()
        else:
            print(f"No issue found with ID {id}")

    def status_of_issue(self, id):
        issue = self.get_issue(id)
        if issue:
            print(f"Issue {id} status: {issue.status}")
        else:
            print(f"Issue {id} not found")

    def get_issue(self, id):
        for issue in self.issues:
            if issue.id == id:
                return issue
        return None

def main():
    obj = IssueTracker()
    user = input("Are you Worker or User? : ")

    if user == "Worker":
        worker_pin = 890
        for p in range(3):
            pin = int(input("Enter your pin to enter: "))
            if pin == worker_pin:
                print("Welcome to your routine")
                break
            else:
                print("Wrong pin")
                print(f"{p} attempts completed, {3-p} attempts remaining")
        else:
            print("Account frozen")
            return

    while True:
        if user == "User":
            print("\na. Add a new issue")
            print("b. Check status of an issue")
            print("c. Exit")
        elif user == "Worker":
            print("1. Get an existing issue")
            print("2. List all issues")
            print("3. Remove an issue")
            print("4. Resolve an issue")
            print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == 'a':
            id = input("Enter issue ID: ")
            title = input("Enter the title of issue: ")
            description = input("Enter the description of your issue: ")
            obj.create_issue(id, title, description)
        elif choice == '1':
            issue_id = input("Enter the issue ID: ")
            issue = obj.get_issue(issue_id)
            if issue:
                print(f"Issue ID: {issue.id}, Title: {issue.title}, Description: {issue.description}, Status: {issue.status}")
            else:
                print(f"No issue found with ID: {issue_id}")
        elif choice == '2':
            print("All issues:")
            for issue in obj.issues:
                print(f"Issue ID: {issue.id}, Title: {issue.title}, Description: {issue.description}, Status: {issue.status}")
        elif choice == '3':
            issue_id = input("Enter the issue ID to delete: ")
            if obj.remove_issue(issue_id):
                print(f"Issue with ID {issue_id} removed successfully")
            else:
                print(f"No issue found with ID: {issue_id}")
        elif choice == 'b':
            issue_id = input("Enter the issue ID to check its status: ")
            obj.status_of_issue(issue_id)
        elif choice == '4':
            issue_id = input("Enter the issue ID to be resolved: ")
            obj.resolve_issue(issue_id)
        elif choice == '5' or choice == 'c':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
main()