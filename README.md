Project Title: Web Scrapping with Streamlit Application

1.Goal: To develop a web application that allows users to search for doctors based on their specialization and location, and retrieve relevant information from Practo's website through web scraping.

2.Aim: Create a user-friendly Streamlit web application that allows users to search for doctors by specialization and location, retrieve detailed doctor information from Practo, and present it in an accessible and interactive format using Pandas and Streamlit.

3.Installation Requirements: To run the application, you need to install the following packages:
	i) Streamlit: For creating and managing the web interface.
	ii) BeautifulSoup4: For parsing HTML content.
	iii) Requests: For sending HTTP requests to the Practo website.
	iv) Pandas: For handling and displaying data in a structured format.

4.Workflow: The application follows a series of steps to complete the project. 
Those steps are:
	i) User Inputs: Users select a doctor's specialization from the dropdown menu and input a location (e.g., city name) in the text box. Once both the specialization and location are chosen, users submit their search query by clicking the "Scrape" button.
	
  ii) Form Submission: Upon form submission, the app constructs a URL based on the user input (location and doctor specialization) and sends an HTTP request to Practo’s website to retrieve relevant doctors' information for the specified location and specialization.
	
  iii) Web Scrapping: The script scrapes doctors' details, including their names, consultation fees, experience, and profile links, from the Practo website. It does this by fetching the HTML content from the site and parsing it using BeautifulSoup.
For each doctor, it gathers:
	Doctor's Name (Full Name)
	Consultation Fees (converting them into Indian Rupees if in AED)
	Experience (in years)
	Doctor's Profile Link (constructs the proper URL)
	
  iv) Error Handling: If the location is unavailable on Practo, it shows a warning and if no doctors are available in the specified location and specialization, it displays a message indicating that no results were found.

  v) Output: If doctors are found, their profiles are displayed in a DataFrame using Pandas and Streamlit’s data_editor, with columns for name, consultation fees, experience, and a profile link. The total number of doctors is also displayed, along with clickable links to their profiles for more detailed information.

  vi) Deployment: Deploy the program on Streamlit Community Cloud to make it accessible to a broader audience, allowing users to interact with the application via a web-based interface.
Access the application via the provided link: [https://webscrap-practo.streamlit.app] 

