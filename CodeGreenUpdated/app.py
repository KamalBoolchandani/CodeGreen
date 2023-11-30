from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import openai

app = Flask(__name__, static_url_path='/static', static_folder='static')

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/code_green')
def code_green():
    return render_template('code_green.html')

@app.route('/optimized')
def optimized():
   # Get the 'output' parameter from the URL
    # output_param = request.args.get('output', default='', type=str)

    # Render the template and pass the output parameter to it
    return render_template('optimized.html')

    

@app.route('/api/greener-code', methods=['POST'])
def get_greener_code():
    try:
        data = request.get_json()
        user_code = data.get('code', '')

        # Add debugging output
        print(f"Received user code: {user_code}")

        # Call the OpenAI API for code optimization
        optimized_code = optimize_code_with_openai(user_code)

        # Add debugging output
        print(f"Optimized code: {optimized_code}")

        return jsonify({'optimizedCode': optimized_code})

    except Exception as e:
        # Print any exceptions for debugging
        print(f"Error: {e}")
        return jsonify({'error': str(e)})

def optimize_code_with_openai(user_code):
    try:
        prompt = f"Optimize the following code to make it greener: {user_code}"

        # Add debugging output
        print(f"Sending prompt to OpenAI API: {prompt}")

        # Call the OpenAI API to generate optimized code
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048,
            temperature=0.7,
        )

        # Add debugging output
        print(f"Received response from OpenAI API: {response}")

        # Extract the generated code from the OpenAI response
        optimized_code=response.choices[0].text.strip()
        # optimized_code = response.choices[0].text.strip()

        return optimized_code

    except Exception as e:
        # Print any exceptions for debugging
        print(f"Error in OpenAI API call: {e}")
        return 'Error getting optimized code.'


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)





# from flask import Flask, render_template, request, jsonify, send_from_directory
# import os
# import openai

# app = Flask(__name__, static_url_path='/static', static_folder='static')

# openai.api_key = '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'

# @app.route('/')
# def index():
#     return render_template('code_green.html')  # Assuming your HTML file is in the templates folder

# @app.route('/api/greener-code', methods=['POST'])
# def get_greener_code():
#     data = request.get_json()
#     user_code = data.get('code', '')

#     # You can process the user's code and get a greener version here
#     # For now, let's assume a simple conversion (for demonstration purposes)
#     greener_code = user_code.replace('for', 'while')

#     return jsonify({'greenerCode': greener_code})

# @app.route('/static/<path:filename>')
# def serve_static(filename):
#     return send_from_directory(app.static_folder, filename)

# if __name__ == '__main__':
#     app.run(debug=True)
# #