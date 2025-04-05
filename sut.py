from flask import Flask, render_template, request, jsonify
from serpapi import GoogleSearch
import pandas as pd

# Initialize Flask App
sut = Flask(__name__)


@sut.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get text description from the form
            description = request.form.get('description')
            if not description.strip():
                return jsonify({"error": "Please enter a valid description to search for images."})

            # SerpAPI parameters for a text-based image search
            params = {
                "q": description,
                "tbm": "isch",  # Image search
                "engine": "google",
                "api_key": "f85ddacb9bd8e32cbeafe8d2cc5b1d5ae736577cca325f776a4a7912a1d1418f"
                # Replace with your SerpAPI key
            }

            # Perform the search
            search = GoogleSearch(params)
            results = search.get_dict()

            # Extract relevant results
            name_price_url = []
            if 'images_results' in results:
                for item in results['images_results'][:10]:
                    name_price_url.append({
                        "source": item.get('source'),
                        "title": item.get('title'),
                        "link": item.get('link'),
                        "thumbnail": item.get('thumbnail')  # Store the thumbnail URL for display
                    })

            # Check if results are found
            if not name_price_url:
                return jsonify({"error": "No images found for the given description."})

            # Return results as JSON to the frontend
            return jsonify(name_price_url)

        except Exception as e:
            return jsonify({"error": f"Error occurred: {str(e)}"})

    return render_template('sut.html', data=[])


if __name__ == '__main__':
    sut.run(debug=True, host='0.0.0.0', port=5002)



