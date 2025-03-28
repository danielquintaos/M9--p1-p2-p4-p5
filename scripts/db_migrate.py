# scripts/db_migrate.py

from persistence.database import Base, engine

def main():
    print("📦 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ DB schema ready.")

if __name__ == "__main__":
    main()
