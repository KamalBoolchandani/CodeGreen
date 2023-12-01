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


@app.route('/process_code', methods=['POST'])
def stats():
    data = request.get_json()
    user_input = data['input']
    result = f"Processed input: {user_input}"
    # carbon_stats = calculate_carbon_stats(result):
    static_results = """  
    Complete summary of carbon emission
    GPU : 0.00 W during 0.01 s [measurement time: 0.0050]
    Energy consumed for all CPUs : 0.000000 kWh. Total CPU Power : 7.5 W
    CPU : 7.50 W during 0.02 s [measurement time: 0.0039]
    0.000000 kWh of electricity used since the beginning.
    last_duration=0.017400026321411133
    """
    return jsonify({'result': static_results})
    

    

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


# def  calculate_carbon_stats():
    # calculation code here




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