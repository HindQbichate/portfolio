# Hind Qbichate – Portfolio

My personal portfolio website, built only in Python with **Streamlit**.
It presents me, my projects, my skills and education, and has a contact form.

**Online version:** https://hind-qbichate-portfolio.streamlit.app

## Pages

- **About me**: presentation, photo, CV download and key figures
- **Projects**: project cards with a filter by tag and a sort by year
- **Skills**: progress bars, bar chart and education timeline
- **Contact**: contact form with validation; messages are saved in `messages.csv`

## Run it on your computer

```bash
git clone https://github.com/HindQbichate/portfolio.git
cd portfolio
pip install -r requirements.txt
streamlit run app.py
```

The site then opens at http://localhost:8501.

## Project structure

```
app.py            entry point: page settings, sidebar, navigation
data.py           all the content of the site (profile, skills, projects, education)
utils.py          pure Python functions (filter projects, check and save the form)
pages/            one file per page
assets/           photo and CV
.streamlit/       config.toml: colours of the site
requirements.txt  libraries to install
```

To add a project, I only add a dictionary to `PROJECTS` in `data.py`: no page needs to change.