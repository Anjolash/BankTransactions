```markdown
# Bank Transaction Dashboard  

## Overview  
This project is a **dashboard application** that displays recent bank transactions for individual users upon login. Transactions are retrieved from a custom API and displayed in an intuitive format.  

## Features  
- Displays recent transactions for a logged-in user.  
- Fetches data from a Flask-based REST API deployed on Render.  
- Aggregates and processes datasets from multiple sources.  
- Provides endpoints for retrieving user-specific or group-wide transaction data.  
- Dynamic and responsive dashboard built using Vue.js.  
- Secure user login integrated with Firebase authentication.  

## Technologies Used  
- **Python**: Data processing and backend API development.  
- **Pandas**: Data cleaning, transformation, and merging.  
- **Flask**: Backend API development.  
- **JavaScript**: Interactive frontend development.  
- **Vue.js**: User interface for the dashboard.  
- **Firebase**: User authentication and session management.  
- **Render**: Deployment platform for the Flask API.  
- **GitHub Pages**: Hosting the Vue.js frontend.  

## Live Demo  

- **Frontend Website**: [Bank Transactions Dashboard](https://anjolash.github.io/BankTransactions/)  
- **API**: [Bank Transactions API](https://banktransactions.onrender.com)  
  
You can test the site using the following login credentials:

| **Email**              | **Password** |
|-------------------------|--------------|
| userone@app.com         | 12345678     |
| usertwo@app.com         | 12345678     |
| userthree@app.com       | 12345678     |
| userfour@app.com        | 12345678     |
| userfive@app.com        | 12345678     |
| usersix@app.com         | 12345678     |
| userseven@app.com       | 12345678     |
| usereight@app.com       | 12345678     |
| usernine@app.com        | 12345678     |
| userten@app.com         | 12345678     |
| usereleven@app.com      | 12345678     |
| usertwelve@app.com      | 12345678     |
| userthirteen@app.com    | 12345678     |
| userfourteen@app.com    | 12345678     |
| userfifteen@app.com     | 12345678     |
| usersixteen@app.com     | 12345678     |
| userseventeen@app.com   | 12345678     |
| usereighteen@app.com    | 12345678     |
| usernineteen@app.com    | 12345678     |
| usertwenty@app.com      | 12345678     |
`  

## Project Workflow  

### 1. Dataset Preparation  
- **Data Sources**: Datasets were downloaded from Kaggle.  
- **Data Cleaning**: Removed invalid data, adjusted formats, and standardized fields like dates and IDs.  
- **Data Transformation**: Created unified formats for merging different transaction datasets.  
- **Key Operations**:  
  - Generating random dates for transactions.  
  - Modifying and standardizing customer IDs.  
  - Merging and consolidating data into a unified structure.  

### 2. API Development and Deployment  
- Built using Flask with **CORS** support.  
- **Endpoints**:  
  - `/api/users/transactions`: Fetch transactions grouped by User ID.  
  - `/api/user/<user_id>/transactions`: Fetch all transactions for a specific user.  
  - `/api/user/<user_id>/recent_transactions`: Fetch recent transactions for a user with a configurable limit.  
- **Deployment**:  
  - The API was deployed on [Render](https://render.com) for production.  
  - Deployment included setting up environment variables and configuring build settings.  

### 3. Dynamic Dashboard with Vue.js  

After deploying the API, we built a **Vue.js** dashboard for dynamic transaction visualization.  

- **Key Features**:  
  - **Dynamic API Integration**:  
    - Used the native JavaScript `fetch()` API (not Axios) to make API calls and fetch transaction data.  
    - Dynamically updated the displayed transactions based on user actions, such as clicking "View More."  
  - **Responsive Design**:  
    - Used custom CSS (including Flexbox and Grid) to ensure a responsive and visually appealing dashboard layout.  
  - **Dynamic Transaction Display**:  
    - Transactions were displayed in paginated form, with a "View More" button dynamically loading more data as needed.  
  - **Loading and Error Handling**:  
    - Implemented loading indicators while fetching data.  
    - Displayed user-friendly error messages when transactions failed to load.  

- **Components**:  
  - **TransactionItem**:  
    - A reusable component that displayed individual transaction details, such as merchant name, amount, and timestamp.  
  - **Dynamic Display**:  
    - Used computed properties (`displayedTransactions`) to show only a limited number of transactions based on a dynamic limit.  

### 4. Login Component with Firebase Integration  

To secure the dashboard, we implemented a login system using **Firebase Authentication**.  

- **Key Features**:  
  - **Custom Login Form**:  
    - A simple form for user authentication, allowing users to log in with email and password.  
    - On successful login, redirected to the dashboard and stored the user’s session securely.  
  - **Dynamic User ID Integration**:  
    - The authenticated user’s ID was dynamically injected into the API URL to fetch personalized data:  
      ```javascript
      `${baseUrl}/api/user/${this.userId}/recent_transactions?limit=${this.limit}`
      ```  
  - **Error Handling**:  
    - Displayed error messages for invalid login credentials.  
    - Included a loading indicator during authentication.  

- **Implementation Highlights**:  
  - **Firebase Setup**:  
    - Configured Firebase SDK and initialized it within the Vue.js project.  
  - **Session Management**:  
    - Managed user sessions securely using Firebase's authentication state listener.  
  - **Dynamic "View More" Functionality**:  
    - Users could load more transactions by increasing the `limit` value, triggered by the "View More" button:  
       

## How to Run the Project  

### Prerequisites  
- Python (>= 3.8)  
- Node.js and npm (for Vue.js frontend)  
- Required Python libraries: `Flask`, `pandas`, `numpy`, `flask-cors`  
- Firebase project configured with email/password authentication enabled  

### Steps  

#### Backend API  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/<your-username>/<your-repo-name>.git  
   cd <your-repo-name>  
   ```  

2. **Set Up Backend**:  
   - Navigate to the backend directory (if applicable).  
   - Install dependencies:  
     ```bash  
     pip install -r requirements.txt  
     ```  
   - Run the Flask server locally:  
     ```bash  
     python app.py  
     ```  

#### Frontend Dashboard  
3. **Set Up Frontend**:  
   - Navigate to the frontend directory (if applicable).  
   - Install dependencies:  
     ```bash  
     npm install  
     ```  
   - Add your Firebase configuration to `src/firebase-config.js`.  
   - Start the development server:  
     ```bash  
     npm run serve  
     ```  

4. **Access the Application**:  
   Open your browser and navigate to `http://localhost:8080` (or the appropriate port for Vue.js).  

## File Structure  

```
├── backend/  
│   ├── app.py            # Flask API backend  
│   ├── merged_transactions_with_fullnames.csv  # Processed dataset  
│   ├── requirements.txt  # Backend dependencies  
├── frontend/  
│   ├── src/              # Vue.js source code  
│   ├── public/           # Static assets  
│   ├── src/firebase-config.js  # Firebase configuration  
│   ├── package.json      # Frontend dependencies  
├── data/  
│   ├── raw/              # Raw datasets from Kaggle  
│   ├── processed/        # Cleaned and processed datasets  
├── README.md  
```  

## Future Enhancements  
- **Visualizations**: Add charts and graphs for transaction trends.  
- **OAuth**: Support third-party login (e.g., Google, Facebook).  


## License  
This project is licensed under the MIT License. See the `LICENSE` file for details.  

## Contact  
For inquiries or feedback, contact [anjolash@gmail.com](mailto:anjolash@gmail.com).  
```