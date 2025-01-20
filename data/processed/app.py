from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load the merged dataset
MERGED_CSV_FILE = "merged_transactions_with_fullnames.csv"
data = pd.read_csv(MERGED_CSV_FILE)

# Endpoint to fetch all transactions grouped by User ID
@app.route("/api/users/transactions", methods=["GET"])
def get_all_user_transactions():
    """
    Fetch all transactions grouped by user.
    Example URL: /api/users/transactions
    """
    # Group transactions by 'User ID' and convert them to a dictionary
    grouped_data = data.groupby("User ID").apply(lambda x: x.to_dict(orient="records"))
    result = grouped_data.to_dict()

    # Return the grouped transactions as a JSON response
    return jsonify(result)

# Endpoint to fetch transactions for a specific user
@app.route("/api/user/<user_id>/transactions", methods=["GET"])
def get_user_transactions(user_id):
    """
    Fetch transactions for a specific user by their User ID.
    Example URL: /api/user/USER__001/transactions
    """
    user_data = data[data["User ID"] == user_id]

    # Check if the user has any transactions
    if user_data.empty:
        return jsonify({"message": f"No transactions found for User ID: {user_id}"}), 404

    # Convert the user's transactions to a list of dictionaries
    user_transactions = user_data.to_dict(orient="records")
    return jsonify({user_id: user_transactions})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
