import tkinter as tk
import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_API_KEY'

class ChatGPTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatGPT Application")

        # Create UI components
        self.label = tk.Label(root, text="Enter your text:")
        self.entry = tk.Entry(root, width=50)
        self.output_text = tk.Text(root, height=10, width=50)
        self.button = tk.Button(root, text="Process", command=self.process_input)

        # Pack UI components
        self.label.pack(pady=10)
        self.entry.pack(pady=10)
        self.button.pack(pady=10)
        self.output_text.pack(pady=10)

    def process_input(self):
        # Get user input
        user_input = self.entry.get()

        # Process user input using ChatGPT
        response = self.generate_response(user_input)

        # Display the response
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, response)

    def generate_response(self, user_input):
        # Call the OpenAI GPT-3 API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the appropriate engine
            prompt=user_input,
            temperature=0.7,
            max_tokens=150
        )

        return response.choices[0].text

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatGPTApp(root)
    root.mainloop()
