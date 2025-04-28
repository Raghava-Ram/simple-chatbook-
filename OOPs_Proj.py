class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.login_status = False
        self.menu()

    def menu(self):
        opt = input("""Welcome to chatbook! Please select an option:
                    1. Press 1 to signup.
                    2. press 2 to signin.
                    3. press 3 to post your idea.
                    4. press 4 to message your friend.
                    5. press any other key to exit.
                    
                    ---> """)
        if opt == '1':
            self.signup()
        elif opt == '2':
            self.signin()
        elif opt == '3':
            self.post_idea()
        elif opt == '4':
            self.message_friend()
        else:
            print("Exiting the chatbook. Thank you!")
            exit()

    def signup(self):
        print("Please enter your username and password to signup.")
        uname = input("Enter username: ")
        pword = input("Enter password: ")
        self.username = uname
        self.password = pword
        print(f"User {self.username} signed up successfully!")
        self.menu()

    def signin(self):
        print("Please enter your username and password to signin.")
        uname = input("Enter username: ")
        pword = input("Enter password: ")
        if uname == self.username and pword == self.password:
            self.login_status = True
            print(f"User {self.username} signed in successfully!")
            
        else:
            print("Invalid credentials. Please try again.If you are not a user please signup by pressing 1.")
        
        self.menu()

    def post_idea(self):
        if self.login_status:
            idea = input("Please enter your idea: ")
            print(f"Idea posted: {idea}")
        else:
            print("You need to sign in first.")
        self.menu()

    def message_friend(self):
        if self.login_status:
            friend = input("Enter friend's username: ")
            message = input("Enter your message: ")
            print(f"Message sent to {friend}: {message}")
        else:
            print("You need to sign in first.")
        self.menu()

# Create an instance of the chatbook class to start the program
user1 = chatbook()