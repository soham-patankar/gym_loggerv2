# Gym Logger v2

A Python workout logging system that evolves from a simple CLI tool into a REST API across 3 phases.

## Project Structure

| File | Phase | Description |
|------|-------|-------------|
| `workout_logger.py` | Phase 1 | Pure Python CLI — add, view, delete workouts stored in JSON |
| `workout_loggerv2.py` | Phase 2 | CLI + API Ninjas integration — fetch real exercises by muscle group |
| `api_prac2.py` | Phase 3 | Flask REST API — expose workout data over HTTP endpoints |

## Setup

```bash
pip install requests flask
```

## How to Run

**CLI version:**
```bash
python workout_loggerv2.py
```

**API version:**
```bash
python api_prac2.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/workouts` | Returns all logged workouts |
| POST | `/workout` | Adds a new workout |
| DELETE | `/workout/<id>` | Deletes a workout by ID |

## External API Used
- [API Ninjas Exercise API](https://api-ninjas.com/api/exercises)

## Roadmap
- Phase 4 — SQLite database integration
- Phase 5 — Analytics and progress tracking with Pandas

## Built With
Python · Flask · requests · JSON · SQLite (coming)
