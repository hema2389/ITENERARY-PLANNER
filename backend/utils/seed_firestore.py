from utils.firestore import add_document
from schemas.data import Destination

def seed_destinations():
    """
    Adds sample destinations to the Firestore database.
    """
    destinations = [
        Destination(
            destination_id="paris_france",
            name="Paris, France",
            description="The famous capital of France.",
            average_crowd_density=85,
            sustainability_score=60,
            activities=["sightseeing", "museums", "food"]
        ),
        Destination(
            destination_id="colmar_france",
            name="Colmar, France",
            description="A charming town in the Alsace region, known for its well-preserved old town.",
            average_crowd_density=40,
            sustainability_score=80,
            activities=["sightseeing", "wine tasting", "history"]
        ),
        Destination(
            destination_id="kyoto_japan",
            name="Kyoto, Japan",
            description="A city of ancient temples, geishas, and beautiful gardens.",
            average_crowd_density=75,
            sustainability_score=70,
            activities=["temples", "gardens", "culture"]
        ),
        Destination(
            destination_id="takayama_japan",
            name="Takayama, Japan",
            description="A city in the mountainous Hida region, known for its well-preserved Edo-period streets.",
            average_crowd_density=30,
            sustainability_score=85,
            activities=["history", "nature", "culture"]
        ),
    ]

    for dest in destinations:
        add_document('destinations', dest.dict(), document_id=dest.destination_id)
        print(f"Added destination: {dest.name}")

if __name__ == "__main__":
    seed_destinations()
