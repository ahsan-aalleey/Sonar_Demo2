# Student Management

Small Python project analyzed with SonarQube Cloud.

- `src/` source code
- `tests/` unit tests
- `.github/workflows/build.yml` CI workflow (tests, coverage, Sonar scan)
- `sonar-project.properties` Sonar settings

Run locally: `pip install -r requirements.txt` then `pytest --cov --cov-report=xml`
