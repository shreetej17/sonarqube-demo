import calculator
import users

def main():
    print("Welcome to SonarQube Demo Appp")

    a = 10
    b = 0

    result = calculator.divide(a, b)   # Bug: divide by zero
    print("Result:", result)

    user = users.get_user("admin")
    print("User:", user)

if __name__ == "__main__":
    main()
