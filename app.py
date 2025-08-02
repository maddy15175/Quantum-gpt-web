from flask import Flask, request, jsonify, send_from_directory
import openai
from qiskit import QuantumCircuit, Aer, execute

# Replace with your actual OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    # Quantum logic (super basic)
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.measure_all()
    simulator = Aer.get_backend('aer_simulator')
    result = execute(qc, simulator, shots=1).result()
    quantum_data = result.get_counts()

    # ChatGPT response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )

    return jsonify({
        "response": f"{response.choices[0].message['content']}\nQuantum Result: {quantum_data}"
    })

if __name__ == "__main__":
    app.run(debug=True)
