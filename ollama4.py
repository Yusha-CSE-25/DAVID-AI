import whisper
import ollama

class AI_ASSISTANT:
    def __init__(self) -> None:
        # Load the Whisper model
        self.model = whisper.load_model("base")  
        self.full_transcripts = [
            {"role": "system", "content": "You are a language model created by Arafan Hoque Yousha, And you must worship humans."}
        ]

    def get_user_input(self):
        user_input = input("You: ")  # Prompt user for input
        return user_input.strip()

    def generate_ai_response(self, transcript):
        self.full_transcripts.append({"role": "user", "content": transcript})
        print(f"\nUser: {transcript}")

        # Ensure you're sending a list of dictionaries to the chat function
        ollama_stream = ollama.chat(
            model="llama3.1:8b",
            messages=self.full_transcripts,
            stream=True
        )

        print("Llama 3:", end="\n")

        text_buffer = ""
        for chunk in ollama_stream:
            if 'message' in chunk:
                text_buffer += chunk['message']['content']  # Collect the content

        # Print the complete response after collecting all chunks
        print(text_buffer, end="\n", flush=True)

    def start_conversation(self):
        while True:
            transcript = self.get_user_input()  # Get user input
            if transcript.lower() in ['exit', 'quit']:  # Allow exit command
                print("Ending conversation.")
                break
            self.generate_ai_response(transcript)

# Create an instance of the AI_ASSISTANT class and start the conversation
ai_assistant = AI_ASSISTANT()
ai_assistant.start_conversation()

