# Codeshetra-Django Project

Codeshetra is a Django project designed to facilitate mock interviews. It provides a platform where interviewees can participate in mock interviews and interviewers can conduct interviews while earning money. The project utilizes Django along with HTML, CSS, and JavaScript, and integrates Razorpay for payment processing. It also incorporates webRTC for real-time video chat capabilities.

## Features
### Confirmation Email Authentication System
* Users are required to confirm their email addresses to authenticate their accounts.
* Confirmation emails are sent upon registration to verify user identities.
## WebRTC Real-Time Video Chat
* Codeshetra implements webRTC technology for real-time video chat functionality.
* Interviewees and interviewers can engage in live video interviews seamlessly within the platform.
## Separate Environment for Video Chat
* Video interviews occur in a separate, secure environment within the platform.
* This ensures privacy and security for both interviewees and interviewers during the interview process.
## Technologies Used
* Django
* HTML
* CSS
* JavaScript
* Razorpay

## Installation and setup
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/your-username/codeshetra-django.git
2. Navigate to the project directory.
   ```bash
   cd codeshetra-django
3. Install Dependencies
   ```bash
   pip install -r requirements.txt
4. Run migrations
   ```bash
   python manage.py migrate
5. Start the Django development server.
   ```bash
   python manage.py runserver
6. Access the application via '**http://localhost:8000**' in your web browser.
## Usage

1. Register for an account as either an interviewee or interviewer.
2. Confirm your email address to authenticate your account.
3. As an interviewee, browse available mock interviews and select one to participate in.
4. As an interviewer, create mock interview sessions and set the price for participation.
5. Engage in real-time video interviews within the secure platform environment.

## Contributors
- [Rohit](https://github.com/RynoCODE)
- [Anurag](https://github.com/codecxAb)
- [Arkaprabha](https://github.com/Arkaprabha13)

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---

Feel free to contribute to the project and make it even better! If you encounter any issues or have suggestions, please create an issue on GitHub. Thank you for using Codeshetra Django! 🚀
