from fittrackee import create_app, db
from fittrackee.users.models import User
from fittrackee.workouts.models import Workout, Sport
from datetime import datetime, timedelta, timezone

app = create_app()
with app.app_context():
    users = User.query.all()
    if not users:
        print("No users found")
        exit(1)
    
    sport_cycling = db.session.get(Sport, 1)
    sport_running = db.session.get(Sport, 5) # Running is id 5
    if not sport_running:
        sport_running = sport_cycling

    for user in users:
        print(f"Adding data for {user.username}...")
        workouts = [
            Workout(
                user_id=user.id,
                sport_id=sport_cycling.id,
                workout_date=datetime.now(timezone.utc) - timedelta(days=5),
                distance=25.5,
                duration=timedelta(hours=1, minutes=10)
            ),
            Workout(
                user_id=user.id,
                sport_id=sport_running.id,
                workout_date=datetime.now(timezone.utc) - timedelta(days=4),
                distance=5.2,
                duration=timedelta(minutes=30)
            ),
            Workout(
                user_id=user.id,
                sport_id=sport_cycling.id,
                workout_date=datetime.now(timezone.utc) - timedelta(days=3),
                distance=30.0,
                duration=timedelta(hours=1, minutes=20)
            ),
            Workout(
                user_id=user.id,
                sport_id=sport_running.id,
                workout_date=datetime.now(timezone.utc) - timedelta(days=2),
                distance=8.0,
                duration=timedelta(minutes=45)
            ),
            Workout(
                user_id=user.id,
                sport_id=sport_cycling.id,
                workout_date=datetime.now(timezone.utc) - timedelta(days=1),
                distance=12.5,
                duration=timedelta(minutes=40)
            )
        ]
        
        # Enrich with more stats
        workouts[0].moving = timedelta(hours=1, minutes=5)
        workouts[0].ascent = 250.0
        workouts[0].descent = 250.0
        workouts[0].ave_speed = 22.0
        workouts[0].max_speed = 45.0
        workouts[0].calories = 600

        workouts[1].moving = timedelta(minutes=28)
        workouts[1].ascent = 50.0
        workouts[1].descent = 50.0
        workouts[1].ave_speed = 10.4
        workouts[1].max_speed = 12.0
        workouts[1].calories = 300

        workouts[2].moving = timedelta(hours=1, minutes=15)
        workouts[2].ascent = 400.0
        workouts[2].descent = 400.0
        workouts[2].ave_speed = 24.0
        workouts[2].max_speed = 50.0
        workouts[2].calories = 800

        workouts[3].moving = timedelta(minutes=43)
        workouts[3].ascent = 80.0
        workouts[3].descent = 80.0
        workouts[3].ave_speed = 10.6
        workouts[3].max_speed = 13.0
        workouts[3].calories = 450

        workouts[4].moving = timedelta(minutes=38)
        workouts[4].ascent = 120.0
        workouts[4].descent = 120.0
        workouts[4].ave_speed = 20.0
        workouts[4].max_speed = 35.0
        workouts[4].calories = 400

        for w in workouts:
            db.session.add(w)
            db.session.commit()

    print("Rich sample data added successfully for all users")
