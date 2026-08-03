# Threadline

A lightweight, full-stack **news & content management platform** built with Django. Threadline ships with a public-facing reader experience and a password-protected CMS dashboard — all in a single Django project, with zero external frontend dependencies.

---

## Features

### Public Site
- **Home page** — featured article hero, trending strip, latest articles grid, and per-category previews
- **Category pages** — filtered article listings per topic
- **Article detail** — full article view with related articles sidebar
- **Search** — keyword search across all published articles

### CMS Dashboard *(login required)*
- **Overview** — headline stats (total / published / draft articles, category count) and a recent-articles table
- **Articles** — browse, filter (by keyword / category / status), create, edit, and delete articles
- **Categories** — view all categories with article counts

### Auth
- Sign up, log in (username **or** e-mail), and log out
- All dashboard routes are protected by `@login_required`

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Framework | Django 5.2 |
| Database (dev) | SQLite |
| Database (prod) | PostgreSQL via `dj-database-url` |
| Static files | WhiteNoise (with Brotli compression) |
| WSGI server | Gunicorn |
| Deployment | Railway |

---

## Project Structure

```
threadline/               <- repo root
├── content/              <- main Django app
│   ├── models.py         <- Article & Category models
│   ├── views.py          <- public + dashboard views
│   ├── urls.py           <- URL routing
│   ├── data.py           <- data-access helpers (queries)
│   ├── mock_data.py      <- seed data for dev/demo
│   ├── admin.py          <- Django admin registration
│   └── templates/        <- HTML templates
│       └── content/
│           ├── home.html
│           ├── category.html
│           ├── article_detail.html
│           ├── search.html
│           ├── login.html
│           ├── signup.html
│           └── dashboard/
│               ├── overview.html
│               ├── articles.html
│               ├── article_create.html
│               ├── article_edit.html
│               └── categories.html
├── threadline/           <- Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/               <- project-level static assets
├── staticfiles/          <- collected statics (generated, do not edit)
├── templates/            <- project-level templates
├── manage.py
├── requirements.txt
├── Procfile              <- Railway / Heroku process definition
├── runtime.txt           <- Python version pin
└── .env.example          <- environment variable template
```

---

## Getting Started

### Prerequisites
- Python 3.12+
- `pip`

### 1 — Clone & create a virtual environment

```bash
git clone <your-repo-url>
cd threadline

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 2 — Install dependencies

```bash
pip install -r requirements.txt
```

### 3 — Configure environment variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

| Variable | Description | Default |
|---|---|---|
| `SECRET_KEY` | Django secret key | Insecure dev key (change in prod!) |
| `DEBUG` | Enable debug mode | `True` |
| `DATABASE_URL` | PostgreSQL connection string | None (SQLite used locally) |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` |

> **Note:** The app will automatically fall back to SQLite when `DATABASE_URL` is not set, so no database setup is needed for local development.

### 4 — Apply migrations & seed the database

```bash
python manage.py migrate
python manage.py seed_db   # loads mock articles and categories
```

### 5 — Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6 — Run the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** to view the site.
The CMS dashboard is at **http://127.0.0.1:8000/dashboard/**.

---

## URL Reference

| URL | View | Description |
|---|---|---|
| `/` | `home` | Homepage |
| `/category/<slug>/` | `category` | Articles by category |
| `/article/<slug>/` | `article_detail` | Single article |
| `/search/` | `search` | Keyword search |
| `/login/` | `login_view` | Login page |
| `/logout/` | `logout_view` | Logout |
| `/signup/` | `signup_view` | Registration |
| `/dashboard/` | `dashboard` | CMS overview *(auth required)* |
| `/dashboard/articles/` | `dashboard_articles` | Manage articles *(auth required)* |
| `/dashboard/articles/create/` | `dashboard_article_create` | New article *(auth required)* |
| `/dashboard/articles/<id>/edit/` | `dashboard_article_edit` | Edit article *(auth required)* |
| `/dashboard/articles/<id>/delete/` | `dashboard_article_delete` | Delete article *(auth required)* |
| `/dashboard/categories/` | `dashboard_categories` | View categories *(auth required)* |

---

## Data Models

### `Category`
| Field | Type | Notes |
|---|---|---|
| `name` | `CharField` | Display name |
| `slug` | `SlugField` | Unique identifier used in URLs |
| `description` | `TextField` | Optional |

### `Article`
| Field | Type | Notes |
|---|---|---|
| `title` | `CharField` | |
| `slug` | `SlugField` | Unique, used in URLs |
| `excerpt` | `TextField` | Short summary |
| `content` | `TextField` | Full body |
| `image` | `URLField` | Cover image URL |
| `author` | `CharField` | Author name |
| `category` | `ForeignKey -> Category` | Linked by slug |
| `status` | `CharField` | `draft` or `published` |
| `featured` | `BooleanField` | Pinned to hero slot |
| `created_at` | `DateTimeField` | Auto-set on creation |

---

## Deployment (Railway)

The project is pre-configured for **Railway** deployment.

1. Create a new Railway project and connect your GitHub repo.
2. Add a **PostgreSQL** plugin and copy the connection string to a `DATABASE_URL` environment variable.
3. Set a strong `SECRET_KEY` environment variable.
4. Railway will detect the `Procfile` and run:
   ```
   python manage.py migrate && python manage.py seed_db && python manage.py collectstatic --noinput && gunicorn threadline.wsgi
   ```
5. Set `DEBUG=False` in production environment variables.

---

## Contributing

1. Fork the repo and create your feature branch (`git checkout -b feature/my-feature`)
2. Commit your changes (`git commit -m 'Add my feature'`)
3. Push to the branch (`git push origin feature/my-feature`)
4. Open a Pull Request

---

## License

This project is open-source. See [LICENSE](LICENSE) for details.
