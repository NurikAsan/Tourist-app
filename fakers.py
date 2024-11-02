import random
from faker import Faker
from django.utils import timezone
from apps.tour.models import (
    PickupLocations, Category, Program, Equipment,
    Included, NotIncluded, Duration, TourDates, Tour, TourImage, FavoriteTour
)

fake = Faker()


def create_pickup_locations(n=5):
    for _ in range(n):
        PickupLocations.objects.create(
            title=fake.sentence(2),
            latitude=fake.latitude(),
            longitude=fake.longitude()
        )


def create_categories(n=5):
    for _ in range(n):
        Category.objects.create(
            title=fake.sentence(2)
        )

def create_programs(n=5):
    for _ in range(n):
        Program.objects.create(
            title=fake.sentence(2),
            time=fake.time()
        )

def create_equipments(n=5):
    for _ in range(n):
        Equipment.objects.create(
            title=fake.sentence(2)
        )


def create_included(n=6):
    for _ in range(n):
        Included.objects.create(
            title=fake.sentence(2)
        )


def create_not_included(n=5):
    for _ in range(n):
        NotIncluded.objects.create(
            title=fake.sentence(2)
        )


def create_durations(n=5):
    for _ in range(n):
        Duration.objects.create(
            title=fake.sentence(2)
        )


def create_tour_dates(n=10):
    for _ in range(n):
        TourDates.objects.create(
            date=fake.date_between(start_date='today', end_date='+30d')
        )


def create_tours(n=10):
    categories = Category.objects.all()
    durations = Duration.objects.all()
    pickup_locations = PickupLocations.objects.all()
    programs = Program.objects.all()
    equipment = Equipment.objects.all()
    included = Included.objects.all()
    not_included = NotIncluded.objects.all()
    tour_dates = TourDates.objects.all()

    for _ in range(n):
        tour = Tour.objects.create(
            title=fake.sentence(nb_words=3),
            point=fake.city(),
            description=fake.text(max_nb_chars=150),
            price=round(random.uniform(50, 500), 2),
            start_date=fake.date_between(start_date='today', end_date='+30d'),
            end_date=fake.date_between(start_date='+30d', end_date='+60d'),
            views=random.randint(0, 1000),
            archived=random.choice([False, False]),
            category=random.choice(categories),
            duration=random.choice(durations)
        )

        tour.pickup_locations.set(random.sample(list(pickup_locations), k=random.randint(1, len(pickup_locations))))
        tour.program.set(random.sample(list(programs), k=random.randint(1, len(programs))))
        tour.equipment.set(random.sample(list(equipment), k=random.randint(1, len(equipment))))
        tour.included.set(random.sample(list(included), k=random.randint(1, len(included))))
        tour.not_included.set(random.sample(list(not_included), k=random.randint(1, len(not_included))))
        tour.tour_dates.set(random.sample(list(tour_dates), k=random.randint(1, len(tour_dates))))


def create_tour_images(n=10):
    tours = Tour.objects.all()
    for tour in tours:
        # Generate 1 to 5 images for each tour
        for _ in range(random.randint(1, 5)):
            TourImage.objects.create(
                tour=tour,
                image=fake.image_url()  # Use actual image file handling if needed
            )


def run():
    create_pickup_locations(5)
    create_categories(5)
    create_programs(5)
    create_equipments(5)
    create_included(5)
    create_not_included(5)
    create_durations(5)
    create_tour_dates(10)
    create_tours(10)
    create_tour_images()


if __name__ == "__main__":
    run()
