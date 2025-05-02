Setup Firebase
Add necessary config information in html file 
Create firestore database in firebase and enable authentication 

🔧 1. **Clone the GitHub Repository**

```bash
git clone https://github.com/samruddhi0857/CC-TE-IT.git
cd CC-TE-IT
```
☁️ 2. **Set Up Google Cloud SDK**

If `gcloud` is not already installed:

* Download and install: [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
* Then initialize:

```bash
gcloud init
```

This will:

* Log in to your Google account.
* Let you select a GCP project or create one.

---

 💳 3. **Enable Billing and APIs**

* Make sure billing is enabled.
* Enable the required APIs:

  ```bash
  gcloud services enable appengine.googleapis.com
  gcloud services enable firestore.googleapis.com
  ```

---

🌍 4. **Create App Engine App (First-time only)**

```bash
gcloud app create
```
Choose your region (cannot be changed later).

---

 📦 5. **Install Python Dependencies**

Ensure Python 3.9 is installed (App Engine standard uses 3.9).

Then install the required libraries locally:

```bash
pip install -r requirements.txt
```

---


🚀 7. **Deploy the App**

```bash
gcloud app deploy
```

This will:

* Upload the files.
* Automatically install the required packages from `requirements.txt`.
* Launch the Flask app with Gunicorn.

---

🌐 8. **Access the Web App**

After successful deployment, open it with:

```bash
gcloud app browse
```




